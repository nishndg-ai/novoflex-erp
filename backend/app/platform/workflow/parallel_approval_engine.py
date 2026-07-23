from __future__ import annotations

from .approval_instance import ApprovalInstance
from .approval_mode import ApprovalMode


class ParallelApprovalEngine:
    """
    Executes parallel approval strategies.

    Supported modes

    - PARALLEL
    - ANYONE
    - MAJORITY
    - UNANIMOUS
    """

    @staticmethod
    def can_approve(
        instance: ApprovalInstance,
        user: str,
    ) -> bool:

        if instance.completed:
            return False

        if instance.rejected:
            return False

        return user in instance.approvers

    @staticmethod
    def approve(
        instance: ApprovalInstance,
        user: str,
    ) -> None:

        if not ParallelApprovalEngine.can_approve(
            instance,
            user,
        ):
            raise PermissionError(
                "User is not an approver."
            )

        if user not in instance.approved_by:
            instance.approved_by.append(user)

        total = len(instance.approvers)
        approved = len(instance.approved_by)

        if instance.mode == ApprovalMode.ANYONE:

            instance.completed = approved >= 1

        elif instance.mode == ApprovalMode.MAJORITY:

            instance.completed = approved > (
                total // 2
            )

        elif instance.mode == ApprovalMode.UNANIMOUS:

            instance.completed = approved == total

        else:
            # PARALLEL
            instance.completed = approved == total