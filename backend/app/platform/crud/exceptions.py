from __future__ import annotations


class CrudException(Exception):
    """Base CRUD exception."""


class RecordNotFound(CrudException):
    """Raised when a record is not found."""


class DuplicateRecord(CrudException):
    """Raised when a duplicate record exists."""


class InvalidData(CrudException):
    """Raised when invalid data is supplied."""


class PermissionDenied(CrudException):
    """Raised when the user has insufficient permissions."""