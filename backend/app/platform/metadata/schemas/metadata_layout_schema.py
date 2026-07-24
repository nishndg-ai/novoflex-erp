from typing import Optional

from pydantic import BaseModel


class MetadataLayoutBase(BaseModel):
    module_id: int
    field_id: int
    section: Optional[str] = None
    row_no: int = 1
    column_no: int = 1
    column_span: int = 1
    tab_name: Optional[str] = None
    is_visible: bool = True


class MetadataLayoutCreate(MetadataLayoutBase):
    pass


class MetadataLayoutUpdate(BaseModel):
    module_id: Optional[int] = None
    field_id: Optional[int] = None
    section: Optional[str] = None
    row_no: Optional[int] = None
    column_no: Optional[int] = None
    column_span: Optional[int] = None
    tab_name: Optional[str] = None
    is_visible: Optional[bool] = None


class MetadataLayoutResponse(MetadataLayoutBase):
    id: int

    model_config = {
        "from_attributes": True
    }