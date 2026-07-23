from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


@dataclass
class WorkflowInstance:
    """
    Represents a workflow instance attached to a business record.

    Example:

        Module : Purchase Order
        Record : PO0000123
        State  : Submitted
    """

    module_code: str

    record_id: Any

    current_state: str

    created_by: str | None = None

    created_at: datetime = field(default_factory=datetime.utcnow)

    updated_at: datetime = field(default_factory=datetime.utcnow)

    version: int = 1

    context: dict[str, Any] = field(default_factory=dict)

    def move_to(
        self,
        state: str,
    ) -> None:

        self.current_state = state
        self.updated_at = datetime.utcnow()
        self.version += 1