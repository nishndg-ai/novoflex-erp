from __future__ import annotations

from typing import Any

from app.platform.crud.module_hooks import get_hooks
from app.platform.crud.validator import RuntimeValidator

from app.platform.runtime.runtime_data_engine import (
    RuntimeDataEngine,
)

from app.platform.runtime.types import (
    RuntimeDefinition,
)



class CrudService:
    """
    Generic CRUD service for runtime modules.
    """

    def __init__(
        self,
        data_engine: RuntimeDataEngine,
    ):

        self.data_engine = data_engine

        self.validator = RuntimeValidator()



    # ---------------------------------------------------------
    # LIST
    # ---------------------------------------------------------

    def list(
        self,
        runtime: RuntimeDefinition,
        *,
        filters: dict[str, Any] | None = None,
        search: str | None = None,
        limit: int = 100,
        offset: int = 0,
        order_by: str | None = None,
        descending: bool = False,
        include_deleted: bool = False,
    ):

        return self.data_engine.get_records(

            table_name=runtime.module.table_name,

            filters=filters,

            search=search,

            limit=limit,

            offset=offset,

            order_by=order_by,

            descending=descending,

            include_deleted=include_deleted,

        )



    # ---------------------------------------------------------
    # GET
    # ---------------------------------------------------------

    def get(
        self,
        runtime: RuntimeDefinition,
        record_id: int,
    ):

        return self.data_engine.get_record(
            runtime.module.table_name,
            record_id,
        )



    # ---------------------------------------------------------
    # CREATE
    # ---------------------------------------------------------

    def create(
        self,
        runtime: RuntimeDefinition,
        values: dict[str, Any],
        user: str = "admin",
    ):

        hooks = get_hooks(
            runtime.module.module_code
        )


        values = hooks.before_create(
            values
        )


        table = self.data_engine.get_table(
            runtime.module.table_name
        )


        self.validator.validate(
            self.data_engine.db,
            runtime.fields,
            values,
            table,
            is_update=False,
        )


        record_id = self.data_engine.insert(

            table_name=runtime.module.table_name,

            module_code=runtime.module.module_code,

            values=values,

            user=user,

        )


        hooks.after_create(
            record_id,
            values,
        )


        return record_id



    # ---------------------------------------------------------
    # UPDATE
    # ---------------------------------------------------------

    def update(
        self,
        runtime: RuntimeDefinition,
        record_id: int,
        values: dict[str, Any],
        user: str = "admin",
    ):

        hooks = get_hooks(
            runtime.module.module_code
        )


        values = hooks.before_update(
            record_id,
            values,
        )


        table = self.data_engine.get_table(
            runtime.module.table_name
        )


        validation_values = values.copy()

        validation_values["id"] = record_id


        self.validator.validate(
            self.data_engine.db,
            runtime.fields,
            validation_values,
            table,
            is_update=True,
        )


        clean_values = values.copy()

        clean_values.pop(
            "id",
            None,
        )


        self.data_engine.update(

            table_name=runtime.module.table_name,

            module_code=runtime.module.module_code,

            record_id=record_id,

            values=clean_values,

            user=user,

        )


        hooks.after_update(
            record_id,
            clean_values,
        )


    # ---------------------------------------------------------
    # RESTORE
    # ---------------------------------------------------------

    def restore(
        self,
        runtime: RuntimeDefinition,
        record_id: int,
        user: str = "admin",
    ):

        self.data_engine.restore(

            table_name=runtime.module.table_name,

            module_code=runtime.module.module_code,

            record_id=record_id,

            user=user,

        )
        

    # ---------------------------------------------------------
    # DELETE
    # ---------------------------------------------------------

    def delete(
        self,
        runtime: RuntimeDefinition,
        record_id: int,
        user: str = "admin",
    ):

        hooks = get_hooks(
            runtime.module.module_code
        )


        hooks.before_delete(
            record_id
        )


        self.data_engine.delete(

            table_name=runtime.module.table_name,

            module_code=runtime.module.module_code,

            record_id=record_id,

            user=user,

        )


        hooks.after_delete(
            record_id
        )