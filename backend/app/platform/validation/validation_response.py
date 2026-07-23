from __future__ import annotations


class ValidationResponse:
    """
    Standard validation response.
    """

    @staticmethod
    def success() -> dict:

        return {
            "success": True,
            "message": "Validation successful.",
        }

    @staticmethod
    def failure(message: str) -> dict:

        return {
            "success": False,
            "message": message,
        }