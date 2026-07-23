from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


@dataclass
class ApprovalHistory:
    """
    Audit record for approval activities.

    Every approval-related action creates one history record.

    Examples

        Purchase Manager Approved

        Plant Head Rejected

        Director Delegated

        SLA Escalated

        Reminder Sent
    """

    module_code: str

    record_id: Any

    approver: str

    action: str

    level: int

    performed_at: datetime = field(
        default_factory=datetime.utcnow
    )

    comment: str | None = None

    metadata: dict[str, Any] = field(
        default_factory=dict
    )