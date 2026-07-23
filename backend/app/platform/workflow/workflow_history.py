from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


@dataclass
class WorkflowHistory:
    """
    Represents one workflow transition.

    Example:

        Draft --Submit--> Submitted

    Every workflow movement creates one history record.
    """

    module_code: str

    record_id: Any

    from_state: str

    to_state: str

    action: str

    performed_by: str

    performed_at: datetime = field(default_factory=datetime.utcnow)

    comment: str | None = None

    metadata: dict[str, Any] = field(default_factory=dict)