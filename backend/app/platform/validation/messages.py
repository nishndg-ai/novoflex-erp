from __future__ import annotations


class ValidationMessages:

    REQUIRED = "{field} is required."

    MAX_LENGTH = "{field} cannot exceed {value} characters."

    MIN_LENGTH = "{field} must be at least {value} characters."

    INVALID_VALUE = "{field} contains an invalid value."

    INVALID_FORMAT = "{field} has an invalid format."

    DUPLICATE_VALUE = "{field} already exists."

    GREATER_THAN = "{field} must be greater than {value}."

    LESS_THAN = "{field} must be less than {value}."

    INVALID_EMAIL = "Invalid email address."

    INVALID_PHONE = "Invalid phone number."

    INVALID_DATE = "Invalid date."

    INVALID_NUMBER = "Invalid number."