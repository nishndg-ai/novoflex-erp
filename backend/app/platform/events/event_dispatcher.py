from __future__ import annotations

from collections import defaultdict

from .event import Event
from .event_handler import EventHandler
from .event_types import EventType


class EventDispatcher:
    """
    Central event dispatcher.
    """

    def __init__(self):
        self._handlers: dict[
            EventType,
            list[EventHandler],
        ] = defaultdict(list)

    def register(
        self,
        event_type: EventType,
        handler: EventHandler,
    ):

        self._handlers[event_type].append(handler)

    def dispatch(
        self,
        event: Event,
    ) -> Event:

        handlers = self._handlers.get(
            event.event_type,
            [],
        )

        for handler in handlers:

            if event.cancelled:
                break

            handler.handle(event)

        return event

    def clear(self):

        self._handlers.clear()