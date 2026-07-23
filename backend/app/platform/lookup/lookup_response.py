from __future__ import annotations

from .lookup_item import LookupItem


class LookupResponse:
    """
    Standard lookup response.
    """

    @staticmethod
    def success(rows: list[dict]) -> dict:

        return {
            "success": True,
            "count": len(rows),
            "items": [
                LookupItem.build(row)
                for row in rows
            ],
        }