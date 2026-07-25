from typing import List, Optional

from pydantic import BaseModel

from app.platform.metadata.schemas.metadata_module_schema import (
    MetadataModuleResponse,
)
from app.platform.metadata.schemas.metadata_field_schema import (
    MetadataFieldResponse,
)
from app.platform.metadata.schemas.metadata_layout_schema import (
    MetadataLayoutResponse,
)


class MetadataFormField(BaseModel):
    field: MetadataFieldResponse
    layout: Optional[MetadataLayoutResponse] = None


class MetadataFormResponse(BaseModel):
    module: MetadataModuleResponse
    fields: List[MetadataFormField]