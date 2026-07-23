from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.company import Company
from app.schemas.company import (
    CompanyCreate,
    CompanyResponse,
)
from app.services.company_service import company_service

router = APIRouter(
    prefix="/companies",
    tags=["Company"],
)


@router.get("/", response_model=List[CompanyResponse])
def get_all(db: Session = Depends(get_db)):
    return company_service.get_all(db)


@router.get("/{company_id}", response_model=CompanyResponse)
def get_by_id(
    company_id: int,
    db: Session = Depends(get_db),
):
    obj = company_service.get_by_id(db, company_id)

    if obj is None:
        raise HTTPException(404, "Company not found")

    return obj


@router.post("/", response_model=CompanyResponse)
def create(
    company: CompanyCreate,
    db: Session = Depends(get_db),
):
    db_obj = Company(**company.model_dump())

    return company_service.create(db, db_obj)


@router.put("/{company_id}", response_model=CompanyResponse)
def update(
    company_id: int,
    company: CompanyCreate,
    db: Session = Depends(get_db),
):
    db_obj = company_service.get_by_id(db, company_id)

    if db_obj is None:
        raise HTTPException(404, "Company not found")

    for key, value in company.model_dump().items():
        setattr(db_obj, key, value)

    return company_service.update(db, db_obj)


@router.delete("/{company_id}")
def delete(
    company_id: int,
    db: Session = Depends(get_db),
):
    obj = company_service.soft_delete(db, company_id)

    if obj is None:
        raise HTTPException(404, "Company not found")

    return {
        "message": "Company deleted successfully"
    }