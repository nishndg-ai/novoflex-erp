from __future__ import annotations

from typing import Any


class LookupItem:

    @staticmethod
    def build(
        row: dict[str, Any],
    ) -> dict[str, Any]:

        return {
            "id": row.get("id"),
            "code": (
                row.get("code")
                or row.get("module_code")
                or row.get("employee_code")
                or row.get("item_code")
            ),
            "name": (
                row.get("name")
                or row.get("title")
                or row.get("description")
                or row.get("company_name")
                or row.get("plant_name")
                or row.get("department_name")
            ),
            "data": row,
        }