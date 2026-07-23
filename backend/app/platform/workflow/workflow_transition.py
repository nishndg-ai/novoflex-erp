from __future__ import annotations

from dataclasses import dataclass, field

from .condition import WorkflowCondition


@dataclass(frozen=True)
class WorkflowTransition:
    """
    Represents an allowed transition between two workflow states.

    Example:

        Draft ------Submit------> Submitted
        Submitted --Approve-----> Approved
        Submitted --Reject------> Rejected
    """

    code: str

    from_state: str

    to_state: str

    action: str

    roles: list[str] = field(default_factory=list)

    conditions: list[WorkflowCondition] = field(
        default_factory=list
    )

    requires_comment: bool = False

    auto_transition: bool = False

    notify_roles: list[str] = field(
        default_factory=list
    )