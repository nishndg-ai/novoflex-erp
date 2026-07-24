from typing import List

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


class MetadataBuilderResponse(BaseModel):
    module: MetadataModuleResponse
    fields: List[MetadataFieldResponse]
    layouts: List[MetadataLayoutResponse]