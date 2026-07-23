from __future__ import annotations

from app.platform.events import Event, EventRegistry, EventType
from app.platform.runtime.runtime_engine import RuntimeEngine

from .query_engine import QueryEngine


class QueryService:
    """
    Runtime query service with lifecycle events.
    """

    def __init__(self, db):
        self.db = db
        self.runtime_engine = RuntimeEngine(db)
        self.query_engine = QueryEngine(db)

    def list(
        self,
        module_code: str,
        request,
    ):

        runtime = self.runtime_engine.build_runtime(
            module_code
        )

        before_event = Event(
            event_type=EventType.BEFORE_QUERY,
            module_code=module_code,
            payload={
                "request": request,
            },
        )

        EventRegistry.dispatcher().dispatch(
            before_event
        )

        if before_event.cancelled:
            raise Exception("Query cancelled.")

        result = self.query_engine.execute(
            runtime,
            before_event.payload["request"],
        )

        after_event = Event(
            event_type=EventType.AFTER_QUERY,
            module_code=module_code,
            payload={
                "request": before_event.payload["request"],
            },
            result=result,
        )

        EventRegistry.dispatcher().dispatch(
            after_event
        )

        return after_event.result