from __future__ import annotations

from typing import Any

from app.platform.runtime.runtime_data_engine import RuntimeDataEngine
from app.platform.runtime.types import RuntimeDefinition


class LookupEngine:
    """
    Generic lookup engine for dropdowns, autocomplete,
    reference fields and foreign key selections.
    """

    def __init__(self, data_engine: RuntimeDataEngine):
        self.data_engine = data_engine

    def get_lookup(
        self,
        runtime: RuntimeDefinition,
        *,
        search: str | None = None,
        limit: int = 25,
    ) -> dict[str, Any]:

        return self.data_engine.get_records(
            table_name=runtime.module.table_name,
            search=search,
            limit=limit,
            order_by="id",
        )