from __future__ import annotations

from dataclasses import dataclass, field

from .approver import WorkflowApprover


@dataclass(frozen=True)
class ApprovalMatrixRule:
    """
    Approval rule.

    Example

        Amount 0 - 50,000
            -> Purchase Manager

        Amount 50,001 - 500,000
            -> Plant Head

        Amount > 500,000
            -> Director
    """

    field: str

    minimum: float | None = None

    maximum: float | None = None

    approvers: list[WorkflowApprover] = field(
        default_factory=list
    )

    priority: int = 1


@dataclass
class ApprovalMatrix:
    """
    Collection of approval rules.
    """

    name: str

    rules: list[ApprovalMatrixRule] = field(
        default_factory=list
    )

    def find_rule(
        self,
        context: dict,
    ) -> ApprovalMatrixRule | None:

        for rule in sorted(
            self.rules,
            key=lambda r: r.priority,
        ):

            value = context.get(rule.field)

            if value is None:
                continue

            if (
                rule.minimum is not None
                and value < rule.minimum
            ):
                continue

            if (
                rule.maximum is not None
                and value > rule.maximum
            ):
                continue

            return rule

        return None