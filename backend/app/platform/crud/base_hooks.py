from __future__ import annotations

from .hooks import CrudHooks


class BaseCrudHooks(CrudHooks):
    """
    Default implementation for CRUD hooks.

    ERP modules can inherit this class and override only the hooks they need.
    """

    pass