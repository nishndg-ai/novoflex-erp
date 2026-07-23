from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.department import Department
from app.schemas.department import (
    DepartmentCreate,
    DepartmentResponse,
)
from app.services.department_service import department_service

router = APIRouter(
    prefix="/departments",
    tags=["Department"],
)


@router.get(
    "/",
    response_model=List[DepartmentResponse],
)
def get_all(
    db: Session = Depends(get_db),
):
    return department_service.get_all(db)


@router.get(
    "/{department_id}",
    response_model=DepartmentResponse,
)
def get_by_id(
    department_id: int,
    db: Session = Depends(get_db),
):
    department = department_service.get_by_id(
        db,
        department_id,
    )

    if department is None:
        raise HTTPException(
            status_code=404,
            detail="Department not found",
        )

    return department


@router.post(
    "/",
    response_model=DepartmentResponse,
)
def create(
    department: DepartmentCreate,
    db: Session = Depends(get_db),
):
    db_obj = Department(**department.model_dump())

    return department_service.create(
        db,
        db_obj,
    )


@router.put(
    "/{department_id}",
    response_model=DepartmentResponse,
)
def update(
    department_id: int,
    department: DepartmentCreate,
    db: Session = Depends(get_db),
):
    db_obj = department_service.get_by_id(
        db,
        department_id,
    )

    if db_obj is None:
        raise HTTPException(
            status_code=404,
            detail="Department not found",
        )

    for key, value in department.model_dump().items():
        setattr(db_obj, key, value)

    return department_service.update(
        db,
        db_obj,
    )


@router.delete(
    "/{department_id}",
)
def delete(
    department_id: int,
    db: Session = Depends(get_db),
):
    department = department_service.soft_delete(
        db,
        department_id,
    )

    if department is None:
        raise HTTPException(
            status_code=404,
            detail="Department not found",
        )

    return {
        "message": "Department deleted successfully"
    }