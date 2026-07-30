from sqlalchemy.orm import Session

from app.platform.metadata.models.metadata_permission import (
    MetadataPermission,
)

from app.platform.metadata.models.metadata_view import (
    MetadataView,
)

from app.platform.metadata.models.metadata_field import (
    MetadataField,
)

from app.platform.metadata.enums import (
    ViewType,
)

from app.platform.schema_engine.schema_generator import (
    SchemaGenerator,
)



class ModuleProvisioningService:
    """
    BLUISH Module Provisioning Engine

    Automatically creates common platform
    capabilities whenever a new module is created.

    Features:
        - Permissions
        - Default Views
        - Default Fields
        - Dynamic Database Table

    Future:
        - Menu
        - Workflow
        - Reports
        - Notifications
        - AI Configuration
    """



    DEFAULT_ROLES = [

        {
            "role_name": "ADMIN",
            "can_view": True,
            "can_create": True,
            "can_edit": True,
            "can_delete": True,
            "can_export": True,
            "can_import": True,
            "can_approve": True,
        },

        {
            "role_name": "VIEWER",
            "can_view": True,
            "can_create": False,
            "can_edit": False,
            "can_delete": False,
            "can_export": False,
            "can_import": False,
            "can_approve": False,
        },

    ]



    DEFAULT_FIELDS = [

        {
            "field_name": "code",
            "display_name": "Code",
            "data_type": "string",
            "control_type": "TEXTBOX",
            "length": 100,
            "is_primary": False,
            "is_required": True,
            "is_unique": True,
            "display_order": 1,
            "show_in_grid": True,
            "grid_order": 1,
            "is_sortable": True,
            "is_filterable": True,
            "is_searchable": True,
        },

        {
            "field_name": "name",
            "display_name": "Name",
            "data_type": "string",
            "control_type": "TEXTBOX",
            "length": 150,
            "is_primary": False,
            "is_required": True,
            "is_unique": False,
            "display_order": 2,
            "show_in_grid": True,
            "grid_order": 2,
            "is_sortable": True,
            "is_filterable": True,
            "is_searchable": True,
        },

        {
            "field_name": "description",
            "display_name": "Description",
            "data_type": "string",
            "control_type": "TEXTAREA",
            "length": 500,
            "is_primary": False,
            "is_required": False,
            "is_unique": False,
            "display_order": 3,
            "show_in_grid": True,
            "grid_order": 3,
            "is_sortable": False,
            "is_filterable": False,
            "is_searchable": True,
        },

    ]



    # =====================================================
    # SECURITY PROVISIONING
    # =====================================================

    def provision_permissions(
        self,
        db: Session,
        module_id: int,
    ):

        for role in self.DEFAULT_ROLES:

            permission = MetadataPermission(
                module_id=module_id,
                **role,
            )

            db.add(permission)



    # =====================================================
    # VIEW PROVISIONING
    # =====================================================

    def provision_views(
        self,
        db: Session,
        module_id: int,
        module_code: str,
        module_name: str,
    ):

        views = [

            MetadataView(
                module_id=module_id,
                view_code=f"{module_code}_list",
                display_name=f"{module_name} List",
                description="Default grid view",
                view_type=ViewType.GRID,
                page_size=25,
                is_default=True,
            ),


            MetadataView(
                module_id=module_id,
                view_code=f"{module_code}_form",
                display_name=f"{module_name} Form",
                description="Default create/edit form",
                view_type=ViewType.FORM,
                page_size=1,
            ),


            MetadataView(
                module_id=module_id,
                view_code=f"{module_code}_detail",
                display_name=f"{module_name} Detail",
                description="Default detail view",
                view_type=ViewType.DETAIL,
                page_size=1,
            ),

        ]


        for view in views:

            db.add(view)



    # =====================================================
    # FIELD PROVISIONING
    # =====================================================

    def provision_fields(
        self,
        db: Session,
        module_id: int,
    ):

        for field in self.DEFAULT_FIELDS:

            metadata_field = MetadataField(
                module_id=module_id,
                **field,
            )

            db.add(metadata_field)



    # =====================================================
    # DATABASE TABLE PROVISIONING
    # =====================================================

    def provision_schema(
        self,
        db: Session,
        module_id: int,
    ):

        generator = SchemaGenerator(
            db
        )

        return generator.generate_table(
            module_id
        )



    # =====================================================
    # COMPLETE MODULE PROVISIONING
    # =====================================================

    def provision_module(
        self,
        db: Session,
        module,
    ):

        # Security

        self.provision_permissions(
            db,
            module.id,
        )


        # UI Views

        self.provision_views(
            db,
            module.id,
            module.module_code,
            module.module_name,
        )


        # Metadata Fields

        self.provision_fields(
            db,
            module.id,
        )


        # Save metadata first
        db.flush()


        # Physical Database Table

        self.provision_schema(
            db,
            module.id,
        )


        db.commit()



module_provisioning_service = ModuleProvisioningService()