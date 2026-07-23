from __future__ import annotations

from typing import Type

from .base_hooks import BaseCrudHooks


class CrudRegistry:
    """
    Registers module-specific CRUD hook classes.
    """

    def __init__(self):
        self._hooks: dict[str, Type[BaseCrudHooks]] = {}

    def register(
        self,
        module_code: str,
        hooks: Type[BaseCrudHooks],
    ) -> None:
        self._hooks[module_code] = hooks

    def get(
        self,
        module_code: str,
    ) -> BaseCrudHooks:

        hook_class = self._hooks.get(
            module_code,
            BaseCrudHooks,
        )

        return hook_class()