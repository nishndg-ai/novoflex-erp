from __future__ import annotations

from typing import Any

from app.platform.crud.module_hooks import get_hooks
from app.platform.crud.validator import RuntimeValidator
from app.platform.runtime.runtime_data_engine import RuntimeDataEngine
from app.platform.runtime.types import RuntimeDefinition


class CrudService:
    """
    Generic CRUD service for runtime modules.
    """

    def __init__(self, data_engine: RuntimeDataEngine):
        self.data_engine = data_engine
        self.validator = RuntimeValidator()

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
    ):

        return self.data_engine.get_records(
            table_name=runtime.module.table_name,
            filters=filters,
            search=search,
            limit=limit,
            offset=offset,
            order_by=order_by,
            descending=descending,
        )

    def get(
        self,
        runtime: RuntimeDefinition,
        record_id: int,
    ):

        return self.data_engine.get_record(
            runtime.module.table_name,
            record_id,
        )

    def create(
        self,
        runtime: RuntimeDefinition,
        values: dict[str, Any],
    ):

        hooks = get_hooks(runtime.module.module_code)

        values = hooks.before_create(values)

        self.validator.validate(runtime.fields, values)

        record_id = self.data_engine.insert(
            runtime.module.table_name,
            values,
        )

        hooks.after_create(record_id, values)

        return record_id

    def update(
        self,
        runtime: RuntimeDefinition,
        record_id: int,
        values: dict[str, Any],
    ):

        hooks = get_hooks(runtime.module.module_code)

        values = hooks.before_update(
            record_id,
            values,
        )

        self.validator.validate(runtime.fields, values)

        self.data_engine.update(
            runtime.module.table_name,
            record_id,
            values,
        )

        hooks.after_update(
            record_id,
            values,
        )

    def delete(
        self,
        runtime: RuntimeDefinition,
        record_id: int,
    ):

        hooks = get_hooks(runtime.module.module_code)

        hooks.before_delete(record_id)

        self.data_engine.delete(
            runtime.module.table_name,
            record_id,
        )

        hooks.after_delete(record_id)