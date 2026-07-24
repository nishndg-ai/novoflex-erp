from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.platform.metadata.services.metadata_builder_service import (
    metadata_builder_service,
)

router = APIRouter(
    prefix="/metadata/builder",
    tags=["Metadata Builder"],
)


@router.get("/{module_id}")
def get_builder(
    module_id: int,
    db: Session = Depends(get_db),
):
    result = metadata_builder_service.get_builder(db, module_id)

    if not result:
        raise HTTPException(
            status_code=404,
            detail="Module not found",
        )

    return result