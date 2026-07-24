from typing import Optional

from pydantic import BaseModel, ConfigDict


class MetadataFieldBase(BaseModel):
    module_id: int

    field_name: str
    display_name: str

    data_type: str
    control_type: str

    length: Optional[int] = None
    decimal_places: int = 0

    default_value: Optional[str] = None

    is_primary: bool = False
    is_required: bool = False
    is_unique: bool = False

    is_visible: bool = True
    is_editable: bool = True

    display_order: int = 1


class MetadataFieldCreate(MetadataFieldBase):
    pass


class MetadataFieldUpdate(MetadataFieldBase):
    pass


class MetadataFieldResponse(MetadataFieldBase):
    id: int

    model_config = ConfigDict(from_attributes=True)