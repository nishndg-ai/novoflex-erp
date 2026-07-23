from __future__ import annotations

from .registry import CrudRegistry


crud_registry = CrudRegistry()


def register_hooks(
    module_code: str,
    hook_class,
) -> None:
    """
    Register CRUD hooks for a runtime module.
    """
    crud_registry.register(
        module_code,
        hook_class,
    )


def get_hooks(
    module_code: str,
):
    """
    Get CRUD hooks for a runtime module.
    """
    return crud_registry.get(module_code)