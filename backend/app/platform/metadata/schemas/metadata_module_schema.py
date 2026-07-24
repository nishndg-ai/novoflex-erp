from typing import Optional

from pydantic import BaseModel, ConfigDict


class MetadataModuleBase(BaseModel):
    module_code: str
    module_name: str
    display_name: str

    description: Optional[str] = None

    application: str
    category: str

    route: str
    icon: Optional[str] = None
    menu_order: int = 0

    table_name: str
    api_endpoint: str
    page_size: int = 20

    supports_excel: bool = True
    supports_workflow: bool = False
    supports_dashboard: bool = False
    supports_ai: bool = False

    is_system: bool = False


class MetadataModuleCreate(MetadataModuleBase):
    pass


class MetadataModuleUpdate(MetadataModuleBase):
    pass


class MetadataModuleResponse(MetadataModuleBase):
    id: int
    is_active: bool
    version: int

    model_config = ConfigDict(from_attributes=True)