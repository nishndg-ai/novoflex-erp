from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class WorkflowState:
    """
    Represents a workflow state.

    Examples:
        Draft
        Submitted
        Approved
        Rejected
        Closed
    """

    code: str
    name: str

    is_initial: bool = False
    is_final: bool = False

    color: str | None = None
    icon: str | None = None