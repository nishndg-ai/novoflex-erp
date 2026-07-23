from __future__ import annotations

from math import ceil
from typing import Any


class Pagination:

    @staticmethod
    def build(
        *,
        total: int,
        limit: int,
        offset: int,
    ) -> dict[str, Any]:

        if limit <= 0:
            limit = 1

        page = (offset // limit) + 1

        return {
            "page": page,
            "page_size": limit,
            "offset": offset,
            "total_records": total,
            "total_pages": ceil(total / limit),
            "has_next": page < ceil(total / limit),
            "has_previous": page > 1,
        }