from __future__ import annotations

from sqlalchemy import or_


class SearchBuilder:
    """
    Builds SQLAlchemy search conditions for runtime tables.
    """

    @staticmethod
    def build(table, search: str | None):

        if not search:
            return None

        conditions = []

        for column in table.columns:
            try:
                if hasattr(column.type, "length") or column.type.python_type is str:
                    conditions.append(column.ilike(f"%{search}%"))
            except Exception:
                continue

        if not conditions:
            return None

        return or_(*conditions)