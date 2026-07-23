from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.uom import UOM
from app.schemas.uom import (
    UOMCreate,
    UOMResponse,
)
from app.services.uom_service import uom_service

router = APIRouter(
    prefix="/uoms",
    tags=["UOM"],
)


@router.get("/", response_model=List[UOMResponse])
def get_all(db: Session = Depends(get_db)):
    return uom_service.get_all(db)


@router.get("/{uom_id}", response_model=UOMResponse)
def get_by_id(
    uom_id: int,
    db: Session = Depends(get_db),
):
    obj = uom_service.get_by_id(db, uom_id)

    if obj is None:
        raise HTTPException(404, "UOM not found")

    return obj


@router.post("/", response_model=UOMResponse)
def create(
    uom: UOMCreate,
    db: Session = Depends(get_db),
):
    db_obj = UOM(**uom.model_dump())

    return uom_service.create(
        db,
        db_obj,
    )


@router.put("/{uom_id}", response_model=UOMResponse)
def update(
    uom_id: int,
    uom: UOMCreate,
    db: Session = Depends(get_db),
):
    db_obj = uom_service.get_by_id(
        db,
        uom_id,
    )

    if db_obj is None:
        raise HTTPException(404, "UOM not found")

    for key, value in uom.model_dump().items():
        setattr(db_obj, key, value)

    return uom_service.update(
        db,
        db_obj,
    )


@router.delete("/{uom_id}")
def delete(
    uom_id: int,
    db: Session = Depends(get_db),
):
    obj = uom_service.soft_delete(
        db,
        uom_id,
    )

    if obj is None:
        raise HTTPException(404, "UOM not found")

    return {
        "message": "UOM deleted successfully"
    }