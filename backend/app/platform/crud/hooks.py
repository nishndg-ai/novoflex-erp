from __future__ import annotations

from typing import Any


class CrudHooks:
    """
    Lifecycle hooks for runtime CRUD operations.
    """

    def before_create(
        self,
        values: dict[str, Any],
    ) -> dict[str, Any]:
        return values

    def after_create(
        self,
        record_id: int,
        values: dict[str, Any],
    ) -> None:
        pass

    def before_update(
        self,
        record_id: int,
        values: dict[str, Any],
    ) -> dict[str, Any]:
        return values

    def after_update(
        self,
        record_id: int,
        values: dict[str, Any],
    ) -> None:
        pass

    def before_delete(
        self,
        record_id: int,
    ) -> None:
        pass

    def after_delete(
        self,
        record_id: int,
    ) -> None:
        pass