from __future__ import annotations

from dataclasses import dataclass, field

from .workflow_state import WorkflowState
from .workflow_transition import WorkflowTransition


@dataclass
class WorkflowDefinition:
    """
    Complete workflow definition.

    A workflow consists of:
    - States
    - Allowed transitions

    Example:

        Draft
           │
           ▼
        Submitted
          ├────────► Rejected
          ▼
        Approved
          ▼
        Closed
    """

    module_code: str

    states: list[WorkflowState] = field(default_factory=list)

    transitions: list[WorkflowTransition] = field(default_factory=list)

    def get_state(
        self,
        code: str,
    ) -> WorkflowState | None:

        for state in self.states:
            if state.code == code:
                return state

        return None

    def get_initial_state(
        self,
    ) -> WorkflowState | None:

        for state in self.states:
            if state.is_initial:
                return state

        return None

    def get_transitions(
        self,
        state_code: str,
    ) -> list[WorkflowTransition]:

        return [
            transition
            for transition in self.transitions
            if transition.from_state == state_code
        ]

    def get_transition(
        self,
        from_state: str,
        action: str,
    ) -> WorkflowTransition | None:

        for transition in self.transitions:

            if (
                transition.from_state == from_state
                and transition.action == action
            ):
                return transition

        return None