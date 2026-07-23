from __future__ import annotations

from .approver import WorkflowApprover
from .delegation import ApprovalDelegation
from .delegation_resolver import DelegationResolver


class WorkflowApproverResolver:
    """
    Resolves workflow approvers.

    Supports
    --------
    - User
    - Role
    - Delegation

    Future
    ------
    - Reporting Manager
    - Department Head
    - Plant Head
    - Cost Center Head
    - Dynamic SQL
    - Plugin Resolvers
    """

    def resolve(
        self,
        approvers: list[WorkflowApprover],
        context: dict,
        delegations: list[ApprovalDelegation] | None = None,
    ) -> list[str]:

        delegations = delegations or []

        resolved: list[str] = []

        role_users = context.get(
            "role_users",
            {},
        )

        for approver in sorted(
            approvers,
            key=lambda a: a.sequence,
        ):

            if approver.approver_type == "user":

                resolved.append(
                    DelegationResolver.resolve(
                        approver.value,
                        delegations,
                    )
                )

            elif approver.approver_type == "role":

                users = role_users.get(
                    approver.value,
                    [],
                )

                users = DelegationResolver.resolve_all(
                    users,
                    delegations,
                )

                resolved.extend(users)

        # Remove duplicates while preserving order
        return list(dict.fromkeys(resolved))