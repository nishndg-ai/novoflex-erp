from __future__ import annotations

from typing import Any

from sqlalchemy import (
    MetaData,
    Table,
    insert,
    select,
    update,
)

from sqlalchemy.orm import Session

from app.platform.query import QueryService

from app.platform.master_engine.audit import (
    AuditEngine,
)

from app.platform.master_engine.history import (
    HistoryEngine,
)


class RuntimeAccessError(Exception):
    """
    Raised when runtime data access violates
    company / plant ownership rules.
    """
    pass



class RuntimeDataEngine:
    """
    Generic Runtime Data Engine.

    Handles dynamic ERP tables
    with automatic audit and history tracking.

    BLUISH data security:
    - GLOBAL
    - COMPANY
    - PLANT
    """



    def __init__(
        self,
        db: Session,
    ):

        self.db = db

        self._metadata = MetaData()

        self._tables: dict[str, Table] = {}

        self.query_service = QueryService(
            db
        )

        self.audit = AuditEngine()

        self.history = HistoryEngine()



    # ---------------------------------------------------------
    # Table Cache
    # ---------------------------------------------------------

    def get_table(
        self,
        table_name: str,
    ) -> Table:


        if table_name not in self._tables:

            self._tables[table_name] = Table(

                table_name,

                self._metadata,

                autoload_with=self.db.bind,

            )


        return self._tables[table_name]



    # ---------------------------------------------------------
    # Data Scope Filter
    # ---------------------------------------------------------

    def apply_data_scope_filter(
        self,
        filters: dict[str, Any] | None,
        user_context: dict | None,
        data_scope: str = "GLOBAL",
    ) -> dict[str, Any]:


        runtime_filters = {}


        if filters:

            runtime_filters.update(
                filters
            )


        if not user_context:

            return runtime_filters



        if data_scope == "COMPANY":

            company_id = user_context.get(
                "company_id"
            )


            if company_id is not None:

                runtime_filters[
                    "company_id"
                ] = company_id



        elif data_scope == "PLANT":

            plant_id = user_context.get(
                "plant_id"
            )


            if plant_id is not None:

                runtime_filters[
                    "plant_id"
                ] = plant_id



        return runtime_filters



    # ---------------------------------------------------------
    # Ownership Condition
    # ---------------------------------------------------------

    def apply_scope_condition(
        self,
        table,
        stmt,
        user_context: dict | None,
        data_scope: str,
    ):

        if not user_context:

            return stmt



        if data_scope == "COMPANY":

            company_id = user_context.get(
                "company_id"
            )


            if (
                company_id is not None
                and hasattr(
                    table.c,
                    "company_id",
                )
            ):

                stmt = stmt.where(
                    table.c.company_id == company_id
                )



        elif data_scope == "PLANT":

            plant_id = user_context.get(
                "plant_id"
            )


            if (
                plant_id is not None
                and hasattr(
                    table.c,
                    "plant_id",
                )
            ):

                stmt = stmt.where(
                    table.c.plant_id == plant_id
                )



        return stmt



    # ---------------------------------------------------------
    # List Records
    # ---------------------------------------------------------

    def get_records(
        self,
        table_name: str,
        *,
        filters: dict[str, Any] | None = None,
        search: str | None = None,
        limit: int = 100,
        offset: int = 0,
        order_by: str | None = None,
        descending: bool = False,
        include_deleted: bool = False,
        user_context: dict | None = None,
        data_scope: str = "GLOBAL",
    ) -> dict[str, Any]:


        table = self.get_table(
            table_name
        )


        filters = self.apply_data_scope_filter(

            filters,

            user_context,

            data_scope,

        )


        return self.query_service.execute(

            table=table,

            filters=filters,

            search=search,

            limit=limit,

            offset=offset,

            order_by=order_by,

            descending=descending,

            include_deleted=include_deleted,

        )
            # ---------------------------------------------------------
    # Get Record
    # ---------------------------------------------------------

    def get_record(
        self,
        table_name: str,
        record_id: int,
        user_context: dict | None = None,
        data_scope: str = "GLOBAL",
    ) -> dict[str, Any] | None:


        table = self.get_table(
            table_name
        )


        stmt = select(table).where(

            table.c.id == record_id

        )


        stmt = self.apply_scope_condition(

            table,

            stmt,

            user_context,

            data_scope,

        )


        row = self.db.execute(
            stmt
        ).first()


        if row is None:

            return None


        return dict(row._mapping)





    # ---------------------------------------------------------
    # Insert
    # ---------------------------------------------------------

    def insert(
        self,
        table_name: str,
        module_code: str,
        values: dict[str, Any],
        user: str = "system",
        user_context: dict | None = None,
        data_scope: str = "GLOBAL",
    ) -> int:


        table = self.get_table(
            table_name
        )


        values.setdefault(
            "is_active",
            True,
        )


        values.setdefault(
            "version",
            1,
        )


        # Force ownership

        if user_context:


            if (
                data_scope == "COMPANY"
                and hasattr(
                    table.c,
                    "company_id",
                )
            ):

                company_id = user_context.get(
                    "company_id"
                )

                if company_id is not None:

                    values["company_id"] = company_id



            elif (
                data_scope == "PLANT"
                and hasattr(
                    table.c,
                    "plant_id",
                )
            ):

                plant_id = user_context.get(
                    "plant_id"
                )

                if plant_id is not None:

                    values["plant_id"] = plant_id



        stmt = (

            insert(table)

            .values(**values)

            .returning(table.c.id)

        )


        record_id = (

            self.db.execute(stmt)

            .scalar_one()

        )


        self.db.commit()


        module_name = module_code.upper()


        self.history.add(

            db=self.db,

            module=module_name,

            record_id=record_id,

            action="CREATE",

            user=user,

            changes={

                "new": values

            }

        )


        self.audit.create_log(

            db=self.db,

            action="CREATE",

            module=module_name,

            user=user,

            record_id=record_id,

            new_data=values,

        )


        return record_id





    # ---------------------------------------------------------
    # Update
    # ---------------------------------------------------------

    def update(
        self,
        table_name: str,
        module_code: str,
        record_id: int,
        values: dict[str, Any],
        user: str = "system",
        user_context: dict | None = None,
        data_scope: str = "GLOBAL",
    ) -> None:


        table = self.get_table(
            table_name
        )


        old_data = self.get_record(

            table_name,

            record_id,

            user_context,

            data_scope,

        )


        if old_data is None:

            raise RuntimeAccessError(
                "Record not found or access denied"
            )


        stmt = (

            update(table)

            .where(

                table.c.id == record_id

            )

        )


        stmt = self.apply_scope_condition(

            table,

            stmt,

            user_context,

            data_scope,

        )


        stmt = stmt.values(
            **values
        )


        self.db.execute(stmt)

        self.db.commit()


        module_name = module_code.upper()


        self.history.add(

            db=self.db,

            module=module_name,

            record_id=record_id,

            action="UPDATE",

            user=user,

            changes={

                "old": old_data,

                "new": values,

            }

        )


        self.audit.create_log(

            db=self.db,

            action="UPDATE",

            module=module_name,

            user=user,

            record_id=record_id,

            old_data=old_data,

            new_data=values,

        )





    # ---------------------------------------------------------
    # Soft Delete
    # ---------------------------------------------------------

    def delete(
        self,
        table_name: str,
        module_code: str,
        record_id: int,
        user: str = "system",
        user_context: dict | None = None,
        data_scope: str = "GLOBAL",
    ) -> None:


        table = self.get_table(
            table_name
        )


        old_data = self.get_record(

            table_name,

            record_id,

            user_context,

            data_scope,

        )


        if old_data is None:

            raise RuntimeAccessError(
                "Record not found or access denied"
            )


        stmt = (

            update(table)

            .where(

                table.c.id == record_id

            )

        )


        stmt = self.apply_scope_condition(

            table,

            stmt,

            user_context,

            data_scope,

        )


        stmt = stmt.values(

            is_active=False,

            version=table.c.version + 1,

        )


        self.db.execute(stmt)

        self.db.commit()





    # ---------------------------------------------------------
    # Restore
    # ---------------------------------------------------------

    def restore(
        self,
        table_name: str,
        module_code: str,
        record_id: int,
        user: str = "system",
        user_context: dict | None = None,
        data_scope: str = "GLOBAL",
    ) -> None:


        table = self.get_table(
            table_name
        )


        old_data = self.get_record(

            table_name,

            record_id,

            user_context,

            data_scope,

        )


        if old_data is None:

            raise RuntimeAccessError(
                "Record not found or access denied"
            )


        stmt = (

            update(table)

            .where(

                table.c.id == record_id

            )

        )


        stmt = self.apply_scope_condition(

            table,

            stmt,

            user_context,

            data_scope,

        )


        stmt = stmt.values(

            is_active=True,

            version=table.c.version + 1,

        )


        self.db.execute(stmt)

        self.db.commit()