from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass
class ApprovalDelegation:
    """
    Represents approval delegation.

    Example

        Director
            ↓
        Plant Head

    Valid only during the specified period.
    """

    from_user: str

    to_user: str

    start_date: datetime

    end_date: datetime

    active: bool = True

    reason: str | None = None

    def is_active(
        self,
        current: datetime | None = None,
    ) -> bool:

        if not self.active:
            return False

        current = current or datetime.utcnow()

        return (
            self.start_date
            <= current
            <= self.end_date
        )