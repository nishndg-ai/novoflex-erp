from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.platform.metadata.schemas.metadata_field_schema import (
    MetadataFieldCreate,
    MetadataFieldUpdate,
)
from app.platform.metadata.services.metadata_field_service import (
    metadata_field_service,
)

router = APIRouter(
    prefix="/metadata/fields",
    tags=["Metadata Fields"],
)


@router.get("/{module_id}")
def get_fields(module_id: int, db: Session = Depends(get_db)):
    return metadata_field_service.get_fields_by_module(db, module_id)


@router.post("/")
def create_field(
    payload: MetadataFieldCreate,
    db: Session = Depends(get_db),
):
    return metadata_field_service.create(db, payload)


@router.put("/{field_id}")
def update_field(
    field_id: int,
    payload: MetadataFieldUpdate,
    db: Session = Depends(get_db),
):
    return metadata_field_service.update(db, field_id, payload)


@router.delete("/{field_id}")
def delete_field(
    field_id: int,
    db: Session = Depends(get_db),
):
    return metadata_field_service.delete(db, field_id)