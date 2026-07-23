from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class ValidationRule:
    field_name: str
    rule: str
    value: object | None = None
    message: str | None = None