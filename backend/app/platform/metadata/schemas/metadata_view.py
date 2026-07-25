from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict

from app.platform.metadata.enums import ViewType


class MetadataViewBase(BaseModel):
    module_id: int
    view_code: str
    display_name: str
    description: Optional[str] = None
    view_type: ViewType

    page_size: int = 25

    default_sort_field: Optional[str] = None
    default_sort_order: Optional[str] = None

    is_default: bool = False

    allow_search: bool = True
    allow_filter: bool = True
    allow_sort: bool = True
    allow_export: bool = True
    allow_grouping: bool = True
    allow_column_resize: bool = True
    allow_column_reorder: bool = True
    allow_pivot: bool = False


class MetadataViewCreate(MetadataViewBase):
    pass


class MetadataViewUpdate(BaseModel):
    display_name: Optional[str] = None
    description: Optional[str] = None
    view_type: Optional[ViewType] = None

    page_size: Optional[int] = None

    default_sort_field: Optional[str] = None
    default_sort_order: Optional[str] = None

    is_default: Optional[bool] = None

    allow_search: Optional[bool] = None
    allow_filter: Optional[bool] = None
    allow_sort: Optional[bool] = None
    allow_export: Optional[bool] = None
    allow_grouping: Optional[bool] = None
    allow_column_resize: Optional[bool] = None
    allow_column_reorder: Optional[bool] = None
    allow_pivot: Optional[bool] = None


class MetadataViewResponse(MetadataViewBase):
    id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime
    created_by: Optional[str]
    updated_by: Optional[str]
    version: int

    model_config = ConfigDict(from_attributes=True)