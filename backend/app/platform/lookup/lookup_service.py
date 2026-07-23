from __future__ import annotations

from app.platform.events import Event, EventRegistry, EventType
from app.platform.runtime.runtime_engine import RuntimeEngine

from .lookup_engine import LookupEngine


class LookupService:
    """
    Runtime lookup service with lifecycle events.
    """

    def __init__(self, db):
        self.db = db
        self.runtime_engine = RuntimeEngine(db)
        self.lookup_engine = LookupEngine(db)

    def get(
        self,
        module_code: str,
        search: str | None = None,
        limit: int = 20,
    ):

        runtime = self.runtime_engine.build_runtime(
            module_code
        )

        before_event = Event(
            event_type=EventType.BEFORE_LOOKUP,
            module_code=module_code,
            payload={
                "search": search,
                "limit": limit,
            },
        )

        EventRegistry.dispatcher().dispatch(
            before_event
        )

        if before_event.cancelled:
            raise Exception("Lookup cancelled.")

        result = self.lookup_engine.lookup(
            runtime=runtime,
            search=before_event.payload["search"],
            limit=before_event.payload["limit"],
        )

        after_event = Event(
            event_type=EventType.AFTER_LOOKUP,
            module_code=module_code,
            payload=before_event.payload,
            result=result,
        )

        EventRegistry.dispatcher().dispatch(
            after_event
        )

        return after_event.result