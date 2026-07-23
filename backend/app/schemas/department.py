from pydantic import BaseModel


class DepartmentBase(BaseModel):
    plant_id: int
    code: str
    name: str
    is_active: bool = True


class DepartmentCreate(DepartmentBase):
    pass


class DepartmentUpdate(DepartmentBase):
    pass


class DepartmentResponse(DepartmentBase):
    id: int

    model_config = {
        "from_attributes": True
    }