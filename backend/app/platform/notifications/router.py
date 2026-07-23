from __future__ import annotations

from fastapi import APIRouter, HTTPException

from .inapp_provider import InAppNotificationProvider
from .notification_registry import notification_registry
from .notification_service import NotificationService

router = APIRouter(
    prefix="/notifications",
    tags=["Notifications"],
)

service = NotificationService()


def _provider() -> InAppNotificationProvider:

    provider = notification_registry.provider("IN_APP")

    if not isinstance(provider, InAppNotificationProvider):
        raise HTTPException(
            status_code=500,
            detail="In-app notification provider not configured.",
        )

    return provider


@router.post("/send")
def send_notification(
    recipient: str,
    title: str,
    message: str,
):

    return service.send(
        recipient=recipient,
        title=title,
        message=message,
    )


@router.get("/{user}")
def get_notifications(
    user: str,
):

    return _provider().all(user)


@router.get("/{user}/unread")
def get_unread_notifications(
    user: str,
):

    return _provider().unread(user)


@router.post("/read/{notification_id}")
def mark_notification_read(
    notification_id: str,
):

    success = _provider().mark_read(notification_id)

    return {
        "success": success,
    }