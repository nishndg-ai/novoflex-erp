from __future__ import annotations

from typing import Any


class AuditService:
    """
    Base audit service.

    Replace the methods with database persistence later.
    """

    def log_create(
        self,
        module_code: str,
        record_id: int,
        values: dict[str, Any],
    ) -> None:
        pass

    def log_update(
        self,
        module_code: str,
        record_id: int,
        values: dict[str, Any],
    ) -> None:
        pass

    def log_delete(
        self,
        module_code: str,
        record_id: int,
    ) -> None:
        pass