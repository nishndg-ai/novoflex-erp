from __future__ import annotations

from .exceptions import WorkflowNotFoundError
from .workflow_definition import WorkflowDefinition
from .workflow_engine import WorkflowEngine
from .workflow_history import WorkflowHistory
from .workflow_instance import WorkflowInstance
from .workflow_registry import WorkflowRegistry


class WorkflowService:
    """
    High-level workflow service.

    Coordinates workflow execution and acts as the
    primary entry point for CRUD, Events, APIs,
    and future approval workflows.
    """

    def __init__(self):
        self.engine = WorkflowEngine()

    def definition(
        self,
        module_code: str,
    ) -> WorkflowDefinition:

        definition = WorkflowRegistry.get(module_code)

        if definition is None:
            definition = WorkflowRegistry.get("default")

        if definition is None:
            raise WorkflowNotFoundError(
                f"No workflow registered for '{module_code}'."
            )

        return definition

    def start(
        self,
        module_code: str,
        record_id,
        created_by: str,
    ) -> WorkflowInstance:

        definition = self.definition(module_code)

        initial_state = definition.get_initial_state()

        if initial_state is None:
            raise WorkflowNotFoundError(
                "Workflow has no initial state."
            )

        return WorkflowInstance(
            module_code=module_code,
            record_id=record_id,
            current_state=initial_state.code,
            created_by=created_by,
        )

    def execute(
        self,
        instance: WorkflowInstance,
        action: str,
        performed_by: str,
        user_roles: list[str] | None = None,
        comment: str | None = None,
    ) -> WorkflowHistory:

        definition = self.definition(
            instance.module_code
        )

        return self.engine.execute(
            definition=definition,
            instance=instance,
            action=action,
            performed_by=performed_by,
            user_roles=user_roles,
            comment=comment,
        )

    def available_actions(
        self,
        instance: WorkflowInstance,
    ) -> list[str]:

        definition = self.definition(
            instance.module_code
        )

        transitions = definition.get_transitions(
            instance.current_state,
        )

        return [
            transition.action
            for transition in transitions
        ]