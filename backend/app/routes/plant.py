from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.plant import Plant
from app.schemas.plant import (
    PlantCreate,
    PlantResponse,
)
from app.services.plant_service import plant_service

router = APIRouter(
    prefix="/plants",
    tags=["Plant"],
)


@router.get(
    "/",
    response_model=List[PlantResponse],
)
def get_all(
    db: Session = Depends(get_db),
):
    return plant_service.get_all(db)


@router.get(
    "/{plant_id}",
    response_model=PlantResponse,
)
def get_by_id(
    plant_id: int,
    db: Session = Depends(get_db),
):
    plant = plant_service.get_by_id(db, plant_id)

    if plant is None:
        raise HTTPException(
            status_code=404,
            detail="Plant not found",
        )

    return plant


@router.post(
    "/",
    response_model=PlantResponse,
)
def create(
    plant: PlantCreate,
    db: Session = Depends(get_db),
):
    db_obj = Plant(**plant.model_dump())

    return plant_service.create(
        db,
        db_obj,
    )


@router.put(
    "/{plant_id}",
    response_model=PlantResponse,
)
def update(
    plant_id: int,
    plant: PlantCreate,
    db: Session = Depends(get_db),
):
    db_obj = plant_service.get_by_id(
        db,
        plant_id,
    )

    if db_obj is None:
        raise HTTPException(
            status_code=404,
            detail="Plant not found",
        )

    for key, value in plant.model_dump().items():
        setattr(db_obj, key, value)

    return plant_service.update(
        db,
        db_obj,
    )


@router.delete(
    "/{plant_id}",
)
def delete(
    plant_id: int,
    db: Session = Depends(get_db),
):
    plant = plant_service.soft_delete(
        db,
        plant_id,
    )

    if plant is None:
        raise HTTPException(
            status_code=404,
            detail="Plant not found",
        )

    return {
        "message": "Plant deleted successfully"
    }