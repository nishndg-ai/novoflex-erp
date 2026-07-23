from __future__ import annotations


class ValidationException(Exception):
    """Base validation exception."""


class RequiredFieldError(ValidationException):
    """Raised when a required field is missing."""


class InvalidValueError(ValidationException):
    """Raised when a field value is invalid."""


class MaxLengthError(ValidationException):
    """Raised when a value exceeds the configured maximum length."""


class MinLengthError(ValidationException):
    """Raised when a value is shorter than the configured minimum length."""


class RegexValidationError(ValidationException):
    """Raised when a value does not match the configured pattern."""