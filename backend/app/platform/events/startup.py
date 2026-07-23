from __future__ import annotations

from .registry import EventRegistry


def initialize_events():
    """
    Initializes the platform event system.

    Module event handlers will be registered here during startup.
    """

    # Force dispatcher creation
    EventRegistry.dispatcher()

    # Future registrations:
    #
    # EventRegistry.dispatcher().register(
    #     EventType.AFTER_CREATE,
    #     InventoryPostingHandler(),
    # )
    #
    # EventRegistry.dispatcher().register(
    #     EventType.AFTER_CREATE,
    #     AuditHandler(),
    # )
    #
    # EventRegistry.dispatcher().register(
    #     EventType.AFTER_APPROVAL,
    #     EmailNotificationHandler(),
    # )