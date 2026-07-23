from __future__ import annotations

from app.platform.events import Event, EventRegistry, EventType

from .authorization import WorkflowAuthorization
from .condition_engine import WorkflowConditionEngine
from .exceptions import (
    InvalidWorkflowTransitionError,
    WorkflowAuthorizationError,
    WorkflowCommentRequiredError,
)
from .workflow_definition import WorkflowDefinition
from .workflow_history import WorkflowHistory
from .workflow_instance import WorkflowInstance


class WorkflowEngine:
    """
    Enterprise workflow execution engine.

    Responsibilities
    ----------------
    • Transition validation
    • Role authorization
    • Condition evaluation
    • Event publishing
    • State changes
    • History generation
    """

    def execute(
        self,
        definition: WorkflowDefinition,
        instance: WorkflowInstance,
        action: str,
        performed_by: str,
        user_roles: list[str] | None = None,
        context: dict | None = None,
        comment: str | None = None,
    ) -> WorkflowHistory:

        user_roles = user_roles or []
        context = context or {}

        transition = definition.get_transition(
            instance.current_state,
            action,
        )

        if transition is None:
            raise InvalidWorkflowTransitionError(
                f"'{action}' is not allowed from "
                f"'{instance.current_state}'."
            )

        if not WorkflowAuthorization.can_execute(
            transition,
            user_roles,
        ):
            raise WorkflowAuthorizationError(
                f"User is not authorized to execute "
                f"'{action}'."
            )

        for condition in transition.conditions:

            if not WorkflowConditionEngine.evaluate(
                condition,
                context,
            ):
                raise InvalidWorkflowTransitionError(
                    "Workflow transition condition failed."
                )

        if (
            transition.requires_comment
            and not comment
        ):
            raise WorkflowCommentRequiredError(
                "A comment is required."
            )

        before_event = Event(
            event_type=EventType.BEFORE_WORKFLOW,
            module_code=instance.module_code,
            payload={
                "instance": instance,
                "transition": transition,
                "context": context,
            },
        )

        EventRegistry.dispatcher().dispatch(
            before_event
        )

        if before_event.cancelled:
            raise InvalidWorkflowTransitionError(
                "Workflow cancelled."
            )

        previous_state = instance.current_state

        EventRegistry.dispatcher().dispatch(
            Event(
                event_type=EventType.BEFORE_STATE_CHANGE,
                module_code=instance.module_code,
                payload={
                    "instance": instance,
                    "from_state": previous_state,
                    "to_state": transition.to_state,
                },
            )
        )

        instance.move_to(
            transition.to_state,
        )

        history = WorkflowHistory(
            module_code=instance.module_code,
            record_id=instance.record_id,
            from_state=previous_state,
            to_state=transition.to_state,
            action=transition.action,
            performed_by=performed_by,
            comment=comment,
        )

        EventRegistry.dispatcher().dispatch(
            Event(
                event_type=EventType.AFTER_STATE_CHANGE,
                module_code=instance.module_code,
                payload={
                    "history": history,
                    "instance": instance,
                },
            )
        )

        EventRegistry.dispatcher().dispatch(
            Event(
                event_type=EventType.AFTER_WORKFLOW,
                module_code=instance.module_code,
                payload={
                    "history": history,
                    "instance": instance,
                },
                result=history,
            )
        )

        return history