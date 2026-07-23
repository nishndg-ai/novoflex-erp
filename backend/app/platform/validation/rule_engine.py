from __future__ import annotations

import re

from .exceptions import (
    InvalidValueError,
    MaxLengthError,
    MinLengthError,
    RegexValidationError,
    RequiredFieldError,
)
from .rules import ValidationRule


class RuleEngine:
    """
    Executes metadata validation rules.
    """

    def validate(
        self,
        value,
        rule: ValidationRule,
    ) -> None:

        if rule.rule == "required":
            if value in (None, ""):
                raise RequiredFieldError(
                    rule.message or f"{rule.field_name} is required."
                )

        elif rule.rule == "max_length":
            if value is not None and len(str(value)) > int(rule.value):
                raise MaxLengthError(
                    rule.message
                    or f"{rule.field_name} exceeds maximum length."
                )

        elif rule.rule == "min_length":
            if value is not None and len(str(value)) < int(rule.value):
                raise MinLengthError(
                    rule.message
                    or f"{rule.field_name} is below minimum length."
                )

        elif rule.rule == "regex":
            if value is not None and not re.match(
                str(rule.value),
                str(value),
            ):
                raise RegexValidationError(
                    rule.message
                    or f"{rule.field_name} has an invalid format."
                )

        elif rule.rule == "in":
            if value not in rule.value:
                raise InvalidValueError(
                    rule.message
                    or f"{rule.field_name} contains an invalid value."
                )