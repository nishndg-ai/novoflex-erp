from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class WorkflowCondition:
    """
    Represents a transition condition.

    Examples

        amount > 50000

        department == "QA"

        plant == "KOL"

        priority == "High"
    """

    field: str

    operator: str

    value: object