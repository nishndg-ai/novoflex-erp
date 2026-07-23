from __future__ import annotations

from .rules import ValidationRule


class RuleFactory:
    """
    Creates ValidationRule objects from runtime metadata.
    """

    @staticmethod
    def build(field) -> list[ValidationRule]:

        rules: list[ValidationRule] = []

        if getattr(field, "required", False):
            rules.append(
                ValidationRule(
                    field_name=field.field_name,
                    rule="required",
                )
            )

        max_length = getattr(field, "max_length", None)
        if max_length:
            rules.append(
                ValidationRule(
                    field_name=field.field_name,
                    rule="max_length",
                    value=max_length,
                )
            )

        min_length = getattr(field, "min_length", None)
        if min_length:
            rules.append(
                ValidationRule(
                    field_name=field.field_name,
                    rule="min_length",
                    value=min_length,
                )
            )

        pattern = getattr(field, "validation_pattern", None)
        if pattern:
            rules.append(
                ValidationRule(
                    field_name=field.field_name,
                    rule="regex",
                    value=pattern,
                )
            )

        return rules