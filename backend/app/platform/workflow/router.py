from __future__ import annotations

from fastapi import APIRouter

from .approval_inbox_service import ApprovalInboxService

router = APIRouter(
    prefix="/workflow",
    tags=["Workflow"],
)

service = ApprovalInboxService()


@router.get("/inbox")
def get_pending():

    return service.pending()


@router.get("/inbox/all")
def get_all():

    return service.all()


@router.get("/inbox/{user}")
def get_user_pending(
    user: str,
):

    return service.pending_for_user(user)


@router.post("/approve")
def approve(
    module_code: str,
    record_id: str,
    approver: str,
    comment: str | None = None,
):

    return service.complete_task(
        module_code=module_code,
        record_id=record_id,
        approver=approver,
        comment=comment,
    )


@router.post("/reject")
def reject(
    module_code: str,
    record_id: str,
    approver: str,
    comment: str | None = None,
):

    return service.complete_task(
        module_code=module_code,
        record_id=record_id,
        approver=approver,
        comment=comment,
    )