from __future__ import annotations

from typing import Any

from sqlalchemy import and_


class FilterBuilder:
    """
    Builds SQLAlchemy WHERE clauses dynamically.
    """

    @staticmethod
    def build(table, filters: dict[str, Any] | None):

        if not filters:
            return None

        conditions = []

        for field, value in filters.items():

            if value is None:
                continue

            if not hasattr(table.c, field):
                continue

            conditions.append(getattr(table.c, field) == value)

        if not conditions:
            return None

        return and_(*conditions)