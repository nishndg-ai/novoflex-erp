from typing import List

from pydantic import BaseModel

from app.platform.metadata.schemas.metadata_field_schema import (
    MetadataFieldResponse,
)
from app.platform.metadata.schemas.metadata_layout_schema import (
    MetadataLayoutResponse,
)
from app.platform.metadata.schemas.metadata_module_schema import (
    MetadataModuleResponse,
)
from app.platform.metadata.schemas.metadata_view import (
    MetadataViewResponse,
)
from app.platform.metadata.schemas.metadata_view_component import (
    MetadataViewComponentResponse,
)


class MetadataBuilderResponse(BaseModel):
    module: MetadataModuleResponse
    fields: List[MetadataFieldResponse]
    layouts: List[MetadataLayoutResponse]
    views: List[MetadataViewResponse]
    view_components: List[MetadataViewComponentResponse]