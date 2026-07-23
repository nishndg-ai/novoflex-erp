from __future__ import annotations

from typing import Any

from app.platform.runtime.types import RuntimeDefinition


class ValidationError(Exception):
    """Raised when metadata validation fails."""


class RuntimeValidator:
    """
    Metadata-driven validator.

    Uses RuntimeDefinition.fields to validate incoming payloads.
    """

    def validate(
        self,
        runtime: RuntimeDefinition,
        values: dict[str, Any],
    ) -> dict[str, Any]:

        validated: dict[str, Any] = {}

        for field in runtime.fields:

            field_name = field.field_name

            value = values.get(field_name)

            # -----------------------------------------
            # Required
            # -----------------------------------------

            if field.is_required:

                if value is None or value == "":

                    raise ValidationError(
                        f"{field.display_name} is required."
                    )

            # -----------------------------------------
            # Skip empty optional fields
            # -----------------------------------------

            if value is None:

                continue

            # -----------------------------------------
            # Length validation
            # -----------------------------------------

            if (
                isinstance(value, str)
                and field.length
                and len(value) > field.length
            ):

                raise ValidationError(
                    f"{field.display_name} "
                    f"cannot exceed {field.length} characters."
                )

            validated[field_name] = value

        return validated