from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.platform.metadata.schemas.metadata_view import (
    MetadataViewCreate,
    MetadataViewUpdate,
)
from app.platform.metadata.services.metadata_view_service import (
    metadata_view_service,
)

router = APIRouter(
    prefix="/metadata/views",
    tags=["Metadata Views"],
)


@router.get("/")
def get_views(db: Session = Depends(get_db)):
    return metadata_view_service.get_all(db)


@router.get("/{view_id}")
def get_view(
    view_id: int,
    db: Session = Depends(get_db),
):
    return metadata_view_service.get_by_id(db, view_id)


@router.post("/")
def create_view(
    payload: MetadataViewCreate,
    db: Session = Depends(get_db),
):
    return metadata_view_service.create(db, payload)


@router.put("/{view_id}")
def update_view(
    view_id: int,
    payload: MetadataViewUpdate,
    db: Session = Depends(get_db),
):
    return metadata_view_service.update(
        db,
        view_id,
        payload,
    )


@router.delete("/{view_id}")
def delete_view(
    view_id: int,
    db: Session = Depends(get_db),
):
    return metadata_view_service.delete(
        db,
        view_id,
    )