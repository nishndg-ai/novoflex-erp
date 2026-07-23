from __future__ import annotations

from app.platform.events import (
    Event,
    EventRegistry,
    EventType,
)

from .approval_engine import ApprovalEngine
from .approval_history import ApprovalHistory
from .approval_instance import ApprovalInstance
from .approval_matrix import ApprovalMatrix
from .approval_mode import ApprovalMode
from .parallel_approval_engine import ParallelApprovalEngine
from .sequential_approval_engine import SequentialApprovalEngine
from .workflow_service import WorkflowService


class ApprovalService:
    """
    Enterprise Approval Service.

    Responsibilities
    ----------------
    - Resolve approvers
    - Execute approval strategies
    - Record approval history
    - Publish platform events
    - Integrate with workflow engine
    """

    def __init__(self):
        self.engine = ApprovalEngine()
        self.workflow = WorkflowService()

    def start(
        self,
        module_code: str,
        record_id,
        matrix: ApprovalMatrix,
        context: dict,
        mode: ApprovalMode = ApprovalMode.SEQUENTIAL,
    ) -> ApprovalInstance:

        approvers = self.engine.resolve_approvers(
            matrix=matrix,
            context=context,
        )

        instance = ApprovalInstance(
            module_code=module_code,
            record_id=record_id,
            approvers=approvers,
            mode=mode,
        )

        EventRegistry.dispatcher().dispatch(
            Event(
                event_type=EventType.BEFORE_WORKFLOW,
                module_code=module_code,
                payload={
                    "approval_instance": instance,
                },
            )
        )

        EventRegistry.dispatcher().dispatch(
            Event(
                event_type=EventType.AFTER_WORKFLOW,
                module_code=module_code,
                payload={
                    "approval_instance": instance,
                },
                result=instance,
            )
        )

        return instance

    def approve(
        self,
        instance: ApprovalInstance,
        user: str,
        comment: str | None = None,
    ) -> ApprovalHistory:

        if instance.mode == ApprovalMode.SEQUENTIAL:

            SequentialApprovalEngine.approve(
                instance,
                user,
            )

        else:

            ParallelApprovalEngine.approve(
                instance,
                user,
            )

        history = ApprovalHistory(
            module_code=instance.module_code,
            record_id=instance.record_id,
            approver=user,
            action="Approved",
            level=instance.current_level,
            comment=comment,
        )

        EventRegistry.dispatcher().dispatch(
            Event(
                event_type=EventType.AFTER_WORKFLOW,
                module_code=instance.module_code,
                payload={
                    "approval_history": history,
                    "approval_instance": instance,
                },
            )
        )

        return history

    def reject(
        self,
        instance: ApprovalInstance,
        user: str,
        comment: str | None = None,
    ) -> ApprovalHistory:

        instance.reject(user)

        history = ApprovalHistory(
            module_code=instance.module_code,
            record_id=instance.record_id,
            approver=user,
            action="Rejected",
            level=instance.current_level,
            comment=comment,
        )

        EventRegistry.dispatcher().dispatch(
            Event(
                event_type=EventType.AFTER_WORKFLOW,
                module_code=instance.module_code,
                payload={
                    "approval_history": history,
                    "approval_instance": instance,
                },
            )
        )

        return history