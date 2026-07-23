from __future__ import annotations

from .approval_matrix import ApprovalMatrix
from .approver_resolver import WorkflowApproverResolver


class ApprovalEngine:
    """
    Enterprise approval engine.

    Responsibilities
    ----------------
    - Evaluate approval matrix
    - Resolve approvers
    - Return ordered approval chain

    Future enhancements
    -------------------
    - Parallel approvals
    - Sequential approvals
    - Percentage approvals
    - Majority voting
    - Escalations
    - Delegation
    """

    def __init__(self):
        self.resolver = WorkflowApproverResolver()

    def resolve_approvers(
        self,
        matrix: ApprovalMatrix,
        context: dict,
    ) -> list[str]:

        rule = matrix.find_rule(context)

        if rule is None:
            return []

        return self.resolver.resolve(
            approvers=rule.approvers,
            context=context,
        )