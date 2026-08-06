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


from app.platform.metadata.models.metadata_menu import (
    MetadataMenu,
)


from app.platform.metadata.enums import (
    ViewType,
)


from app.platform.schema_engine.schema_generator import (
    SchemaGenerator,
)


from app.platform.metadata.services.metadata_menu_service import (
    metadata_menu_service,
)





class ModuleProvisioningService:
    """
    BLUISH Module Provisioning Engine

    Creates platform capabilities for dynamic objects.

    STANDARD:
        - Permissions
        - Views
        - Default Fields
        - Database Table
        - Menu


    DESIGNER:
        - Permissions
        - Views
        - User Fields
        - Database Table
        - Menu

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
    # PERMISSIONS
    # =====================================================


    def provision_permissions(
        self,
        db: Session,
        module_id: int,
    ):


        for role in self.DEFAULT_ROLES:


            db.add(

                MetadataPermission(

                    module_id=module_id,

                    **role,

                )

            )





    # =====================================================
    # VIEWS
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
    # DEFAULT FIELDS
    # =====================================================


    def provision_default_fields(
        self,
        db: Session,
        module_id: int,
    ):


        for field in self.DEFAULT_FIELDS:


            db.add(

                MetadataField(

                    module_id=module_id,

                    **field,

                )

            )







    # =====================================================
    # DATABASE SCHEMA
    # =====================================================


    def provision_schema(
        self,
        db: Session,
        module_id: int,
    ):


        generator = SchemaGenerator(db)


        return generator.generate_table(
            module_id
        )







    # =====================================================
    # MENU PROVISIONING
    # =====================================================


    def provision_menu(
        self,
        db: Session,
        module,
    ):


        menu = MetadataMenu(

            menu_code=module.module_code.upper(),

            menu_name=module.module_code,

            display_name=module.module_name,

            description=module.description,

            menu_type="PAGE",

            module_id=module.id,

            route=module.route,

            menu_order=0,

            is_visible=True,

            is_active=True,

            version=1,

        )


        metadata_menu_service.create_menu(

            db,

            menu,

        )







    # =====================================================
    # MAIN PROVISION METHOD
    # =====================================================


    def provision_module(
        self,
        db: Session,
        module,
        mode: str = "STANDARD",
    ):


        self.provision_permissions(

            db,

            module.id,

        )



        self.provision_views(

            db,

            module.id,

            module.module_code,

            module.module_name,

        )



        if mode == "STANDARD":


            self.provision_default_fields(

                db,

                module.id,

            )


        elif mode == "DESIGNER":

            pass


        else:


            raise ValueError(

                f"Invalid provisioning mode: {mode}"

            )




        db.flush()



        self.provision_schema(

            db,

            module.id,

        )



        # BLUISH AUTO MENU CREATION

        self.provision_menu(

            db,

            module,

        )



        db.commit()





module_provisioning_service = ModuleProvisioningService()