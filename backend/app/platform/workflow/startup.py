from __future__ import annotations

from .workflow_definition import WorkflowDefinition
from .workflow_registry import WorkflowRegistry
from .workflow_state import WorkflowState
from .workflow_transition import WorkflowTransition


def initialize_workflows() -> None:
    """
    Register built-in workflow definitions.

    Future implementation:
    ----------------------
    Load workflow definitions dynamically from metadata/database.
    """

    WorkflowRegistry.clear()

    default_workflow = WorkflowDefinition(
        module_code="default",
        states=[
            WorkflowState(
                code="draft",
                name="Draft",
                is_initial=True,
            ),
            WorkflowState(
                code="submitted",
                name="Submitted",
            ),
            WorkflowState(
                code="approved",
                name="Approved",
            ),
            WorkflowState(
                code="rejected",
                name="Rejected",
            ),
            WorkflowState(
                code="closed",
                name="Closed",
                is_final=True,
            ),
        ],
        transitions=[
            WorkflowTransition(
                code="submit",
                from_state="draft",
                to_state="submitted",
                action="Submit",
            ),
            WorkflowTransition(
                code="approve",
                from_state="submitted",
                to_state="approved",
                action="Approve",
            ),
            WorkflowTransition(
                code="reject",
                from_state="submitted",
                to_state="rejected",
                action="Reject",
                requires_comment=True,
            ),
            WorkflowTransition(
                code="close",
                from_state="approved",
                to_state="closed",
                action="Close",
            ),
        ],
    )

    WorkflowRegistry.register(default_workflow)