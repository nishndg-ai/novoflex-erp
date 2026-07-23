from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any
from uuid import uuid4


@dataclass
class Notification:
    """
    Represents a notification delivered to a user.
    """

    id: str = field(default_factory=lambda: str(uuid4()))

    recipient: str = ""

    title: str = ""

    message: str = ""

    channel: str = "IN_APP"

    priority: str = "Normal"

    created_at: datetime = field(default_factory=datetime.utcnow)

    read: bool = False

    read_at: datetime | None = None

    metadata: dict[str, Any] = field(default_factory=dict)

    def mark_read(self) -> None:

        self.read = True
        self.read_at = datetime.utcnow()