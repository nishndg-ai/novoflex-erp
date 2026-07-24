from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.platform.metadata.schemas.metadata_layout_schema import (
    MetadataLayoutCreate,
    MetadataLayoutUpdate,
)
from app.platform.metadata.services.metadata_layout_service import (
    metadata_layout_service,
)

router = APIRouter(
    prefix="/metadata/layouts",
    tags=["Metadata Layouts"],
)


@router.get("/")
def get_all(db: Session = Depends(get_db)):
    return metadata_layout_service.get_all(db)


@router.get("/{layout_id}")
def get_by_id(
    layout_id: int,
    db: Session = Depends(get_db),
):
    layout = metadata_layout_service.get_by_id(db, layout_id)

    if not layout:
        raise HTTPException(status_code=404, detail="Layout not found")

    return layout


@router.post("/")
def create(
    payload: MetadataLayoutCreate,
    db: Session = Depends(get_db),
):
    return metadata_layout_service.create(db, payload)


@router.put("/{layout_id}")
def update(
    layout_id: int,
    payload: MetadataLayoutUpdate,
    db: Session = Depends(get_db),
):
    layout = metadata_layout_service.update(
        db,
        layout_id,
        payload,
    )

    if not layout:
        raise HTTPException(status_code=404, detail="Layout not found")

    return layout


@router.delete("/{layout_id}")
def delete(
    layout_id: int,
    db: Session = Depends(get_db),
):
    deleted = metadata_layout_service.delete(
        db,
        layout_id,
    )

    if not deleted:
        raise HTTPException(status_code=404, detail="Layout not found")

    return {"message": "Metadata Layout deleted successfully"}