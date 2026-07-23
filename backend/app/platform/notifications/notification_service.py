from __future__ import annotations

from collections.abc import Iterable

from .notification import Notification
from .notification_registry import notification_registry


class NotificationService:
    """
    Central notification service.

    All ERP modules should use this service to
    send notifications.
    """

    def send(
        self,
        recipient: str,
        title: str,
        message: str,
        channels: Iterable[str] | None = None,
        priority: str = "Normal",
        metadata: dict | None = None,
    ) -> Notification:

        notification = Notification(
            recipient=recipient,
            title=title,
            message=message,
            priority=priority,
            metadata=metadata or {},
        )

        channels = list(channels or ["IN_APP"])

        for channel in channels:

            provider = notification_registry.provider(channel)

            if provider is None:
                continue

            notification.channel = channel.upper()

            provider.send(notification)

        return notification

    def send_to_many(
        self,
        recipients: Iterable[str],
        title: str,
        message: str,
        channels: Iterable[str] | None = None,
        priority: str = "Normal",
        metadata: dict | None = None,
    ) -> list[Notification]:

        notifications: list[Notification] = []

        for recipient in recipients:

            notifications.append(
                self.send(
                    recipient=recipient,
                    title=title,
                    message=message,
                    channels=channels,
                    priority=priority,
                    metadata=metadata,
                )
            )

        return notifications