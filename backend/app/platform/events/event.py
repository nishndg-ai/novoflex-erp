from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .event_types import EventType


@dataclass
class Event:
    """
    Generic platform event.
    """

    event_type: EventType
    module_code: str

    payload: dict[str, Any] = field(default_factory=dict)

    context: dict[str, Any] = field(default_factory=dict)

    cancelled: bool = False

    result: Any = None

    def cancel(self):
        self.cancelled = True