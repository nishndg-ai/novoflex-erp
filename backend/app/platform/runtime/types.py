from typing import Any

from pydantic import BaseModel, ConfigDict, Field



# ==========================================================
# MODULE
# ==========================================================

class ModuleDefinition(BaseModel):

    id: int

    module_code: str
    module_name: str
    display_name: str

    description: str | None = None

    application: str
    category: str

    route: str
    icon: str | None = None

    menu_order: int

    table_name: str
    api_endpoint: str

    page_size: int

    supports_excel: bool
    supports_workflow: bool
    supports_dashboard: bool
    supports_ai: bool

    is_system: bool


    model_config = ConfigDict(
        from_attributes=True
    )



# ==========================================================
# FIELD
# ==========================================================

class FieldDefinition(BaseModel):

    id: int

    field_name: str
    display_name: str

    data_type: str
    control_type: str

    display_order: int

    is_required: bool = False
    is_unique: bool = False
    is_visible: bool = True
    is_editable: bool = True
    is_primary: bool = False

    length: int | None = None
    decimal_places: int | None = None

    default_value: Any | None = None


    show_in_grid: bool = True
    grid_order: int = 0
    grid_width: int = 150

    is_sortable: bool = True
    is_filterable: bool = True
    is_searchable: bool = True


    validation_rules: list[str] = Field(
        default_factory=list
    )


    model_config = ConfigDict(
        from_attributes=True
    )



# ==========================================================
# LAYOUT
# ==========================================================

class LayoutDefinition(BaseModel):

    id: int

    row_no: int
    column_no: int
    column_span: int

    field_name: str


    model_config = ConfigDict(
        from_attributes=True
    )



# ==========================================================
# VIEW COMPONENT
# ==========================================================

class ViewComponentDefinition(BaseModel):

    id: int

    view_id: int

    component_type: str

    component_key: str


    title: str | None = None

    field_name: str | None = None



    row_no: int

    column_no: int

    column_span: int



    width: int | None = None

    height: int | None = None



    # Runtime UI configuration
    #
    # Example:
    #
    # {
    #     "control_type": "checkbox"
    # }
    #
    properties: dict[str, Any] | None = None



    # Backward compatibility
    config: dict[str, Any] | None = None



    display_order: int

    is_visible: bool



    model_config = ConfigDict(
        from_attributes=True
    )



# ==========================================================
# VIEW
# ==========================================================

class ViewDefinition(BaseModel):

    id: int

    view_code: str

    view_name: str

    view_type: str



    title: str | None = None

    description: str | None = None

    icon: str | None = None



    display_order: int


    is_default: bool

    is_active: bool



    components: list[ViewComponentDefinition] = Field(
        default_factory=list
    )



    model_config = ConfigDict(
        from_attributes=True
    )



# ==========================================================
# WORKFLOW
# ==========================================================

class WorkflowDefinition(BaseModel):

    id: int


    model_config = ConfigDict(
        from_attributes=True
    )



# ==========================================================
# PERMISSION
# ==========================================================

class PermissionDefinition(BaseModel):

    id: int

    role_name: str

    can_view: bool = True

    can_create: bool = False

    can_edit: bool = False

    can_delete: bool = False

    can_export: bool = False

    can_import: bool = False

    can_approve: bool = False


    model_config = ConfigDict(
        from_attributes=True
    )


# ==========================================================
# DASHBOARD
# ==========================================================

class DashboardDefinition(BaseModel):

    id: int


    model_config = ConfigDict(
        from_attributes=True
    )



# ==========================================================
# REPORT
# ==========================================================

class ReportDefinition(BaseModel):

    id: int


    model_config = ConfigDict(
        from_attributes=True
    )



# ==========================================================
# COMPLETE RUNTIME
# ==========================================================

class RuntimeDefinition(BaseModel):

    module: ModuleDefinition


    fields: list[FieldDefinition] = Field(
        default_factory=list
    )


    layout: list[LayoutDefinition] = Field(
        default_factory=list
    )


    views: list[ViewDefinition] = Field(
        default_factory=list
    )


    workflow: list[WorkflowDefinition] = Field(
        default_factory=list
    )


    permissions: list[PermissionDefinition] = Field(
        default_factory=list
    )


    dashboard: list[DashboardDefinition] = Field(
        default_factory=list
    )


    reports: list[ReportDefinition] = Field(
        default_factory=list
    )


    errors: list[str] = Field(
        default_factory=list
    )


    model_config = ConfigDict(
        from_attributes=True
    )