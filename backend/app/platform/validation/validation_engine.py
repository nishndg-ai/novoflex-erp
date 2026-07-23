from __future__ import annotations

from app.platform.runtime.types import RuntimeDefinition

from .coercion import ValueCoercion
from .exceptions import InvalidValueError
from .rule_engine import RuleEngine
from .rule_factory import RuleFactory
from .type_validator import TypeValidator


class ValidationEngine:
    """
    Metadata-driven validation engine.
    Performs:
    - Type coercion
    - Type validation
    - Rule validation
    """

    def __init__(self):
        self.rule_engine = RuleEngine()

    def validate(
        self,
        runtime: RuntimeDefinition,
        values: dict,
    ) -> dict:

        validated_values = {}

        for field in runtime.fields:

            field_name = field.field_name

            field_type = getattr(
                field,
                "field_type",
                "string",
            )

            value = values.get(field_name)

            value = ValueCoercion.convert(
                field_type,
                value,
            )

            if not TypeValidator.validate(
                field_type,
                value,
            ):
                raise InvalidValueError(
                    f"{field_name} must be of type {field_type}."
                )

            for rule in RuleFactory.build(field):
                self.rule_engine.validate(
                    value=value,
                    rule=rule,
                )

            validated_values[field_name] = value

        return validated_values