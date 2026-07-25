from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.platform.metadata.schemas.metadata_view_component import (
    MetadataViewComponentCreate,
    MetadataViewComponentUpdate,
)
from app.platform.metadata.services.metadata_view_component_service import (
    metadata_view_component_service,
)

router = APIRouter(
    prefix="/metadata/view-components",
    tags=["Metadata View Components"],
)


@router.get("/")
def get_components(
    db: Session = Depends(get_db),
):
    return metadata_view_component_service.get_all(db)


@router.get("/view/{view_id}")
def get_components_by_view(
    view_id: int,
    db: Session = Depends(get_db),
):
    return metadata_view_component_service.get_by_view(
        db,
        view_id,
    )


@router.get("/{component_id}")
def get_component(
    component_id: int,
    db: Session = Depends(get_db),
):
    return metadata_view_component_service.get_by_id(
        db,
        component_id,
    )


@router.post("/")
def create_component(
    payload: MetadataViewComponentCreate,
    db: Session = Depends(get_db),
):
    return metadata_view_component_service.create(
        db,
        payload,
    )


@router.put("/{component_id}")
def update_component(
    component_id: int,
    payload: MetadataViewComponentUpdate,
    db: Session = Depends(get_db),
):
    return metadata_view_component_service.update(
        db,
        component_id,
        payload,
    )


@router.delete("/{component_id}")
def delete_component(
    component_id: int,
    db: Session = Depends(get_db),
):
    return metadata_view_component_service.delete(
        db,
        component_id,
    )