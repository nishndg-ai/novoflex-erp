from __future__ import annotations

from sqlalchemy import Select, func, select


class CountBuilder:
    """
    Builds COUNT(*) queries with runtime filters/search.
    """

    @staticmethod
    def build(
        table,
        *,
        filters=None,
        search=None,
    ) -> Select:

        from .filter_builder import FilterBuilder
        from .search_builder import SearchBuilder

        stmt = select(func.count()).select_from(table)

        filter_clause = FilterBuilder.build(table, filters)
        if filter_clause is not None:
            stmt = stmt.where(filter_clause)

        search_clause = SearchBuilder.build(table, search)
        if search_clause is not None:
            stmt = stmt.where(search_clause)

        return stmt