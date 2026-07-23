from typing import Optional

from pydantic import BaseModel, ConfigDict


class MetadataModuleBase(BaseModel):
    module_code: str
    module_name: str
    display_name: str
    description: Optional[str] = None
    icon: Optional[str] = None
    route: str
    api_endpoint: str
    table_name: str
    schema_name: str = "public"
    display_order: int = 0
    is_system: bool = False
    allow_import: bool = True
    allow_export: bool = True
    allow_workflow: bool = False
    allow_approval: bool = False


class MetadataModuleCreate(MetadataModuleBase):
    pass


class MetadataModuleUpdate(MetadataModuleBase):
    pass


class MetadataModuleResponse(MetadataModuleBase):
    id: int
    is_active: bool
    version: int

    model_config = ConfigDict(from_attributes=True)