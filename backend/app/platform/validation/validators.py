from __future__ import annotations

from .rule_engine import RuleEngine
from .rule_factory import RuleFactory


class Validators:
    """
    Helper class to validate a single runtime field.
    """

    def __init__(self):
        self.rule_engine = RuleEngine()

    def validate_field(
        self,
        field,
        value,
    ) -> None:

        rules = RuleFactory.build(field)

        for rule in rules:
            self.rule_engine.validate(
                value=value,
                rule=rule,
            )