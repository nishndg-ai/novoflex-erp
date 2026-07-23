from __future__ import annotations

from typing import Any


class CrudResponse:

    @staticmethod
    def success(
        data: Any = None,
        message: str = "Success",
    ) -> dict[str, Any]:

        return {
            "success": True,
            "message": message,
            "data": data,
        }

    @staticmethod
    def created(
        record_id: int,
        message: str = "Record created successfully",
    ) -> dict[str, Any]:

        return {
            "success": True,
            "message": message,
            "data": {
                "id": record_id,
            },
        }

    @staticmethod
    def updated(
        message: str = "Record updated successfully",
    ) -> dict[str, Any]:

        return {
            "success": True,
            "message": message,
        }

    @staticmethod
    def deleted(
        message: str = "Record deleted successfully",
    ) -> dict[str, Any]:

        return {
            "success": True,
            "message": message,
        }

    @staticmethod
    def error(
        message: str,
    ) -> dict[str, Any]:

        return {
            "success": False,
            "message": message,
        }