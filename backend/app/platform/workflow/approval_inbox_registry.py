from __future__ import annotations

from .approval_inbox import ApprovalInbox


class ApprovalInboxRegistry:
    """
    Global Approval Inbox.

    Provides a singleton inbox for the ERP.

    Future implementation:
        Database-backed inbox service.
    """

    _inbox = ApprovalInbox()

    @classmethod
    def inbox(
        cls,
    ) -> ApprovalInbox:

        return cls._inbox

    @classmethod
    def clear(
        cls,
    ) -> None:

        cls._inbox.clear()