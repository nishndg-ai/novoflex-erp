from __future__ import annotations

from typing import Any

from .audit_service import AuditService
from .base_hooks import BaseCrudHooks


class AuditCrudHooks(BaseCrudHooks):
    """
    Default audit hooks.

    Every ERP module can inherit this class to automatically
    log CRUD operations.
    """

    def __init__(self) -> None:
        self.audit = AuditService()
        self.module_code = "UNKNOWN"

    def after_create(
        self,
        record_id: int,
        values: dict[str, Any],
    ) -> None:

        self.audit.log_create(
            self.module_code,
            record_id,
            values,
        )

    def after_update(
        self,
        record_id: int,
        values: dict[str, Any],
    ) -> None:

        self.audit.log_update(
            self.module_code,
            record_id,
            values,
        )

    def after_delete(
        self,
        record_id: int,
    ) -> None:

        self.audit.log_delete(
            self.module_code,
            record_id,
        )