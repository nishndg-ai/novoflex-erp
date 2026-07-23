from __future__ import annotations

from .notification import Notification
from .notification_provider import NotificationProvider


class InAppNotificationProvider(NotificationProvider):
    """
    In-app notification provider.

    Current implementation:
        Stores notifications in memory.

    Future implementation:
        Persist notifications in the database.
    """

    def __init__(self):
        self.notifications: list[Notification] = []

    def send(
        self,
        notification: Notification,
    ) -> None:

        self.notifications.append(notification)

    def unread(
        self,
        recipient: str,
    ) -> list[Notification]:

        return [
            notification
            for notification in self.notifications
            if (
                notification.recipient == recipient
                and not notification.read
            )
        ]

    def all(
        self,
        recipient: str,
    ) -> list[Notification]:

        return [
            notification
            for notification in self.notifications
            if notification.recipient == recipient
        ]

    def mark_read(
        self,
        notification_id: str,
    ) -> bool:

        for notification in self.notifications:

            if notification.id == notification_id:

                notification.mark_read()

                return True

        return False

    def clear(
        self,
    ) -> None:

        self.notifications.clear()