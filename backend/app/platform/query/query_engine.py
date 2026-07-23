from __future__ import annotations

from typing import Any

from sqlalchemy import Select, select

from .filter_builder import FilterBuilder
from .search_builder import SearchBuilder
from .sort_builder import SortBuilder


class QueryEngine:
    """
    Generic SQLAlchemy query builder.
    """

    @staticmethod
    def build_select(
        table,
        *,
        filters: dict[str, Any] | None = None,
        search: str | None = None,
        limit: int = 100,
        offset: int = 0,
        order_by: str | None = None,
        descending: bool = False,
    ) -> Select:

        stmt = select(table)

        filter_clause = FilterBuilder.build(table, filters)
        if filter_clause is not None:
            stmt = stmt.where(filter_clause)

        search_clause = SearchBuilder.build(table, search)
        if search_clause is not None:
            stmt = stmt.where(search_clause)

        sort_clause = SortBuilder.build(
            table,
            order_by=order_by,
            descending=descending,
        )
        if sort_clause is not None:
            stmt = stmt.order_by(sort_clause)

        stmt = stmt.offset(offset).limit(limit)

        return stmt