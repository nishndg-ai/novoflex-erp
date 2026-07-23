from __future__ import annotations

from datetime import datetime

from .delegation import ApprovalDelegation


class DelegationResolver:
    """
    Resolves delegated approvers.

    Future implementation:
    ----------------------
    Delegations will be loaded from the database.

    Current implementation:
    -----------------------
    Uses the supplied delegation list.
    """

    @staticmethod
    def resolve(
        approver: str,
        delegations: list[ApprovalDelegation],
        current: datetime | None = None,
    ) -> str:

        current = current or datetime.utcnow()

        for delegation in delegations:

            if (
                delegation.from_user == approver
                and delegation.is_active(current)
            ):
                return delegation.to_user

        return approver

    @staticmethod
    def resolve_all(
        approvers: list[str],
        delegations: list[ApprovalDelegation],
        current: datetime | None = None,
    ) -> list[str]:

        return [
            DelegationResolver.resolve(
                approver=user,
                delegations=delegations,
                current=current,
            )
            for user in approvers
        ]