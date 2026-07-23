from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db

from app.platform.metadata.models.metadata_module import MetadataModule
from app.platform.metadata.schemas.metadata_module_schema import (
    MetadataModuleCreate,
    MetadataModuleResponse,
    MetadataModuleUpdate,
)
from app.platform.metadata.services.metadata_service import (
    metadata_service,
)

router = APIRouter(
    prefix="/metadata/modules",
    tags=["Metadata Modules"],
)


@router.get(
    "/",
    response_model=list[MetadataModuleResponse],
)
def get_modules(
    db: Session = Depends(get_db),
):
    return metadata_service.get_all_modules(db)


@router.get(
    "/{module_id}",
    response_model=MetadataModuleResponse,
)
def get_module(
    module_id: int,
    db: Session = Depends(get_db),
):
    module = metadata_service.get_module(
        db,
        module_id,
    )

    if module is None:
        raise HTTPException(
            status_code=404,
            detail="Module not found",
        )

    return module


@router.post(
    "/",
    response_model=MetadataModuleResponse,
)
def create_module(
    data: MetadataModuleCreate,
    db: Session = Depends(get_db),
):
    module = MetadataModule(**data.model_dump())

    try:
        return metadata_service.create_module(
            db,
            module,
        )

    except ValueError as ex:
        raise HTTPException(
            status_code=400,
            detail=str(ex),
        )


@router.put(
    "/{module_id}",
    response_model=MetadataModuleResponse,
)
def update_module(
    module_id: int,
    data: MetadataModuleUpdate,
    db: Session = Depends(get_db),
):
    module = metadata_service.get_module(
        db,
        module_id,
    )

    if module is None:
        raise HTTPException(
            status_code=404,
            detail="Module not found",
        )

    for key, value in data.model_dump().items():
        setattr(module, key, value)

    return metadata_service.update_module(
        db,
        module,
    )


@router.delete(
    "/{module_id}",
)
def delete_module(
    module_id: int,
    db: Session = Depends(get_db),
):
    module = metadata_service.delete_module(
        db,
        module_id,
    )

    if module is None:
        raise HTTPException(
            status_code=404,
            detail="Module not found",
        )

    return {
        "message": "Module deleted successfully"
    }