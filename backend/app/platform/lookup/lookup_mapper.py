from __future__ import annotations

from .lookup_item import LookupItem


class LookupMapper:
    """
    Maps runtime query results into lookup items.
    """

    @staticmethod
    def map(rows: list[dict]) -> list[dict]:

        return [
            LookupItem.build(row)
            for row in rows
        ]