from typing import Optional, List

from pydantic import BaseModel


class DesignerFieldRequest(BaseModel):

    name: str

    label: str

    data_type: str = "string"

    control_type: str = "TEXTBOX"

    length: Optional[int] = 150

    required: bool = False

    unique: bool = False

    show_in_grid: bool = True

    searchable: bool = True

    filterable: bool = True



class DesignerFeatures(BaseModel):

    excel_import: bool = False

    workflow: bool = False

    dashboard: bool = False

    ai: bool = False



class BusinessObjectCreateRequest(BaseModel):

    object_name: str

    description: Optional[str] = None

    application: str

    category: str

    features: DesignerFeatures = DesignerFeatures()

    fields: List[DesignerFieldRequest]