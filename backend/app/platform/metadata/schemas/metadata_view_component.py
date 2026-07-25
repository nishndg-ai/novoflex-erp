from datetime import datetime
from typing import Any, Dict, Optional

from pydantic import BaseModel, ConfigDict

from app.platform.metadata.enums import ViewComponentType


class MetadataViewComponentBase(BaseModel):
    view_id: int
    field_id: Optional[int] = None

    component_type: ViewComponentType
    component_name: str
    display_name: str
    description: Optional[str] = None

    display_order: int = 1

    row_no: int = 1
    column_no: int = 1
    column_span: int = 1

    is_visible: bool = True
    is_readonly: bool = False

    css_class: Optional[str] = None
    style: Optional[str] = None

    properties: Optional[Dict[str, Any]] = None


class MetadataViewComponentCreate(MetadataViewComponentBase):
    pass


class MetadataViewComponentUpdate(BaseModel):
    field_id: Optional[int] = None

    component_type: Optional[ViewComponentType] = None
    component_name: Optional[str] = None
    display_name: Optional[str] = None
    description: Optional[str] = None

    display_order: Optional[int] = None

    row_no: Optional[int] = None
    column_no: Optional[int] = None
    column_span: Optional[int] = None

    is_visible: Optional[bool] = None
    is_readonly: Optional[bool] = None

    css_class: Optional[str] = None
    style: Optional[str] = None

    properties: Optional[Dict[str, Any]] = None


class MetadataViewComponentResponse(MetadataViewComponentBase):
    id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime
    created_by: Optional[str]
    updated_by: Optional[str]
    version: int

    model_config = ConfigDict(from_attributes=True)