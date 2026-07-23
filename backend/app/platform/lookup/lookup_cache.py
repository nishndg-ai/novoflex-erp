from __future__ import annotations

from typing import Any


class LookupCache:
    """
    Simple in-memory lookup cache.
    Replace with Redis later.
    """

    def __init__(self):
        self._cache: dict[str, Any] = {}

    def get(self, key: str):

        return self._cache.get(key)

    def set(
        self,
        key: str,
        value: Any,
    ) -> None:

        self._cache[key] = value

    def clear(self) -> None:

        self._cache.clear()