from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.platform.runtime.runtime_engine import RuntimeEngine
from app.platform.validation import ValidationResponse, ValidationService

router = APIRouter(
    prefix="/validation",
    tags=["Validation"],
)


def get_validation_service(
    db: Session,
) -> ValidationService:

    runtime_engine = RuntimeEngine(db)

    return ValidationService(runtime_engine)


@router.post("/{module_code}")
def validate(
    module_code: str,
    values: dict[str, Any],
    db: Session = Depends(get_db),
):

    service = get_validation_service(db)

    service.validate(
        module_code=module_code,
        values=values,
    )

    return ValidationResponse.success()