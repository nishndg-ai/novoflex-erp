from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from .event import Event


class EventHandler(ABC):
    """
    Base class for all platform event handlers.
    """

    @abstractmethod
    def handle(
        self,
        event: Event,
    ) -> None:
        """
        Handle a platform event.
        """
        raise NotImplementedError