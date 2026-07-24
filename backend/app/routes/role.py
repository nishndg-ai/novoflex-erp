from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.database.session import get_db

from app.models.role import Role

from app.schemas.role import (
    RoleCreate,
    RoleUpdate,
    RoleResponse,
)

from app.services.role_service import role_service


router = APIRouter(
    prefix="/roles",
    tags=["Role"],
)


@router.get(
    "/",
    response_model=List[RoleResponse],
)
def get_roles(
    db: Session = Depends(get_db),
):
    return role_service.get_all(db)


@router.get(
    "/{role_id}",
    response_model=RoleResponse,
)
def get_role(
    role_id: int,
    db: Session = Depends(get_db),
):
    role = role_service.get_by_id(db, role_id)

    if role is None:
        raise HTTPException(
            status_code=404,
            detail="Role not found",
        )

    return role


@router.post(
    "/",
    response_model=RoleResponse,
)
def create_role(
    role: RoleCreate,
    db: Session = Depends(get_db),
):
    try:
        db_obj = Role(**role.model_dump())
        return role_service.create(db, db_obj)

    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail="Role code already exists.",
        )


@router.put(
    "/{role_id}",
    response_model=RoleResponse,
)
def update_role(
    role_id: int,
    role: RoleUpdate,
    db: Session = Depends(get_db),
):
    db_obj = role_service.get_by_id(db, role_id)

    if db_obj is None:
        raise HTTPException(
            status_code=404,
            detail="Role not found",
        )

    try:
        for key, value in role.model_dump().items():
            setattr(db_obj, key, value)

        return role_service.update(db, db_obj)

    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail="Role code already exists.",
        )


@router.delete("/{role_id}")
def delete_role(
    role_id: int,
    db: Session = Depends(get_db),
):
    obj = role_service.soft_delete(db, role_id)

    if obj is None:
        raise HTTPException(
            status_code=404,
            detail="Role not found",
        )

    return {
        "message": "Role deleted successfully"
    }