from __future__ import annotations

from .condition import WorkflowCondition


class WorkflowConditionEngine:
    """
    Evaluates workflow transition conditions.

    Supported operators:

        ==
        !=
        >
        >=
        <
        <=
        in
        not in
    """

    @staticmethod
    def evaluate(
        condition: WorkflowCondition | None,
        context: dict,
    ) -> bool:

        if condition is None:
            return True

        value = context.get(condition.field)

        operator = condition.operator

        expected = condition.value

        if operator == "==":
            return value == expected

        if operator == "!=":
            return value != expected

        if operator == ">":
            return value > expected

        if operator == ">=":
            return value >= expected

        if operator == "<":
            return value < expected

        if operator == "<=":
            return value <= expected

        if operator == "in":
            return value in expected

        if operator == "not in":
            return value not in expected

        raise ValueError(
            f"Unsupported workflow operator '{operator}'."
        )