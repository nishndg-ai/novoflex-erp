from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class WorkflowApprover:
    """
    Represents a workflow approver.

    Examples:

        User
        Role
        Department Head
        Reporting Manager
        Plant Head
        Quality Head
    """

    approver_type: str

    value: str

    sequence: int = 1

    required: bool = True