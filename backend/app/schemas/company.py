from typing import Optional
from pydantic import BaseModel


class CompanyBase(BaseModel):
    code: str
    name: str

    gstin: Optional[str] = None
    pan: Optional[str] = None
    cin: Optional[str] = None

    email: Optional[str] = None
    phone: Optional[str] = None

    address: Optional[str] = None

    is_active: bool = True


class CompanyCreate(CompanyBase):
    pass


class CompanyUpdate(CompanyBase):
    pass


class CompanyResponse(CompanyBase):
    id: int

    model_config = {
        "from_attributes": True
    }