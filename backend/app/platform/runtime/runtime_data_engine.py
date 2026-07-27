from __future__ import annotations

from typing import Any

from sqlalchemy import (
    MetaData,
    Table,
    delete,
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



class RuntimeDataEngine:
    """
    Generic Runtime Data Engine.

    Handles dynamic ERP tables
    with automatic audit and history tracking.
    """



    def __init__(self, db: Session):

        self.db = db

        self._metadata = MetaData()

        self._tables: dict[str, Table] = {}

        self.query_service = QueryService(db)

        self.audit = AuditEngine()

        self.history = HistoryEngine()



    # ---------------------------------------------------------
    # Table Cache
    # ---------------------------------------------------------

    def get_table(

        self,

        table_name: str

    ) -> Table:


        if table_name not in self._tables:


            self._tables[table_name] = Table(

                table_name,

                self._metadata,

                autoload_with=self.db.bind,

            )


        return self._tables[table_name]





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

    ) -> dict[str, Any]:


        table = self.get_table(table_name)


        return self.query_service.execute(

            table=table,

            filters=filters,

            search=search,

            limit=limit,

            offset=offset,

            order_by=order_by,

            descending=descending,

        )





    # ---------------------------------------------------------
    # Get Record
    # ---------------------------------------------------------

    def get_record(

        self,

        table_name: str,

        record_id: int,

    ) -> dict[str, Any] | None:


        table = self.get_table(table_name)


        stmt = select(table).where(

            table.c.id == record_id

        )


        row = self.db.execute(stmt).first()


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

    ) -> int:


        table = self.get_table(table_name)


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

    ) -> None:


        table = self.get_table(table_name)



        old_data = self.get_record(

            table_name,

            record_id,

        )



        stmt = (

            update(table)

            .where(

                table.c.id == record_id

            )

            .values(**values)

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
    # Delete
    # ---------------------------------------------------------

    def delete(

        self,

        table_name: str,

        module_code: str,

        record_id: int,

        user: str = "system",

    ) -> None:


        table = self.get_table(table_name)



        old_data = self.get_record(

            table_name,

            record_id,

        )



        stmt = (

            delete(table)

            .where(

                table.c.id == record_id

            )

        )


        self.db.execute(stmt)

        self.db.commit()



        module_name = module_code.upper()



        self.history.add(

            db=self.db,

            module=module_name,

            record_id=record_id,

            action="DELETE",

            user=user,

            changes={

                "old": old_data

            }

        )



        self.audit.create_log(

            db=self.db,

            action="DELETE",

            module=module_name,

            user=user,

            record_id=record_id,

            old_data=old_data,

        )