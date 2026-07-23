from pydantic import BaseModel


class PlantBase(BaseModel):
    company_id: int
    code: str
    name: str
    address: str = ""
    city: str = ""
    state: str = ""
    country: str = "India"
    pincode: str = ""
    phone: str = ""
    email: str = ""
    is_active: bool = True


class PlantCreate(PlantBase):
    pass


class PlantUpdate(PlantBase):
    pass


class PlantResponse(PlantBase):
    id: int

    model_config = {
        "from_attributes": True
    }