from __future__ import annotations

from .email_provider import EmailNotificationProvider
from .inapp_provider import InAppNotificationProvider
from .notification_provider import NotificationProvider


class NotificationRegistry:
    """
    Registry of notification providers.

    Multiple providers may be registered:
    - In-App
    - Email
    - SMS
    - WhatsApp
    - Teams
    - Slack
    """

    def __init__(self):

        self._providers: dict[str, NotificationProvider] = {}

        self.register(
            "IN_APP",
            InAppNotificationProvider(),
        )

        self.register(
            "EMAIL",
            EmailNotificationProvider(),
        )

    def register(
        self,
        channel: str,
        provider: NotificationProvider,
    ) -> None:

        self._providers[channel.upper()] = provider

    def provider(
        self,
        channel: str,
    ) -> NotificationProvider | None:

        return self._providers.get(channel.upper())

    def providers(
        self,
    ) -> dict[str, NotificationProvider]:

        return dict(self._providers)


notification_registry = NotificationRegistry()