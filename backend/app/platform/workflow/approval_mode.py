from __future__ import annotations

from enum import Enum


class ApprovalMode(str, Enum):
    """
    Approval execution strategy.

    SEQUENTIAL
        Approvers execute one after another.

    PARALLEL
        All approvers receive the task simultaneously.

    ANYONE
        Any one approver can approve.

    MAJORITY
        Majority approval wins.

    UNANIMOUS
        Every approver must approve.
    """

    SEQUENTIAL = "sequential"

    PARALLEL = "parallel"

    ANYONE = "anyone"

    MAJORITY = "majority"

    UNANIMOUS = "unanimous"