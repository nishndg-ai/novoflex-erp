from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


@dataclass
class ApprovalTask:
    """
    Represents a pending approval task.

    One task corresponds to one approver's action
    on one business record.
    """

    module_code: str

    record_id: Any

    approver: str

    workflow_state: str

    action: str

    assigned_at: datetime = field(
        default_factory=datetime.utcnow
    )

    due_date: datetime | None = None

    priority: str = "Normal"

    completed: bool = False

    completed_at: datetime | None = None

    comment: str | None = None

    metadata: dict[str, Any] = field(
        default_factory=dict
    )

    def complete(
        self,
        comment: str | None = None,
    ) -> None:

        self.completed = True

        self.completed_at = datetime.utcnow()

        self.comment = comment