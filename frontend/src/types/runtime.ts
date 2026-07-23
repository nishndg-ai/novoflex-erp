export interface RuntimeModule {
    id: number;
    module_code: string;
    module_name: string;
    display_name: string;
    description: string;
    application: string;
    category: string;
    route: string;
    icon: string;
    menu_order: number;
    table_name: string;
    api_endpoint: string;
    page_size: number;
    supports_excel: boolean;
    supports_workflow: boolean;
    supports_dashboard: boolean;
    supports_ai: boolean;
    is_system: boolean;
}

export interface RuntimeField {
    id: number;
    field_name: string;
    display_name: string;
    data_type: string;
    control_type: string;
    display_order: number;
    is_required: boolean;
    is_unique: boolean;
    is_visible: boolean;
    is_editable: boolean;
    is_primary: boolean;
    length: number;
    decimal_places: number;
    default_value: unknown;
    validation_rules: unknown[];
}

export interface RuntimeLayout {
    id: number;
    row_no: number;
    column_no: number;
    column_span: number;
    field_name: string;
}

export interface RuntimeMetadata {
    module: RuntimeModule;
    fields: RuntimeField[];
    layout: RuntimeLayout[];
    workflow: unknown[];
    permissions: unknown[];
    dashboard: unknown[];
    reports: unknown[];
    errors?: string[];
}