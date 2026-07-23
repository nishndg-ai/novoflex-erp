from __future__ import annotations


class ValidationError(Exception):
    pass


class RuntimeValidator:

    def validate(
        self,
        fields,
        values: dict,
    ) -> None:

        for field in fields:

            if not getattr(field, "required", False):
                continue

            value = values.get(field.field_name)

            if value in (None, ""):
                raise ValidationError(
                    f"{field.label} is required."
                )

            max_length = getattr(field, "max_length", None)

            if (
                max_length
                and isinstance(value, str)
                and len(value) > max_length
            ):
                raise ValidationError(
                    f"{field.label} cannot exceed {max_length} characters."
                )