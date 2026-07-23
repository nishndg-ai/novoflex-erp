from __future__ import annotations

from .workflow_transition import WorkflowTransition


class WorkflowAuthorization:
    """
    Handles authorization for workflow transitions.

    Initially supports role-based authorization.

    Future enhancements:
    - User permissions
    - Dynamic expressions
    - Department-based approvals
    - Plant-based approvals
    - Amount-based approvals
    """

    @staticmethod
    def can_execute(
        transition: WorkflowTransition,
        user_roles: list[str],
    ) -> bool:

        if not transition.roles:
            return True

        return any(
            role in transition.roles
            for role in user_roles
        )