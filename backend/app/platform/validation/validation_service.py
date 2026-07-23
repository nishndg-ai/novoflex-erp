from __future__ import annotations

from app.platform.events import Event, EventRegistry, EventType
from app.platform.runtime.runtime_engine import RuntimeEngine

from .validation_engine import ValidationEngine


class ValidationService:
    """
    Runtime validation service with lifecycle events.
    """

    def __init__(
        self,
        runtime_engine: RuntimeEngine,
    ):
        self.runtime_engine = runtime_engine
        self.validation_engine = ValidationEngine()

    def validate(
        self,
        module_code: str,
        values: dict,
    ) -> dict:

        runtime = self.runtime_engine.build_runtime(
            module_code
        )

        before_event = Event(
            event_type=EventType.BEFORE_VALIDATE,
            module_code=module_code,
            payload=values,
        )

        EventRegistry.dispatcher().dispatch(
            before_event
        )

        if before_event.cancelled:
            raise Exception("Validation cancelled.")

        validated = self.validation_engine.validate(
            runtime,
            before_event.payload,
        )

        after_event = Event(
            event_type=EventType.AFTER_VALIDATE,
            module_code=module_code,
            payload=validated,
            result=validated,
        )

        EventRegistry.dispatcher().dispatch(
            after_event
        )

        return after_event.result