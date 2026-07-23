from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any

from .approval_mode import ApprovalMode


@dataclass
class ApprovalInstance:
    """
    Runtime approval instance.

    Supports:
    - Sequential approvals
    - Parallel approvals
    - Anyone approvals
    - Majority approvals
    - Unanimous approvals
    """

    module_code: str

    record_id: Any

    approvers: list[str] = field(default_factory=list)

    mode: ApprovalMode = ApprovalMode.SEQUENTIAL

    current_level: int = 1

    approved_by: list[str] = field(default_factory=list)

    rejected_by: list[str] = field(default_factory=list)

    completed: bool = False

    rejected: bool = False

    created_at: datetime = field(default_factory=datetime.utcnow)

    updated_at: datetime = field(default_factory=datetime.utcnow)

    def approve(
        self,
        user: str,
    ) -> None:

        if user not in self.approved_by:
            self.approved_by.append(user)

        self.updated_at = datetime.utcnow()

        total = len(self.approvers)
        approved = len(self.approved_by)

        if self.mode == ApprovalMode.ANYONE:

            self.completed = approved >= 1

        elif self.mode == ApprovalMode.UNANIMOUS:

            self.completed = approved == total

        elif self.mode == ApprovalMode.MAJORITY:

            self.completed = approved > (total // 2)

        elif self.mode == ApprovalMode.PARALLEL:

            self.completed = approved == total

        else:
            # Sequential (first implementation)
            self.completed = approved == total

    def reject(
        self,
        user: str,
    ) -> None:

        if user not in self.rejected_by:
            self.rejected_by.append(user)

        self.rejected = True

        self.updated_at = datetime.utcnow()

    @property
    def pending_approvers(
        self,
    ) -> list[str]:

        return [
            approver
            for approver in self.approvers
            if approver not in self.approved_by
        ]