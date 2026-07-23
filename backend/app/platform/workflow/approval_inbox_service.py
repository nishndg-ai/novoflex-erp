from __future__ import annotations

from typing import Any

from .approval_inbox_registry import ApprovalInboxRegistry
from .approval_task import ApprovalTask


class ApprovalInboxService:
    """
    Service layer for Approval Inbox.
    """

    def __init__(self):
        self.inbox = ApprovalInboxRegistry.inbox()

    def create_task(
        self,
        module_code: str,
        record_id: Any,
        approver: str,
        workflow_state: str,
        action: str,
        priority: str = "Normal",
        due_date=None,
        metadata: dict | None = None,
    ) -> ApprovalTask:

        task = ApprovalTask(
            module_code=module_code,
            record_id=record_id,
            approver=approver,
            workflow_state=workflow_state,
            action=action,
            priority=priority,
            due_date=due_date,
            metadata=metadata or {},
        )

        self.inbox.add(task)

        return task

    def complete_task(
        self,
        module_code: str,
        record_id: Any,
        approver: str,
        comment: str | None = None,
    ) -> ApprovalTask | None:

        return self.inbox.complete(
            module_code=module_code,
            record_id=record_id,
            approver=approver,
            comment=comment,
        )

    def pending_for_user(
        self,
        user: str,
    ) -> list[ApprovalTask]:

        return self.inbox.pending_for_user(user)

    def pending(
        self,
    ) -> list[ApprovalTask]:

        return self.inbox.pending()

    def all(
        self,
    ) -> list[ApprovalTask]:

        return self.inbox.all()

    def clear(
        self,
    ) -> None:

        self.inbox.clear()