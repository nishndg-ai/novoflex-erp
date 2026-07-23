from __future__ import annotations

from .event_dispatcher import EventDispatcher


class EventRegistry:
    """
    Global platform event registry.
    """

    _dispatcher = EventDispatcher()

    @classmethod
    def dispatcher(cls) -> EventDispatcher:
        return cls._dispatcher