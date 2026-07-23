from __future__ import annotations

from typing import Any

from app.platform.runtime.runtime_data_engine import RuntimeDataEngine
from app.platform.runtime.types import RuntimeDefinition


class CrudEngine:
    """
    Generic metadata-driven CRUD engine.

    This engine never knows about Company, Plant, Supplier,
    Employee, etc.

    It only works with RuntimeDefinition.
    """

    def __init__(self, data_engine: RuntimeDataEngine):
        self.data_engine = data_engine

    # ---------------------------------------------------------
    # List
    # ---------------------------------------------------------

    def list(
        self,
        runtime: RuntimeDefinition,
        limit: int = 100,
        offset: int = 0,
    ) -> list[dict[str, Any]]:

        return self.data_engine.get_records(
            table_name=runtime.module.table_name,
            limit=limit,
            offset=offset,
        )

    # ---------------------------------------------------------
    # Get
    # ---------------------------------------------------------

    def get(
        self,
        runtime: RuntimeDefinition,
        record_id: int,
    ) -> dict[str, Any] | None:

        return self.data_engine.get_record(
            table_name=runtime.module.table_name,
            record_id=record_id,
        )

    # ---------------------------------------------------------
    # Create
    # ---------------------------------------------------------

    def create(
        self,
        runtime: RuntimeDefinition,
        values: dict[str, Any],
    ) -> int:

        return self.data_engine.insert(
            table_name=runtime.module.table_name,
            values=values,
        )

    # ---------------------------------------------------------
    # Update
    # ---------------------------------------------------------

    def update(
        self,
        runtime: RuntimeDefinition,
        record_id: int,
        values: dict[str, Any],
    ) -> None:

        self.data_engine.update(
            table_name=runtime.module.table_name,
            record_id=record_id,
            values=values,
        )

    # ---------------------------------------------------------
    # Delete
    # ---------------------------------------------------------

    def delete(
        self,
        runtime: RuntimeDefinition,
        record_id: int,
    ) -> None:

        self.data_engine.delete(
            table_name=runtime.module.table_name,
            record_id=record_id,
        )