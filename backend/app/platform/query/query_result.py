from __future__ import annotations

from typing import Any

from .pagination import Pagination


class QueryResult:
    """
    Standard query response for runtime data.
    """

    @staticmethod
    def build(
        *,
        rows: list[dict[str, Any]],
        total: int,
        limit: int,
        offset: int,
    ) -> dict[str, Any]:

        return {
            "data": rows,
            "pagination": Pagination.build(
                total=total,
                limit=limit,
                offset=offset,
            ),
        }