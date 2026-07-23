from __future__ import annotations

from datetime import date, datetime
from decimal import Decimal


class TypeValidator:
    """
    Validates Python data types for runtime fields.
    """

    PYTHON_TYPES = {
        "string": str,
        "text": str,
        "integer": int,
        "float": float,
        "decimal": Decimal,
        "boolean": bool,
        "date": date,
        "datetime": datetime,
    }

    @classmethod
    def validate(
        cls,
        field_type: str,
        value,
    ) -> bool:

        if value is None:
            return True

        expected = cls.PYTHON_TYPES.get(field_type.lower())

        if expected is None:
            return True

        return isinstance(value, expected)