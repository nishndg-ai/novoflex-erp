from __future__ import annotations

from datetime import date, datetime
from decimal import Decimal


class ValueCoercion:
    """
    Converts incoming values to the expected Python type.
    """

    @staticmethod
    def convert(
        field_type: str,
        value,
    ):

        if value is None:
            return None

        field_type = field_type.lower()

        if field_type in ("string", "text"):
            return str(value)

        if field_type == "integer":
            return int(value)

        if field_type == "float":
            return float(value)

        if field_type == "decimal":
            return Decimal(str(value))

        if field_type == "boolean":

            if isinstance(value, bool):
                return value

            return str(value).lower() in (
                "1",
                "true",
                "yes",
                "y",
            )

        if field_type == "date":

            if isinstance(value, date):
                return value

            return date.fromisoformat(str(value))

        if field_type == "datetime":

            if isinstance(value, datetime):
                return value

            return datetime.fromisoformat(str(value))

        return value