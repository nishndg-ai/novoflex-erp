from pydantic import BaseModel


class TemplateResponse(BaseModel):
    id: int
    name: str
    module: str
    file_name: str
    sheet_name: str | None = None
    version: int
    is_active: bool

    model_config = {
        "from_attributes": True
    }