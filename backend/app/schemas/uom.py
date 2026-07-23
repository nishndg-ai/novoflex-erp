from typing import Optional
from pydantic import BaseModel


class UOMBase(BaseModel):
    code: str
    name: str
    description: Optional[str] = None
    is_active: bool = True


class UOMCreate(UOMBase):
    pass


class UOMUpdate(UOMBase):
    pass


class UOMResponse(UOMBase):
    id: int

    model_config = {
        "from_attributes": True
    }