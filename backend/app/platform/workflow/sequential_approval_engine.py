from __future__ import annotations

from .approval_instance import ApprovalInstance


class SequentialApprovalEngine:
    """
    Sequential approval execution.

    Example

        Level 1
            Purchase Manager

        Level 2
            Plant Head

        Level 3
            Director

    Only the current approver is allowed to approve.
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

        if instance.current_level > len(instance.approvers):
            return False

        current_approver = instance.approvers[
            instance.current_level - 1
        ]

        return current_approver == user

    @staticmethod
    def approve(
        instance: ApprovalInstance,
        user: str,
    ) -> None:

        if not SequentialApprovalEngine.can_approve(
            instance,
            user,
        ):
            raise PermissionError(
                "User is not the current approver."
            )

        instance.approved_by.append(user)

        instance.current_level += 1

        if (
            instance.current_level
            > len(instance.approvers)
        ):
            instance.completed = True