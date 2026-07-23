from __future__ import annotations

from typing import Any

from .approval_task import ApprovalTask


class ApprovalInbox:
    """
    Central approval inbox.

    Stores pending approval tasks.

    Current implementation:
        In-memory

    Future implementation:
        Database-backed
    """

    def __init__(self):
        self._tasks: list[ApprovalTask] = []

    def add(
        self,
        task: ApprovalTask,
    ) -> None:

        self._tasks.append(task)

    def remove(
        self,
        task: ApprovalTask,
    ) -> None:

        if task in self._tasks:
            self._tasks.remove(task)

    def complete(
        self,
        module_code: str,
        record_id: Any,
        approver: str,
        comment: str | None = None,
    ) -> ApprovalTask | None:

        for task in self._tasks:

            if (
                task.module_code == module_code
                and task.record_id == record_id
                and task.approver == approver
                and not task.completed
            ):

                task.complete(comment)

                return task

        return None

    def pending_for_user(
        self,
        user: str,
    ) -> list[ApprovalTask]:

        return [
            task
            for task in self._tasks
            if (
                task.approver == user
                and not task.completed
            )
        ]

    def pending(
        self,
    ) -> list[ApprovalTask]:

        return [
            task
            for task in self._tasks
            if not task.completed
        ]

    def all(
        self,
    ) -> list[ApprovalTask]:

        return list(self._tasks)

    def clear(
        self,
    ) -> None:

        self._tasks.clear()