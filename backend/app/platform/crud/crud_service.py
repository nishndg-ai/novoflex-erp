from __future__ import annotations

from app.platform.events import Event, EventRegistry, EventType
from app.platform.runtime.runtime_engine import RuntimeEngine

from .crud_engine import CrudEngine


class CrudService:
    """
    Runtime CRUD service with lifecycle hooks and events.
    """

    def __init__(self, db):
        self.db = db
        self.runtime_engine = RuntimeEngine(db)
        self.crud_engine = CrudEngine(db)

    def create(
        self,
        module_code: str,
        values: dict,
    ):

        runtime = self.runtime_engine.build_runtime(module_code)

        before_event = Event(
            event_type=EventType.BEFORE_CREATE,
            module_code=module_code,
            payload=values,
        )

        EventRegistry.dispatcher().dispatch(before_event)

        if before_event.cancelled:
            raise Exception("Create operation cancelled.")

        result = self.crud_engine.create(
            runtime,
            before_event.payload,
        )

        after_event = Event(
            event_type=EventType.AFTER_CREATE,
            module_code=module_code,
            payload=before_event.payload,
            result=result,
        )

        EventRegistry.dispatcher().dispatch(after_event)

        return result

    def update(
        self,
        module_code: str,
        record_id,
        values: dict,
    ):

        runtime = self.runtime_engine.build_runtime(module_code)

        before_event = Event(
            event_type=EventType.BEFORE_UPDATE,
            module_code=module_code,
            payload=values,
        )

        EventRegistry.dispatcher().dispatch(before_event)

        if before_event.cancelled:
            raise Exception("Update operation cancelled.")

        result = self.crud_engine.update(
            runtime,
            record_id,
            before_event.payload,
        )

        after_event = Event(
            event_type=EventType.AFTER_UPDATE,
            module_code=module_code,
            payload=before_event.payload,
            result=result,
        )

        EventRegistry.dispatcher().dispatch(after_event)

        return result

    def delete(
        self,
        module_code: str,
        record_id,
    ):

        runtime = self.runtime_engine.build_runtime(module_code)

        before_event = Event(
            event_type=EventType.BEFORE_DELETE,
            module_code=module_code,
            payload={"id": record_id},
        )

        EventRegistry.dispatcher().dispatch(before_event)

        if before_event.cancelled:
            raise Exception("Delete operation cancelled.")

        result = self.crud_engine.delete(
            runtime,
            record_id,
        )

        after_event = Event(
            event_type=EventType.AFTER_DELETE,
            module_code=module_code,
            payload={"id": record_id},
            result=result,
        )

        EventRegistry.dispatcher().dispatch(after_event)

        return result