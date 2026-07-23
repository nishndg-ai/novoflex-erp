from __future__ import annotations

# Importing this module registers all CRUD hooks.
from . import module_audit_hooks


def initialize_crud() -> None:
    """
    Initialize the CRUD platform.
    """
    _ = module_audit_hooks