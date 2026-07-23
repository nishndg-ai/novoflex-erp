from __future__ import annotations

from .notification import Notification
from .notification_provider import NotificationProvider


class EmailNotificationProvider(NotificationProvider):
    """
    Email notification provider.

    Current implementation:
        Stub implementation.

    Future implementation:
        - SMTP
        - Microsoft Graph
        - SendGrid
        - Amazon SES
    """

    def send(
        self,
        notification: Notification,
    ) -> None:

        # Placeholder for future email delivery.
        print(
            f"[EMAIL] "
            f"To={notification.recipient} "
            f"Title={notification.title}"
        )