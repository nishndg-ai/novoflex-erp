from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from .notification import Notification


class NotificationProvider(ABC):
    """
    Base notification provider.

    All notification channels should implement this interface.
    """

    @abstractmethod
    def send(
        self,
        notification: Notification,
    ) -> None:
        """
        Deliver a notification.
        """
        raise NotImplementedError