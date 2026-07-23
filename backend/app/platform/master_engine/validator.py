from typing import Any


class ValidationEngine:

    def validate_required(
        self,
        data: dict,
        required_fields: list[str],
    ):

        missing = []

        for field in required_fields:
            if data.get(field) in [None, ""]:
                missing.append(field)

        if missing:
            raise ValueError(
                f"Required fields missing: {', '.join(missing)}"
            )

    def validate(
        self,
        data: dict,
        rules: dict[str, Any] | None = None,
    ):

        if rules is None:
            return True

        self.validate_required(
            data,
            rules.get("required", []),
        )

        return True