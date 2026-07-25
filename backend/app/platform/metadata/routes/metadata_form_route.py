from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db

from app.platform.metadata.schemas.metadata_form_schema import (
    MetadataFormResponse,
)
from app.platform.metadata.services.metadata_form_service import (
    metadata_form_service,
)

router = APIRouter(
    prefix="/metadata/form",
    tags=["Metadata Form"],
)


@router.get(
    "/{module_code}",
    response_model=MetadataFormResponse,
)
def get_form(
    module_code: str,
    db: Session = Depends(get_db),
):
    form = metadata_form_service.get_form(
        db,
        module_code,
    )

    if form is None:
        raise HTTPException(
            status_code=404,
            detail="Module not found",
        )

    return form