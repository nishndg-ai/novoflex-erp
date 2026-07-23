from __future__ import annotations

from sqlalchemy import asc, desc


class SortBuilder:
    """
    Builds SQLAlchemy ORDER BY clauses.
    """

    @staticmethod
    def build(
        table,
        order_by: str | None = None,
        descending: bool = False,
    ):

        if not order_by:
            return None

        if not hasattr(table.c, order_by):
            return None

        column = getattr(table.c, order_by)

        if descending:
            return desc(column)

        return asc(column)