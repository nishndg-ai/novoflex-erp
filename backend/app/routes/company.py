from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.database.session import get_db

from app.models.company import Company

from app.schemas.company import (
    CompanyCreate,
    CompanyUpdate,
    CompanyResponse,
)

from app.services.company_service import company_service


router = APIRouter(
    prefix="/companies",
    tags=["Company"],
)


@router.get(
    "/",
    response_model=List[CompanyResponse],
)
def get_companies(
    db: Session = Depends(get_db),
):
    return company_service.get_all(db)


@router.get(
    "/{company_id}",
    response_model=CompanyResponse,
)
def get_company(
    company_id: int,
    db: Session = Depends(get_db),
):
    company = company_service.get_by_id(db, company_id)

    if company is None:
        raise HTTPException(
            status_code=404,
            detail="Company not found",
        )

    return company


@router.post(
    "/",
    response_model=CompanyResponse,
)
def create_company(
    company: CompanyCreate,
    db: Session = Depends(get_db),
):
    try:
        db_obj = Company(**company.model_dump())
        return company_service.create(db, db_obj)

    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail="Company code already exists.",
        )


@router.put(
    "/{company_id}",
    response_model=CompanyResponse,
)
def update_company(
    company_id: int,
    company: CompanyUpdate,
    db: Session = Depends(get_db),
):
    db_obj = company_service.get_by_id(db, company_id)

    if db_obj is None:
        raise HTTPException(
            status_code=404,
            detail="Company not found",
        )

    try:
        for key, value in company.model_dump().items():
            setattr(db_obj, key, value)

        return company_service.update(db, db_obj)

    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail="Company code already exists.",
        )


@router.delete("/{company_id}")
def delete_company(
    company_id: int,
    db: Session = Depends(get_db),
):
    obj = company_service.soft_delete(db, company_id)

    if obj is None:
        raise HTTPException(
            status_code=404,
            detail="Company not found",
        )

    return {
        "message": "Company deleted successfully"
    }