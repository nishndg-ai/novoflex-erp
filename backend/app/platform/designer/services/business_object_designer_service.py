from sqlalchemy.orm import Session


from app.platform.metadata.models.metadata_module import (
    MetadataModule,
)

from app.platform.metadata.models.metadata_field import (
    MetadataField,
)


from app.platform.metadata.services.metadata_service import (
    metadata_service,
)


from app.platform.metadata.services.module_provisioning_service import (
    module_provisioning_service,
)


from app.platform.designer.schemas.designer_schema import (
    BusinessObjectCreateRequest,
)


from app.platform.designer.services.designer_validation_service import (
    designer_validation_service,
)


from app.platform.designer.versioning.designer_version_service import (
    designer_version_service,
)





class BusinessObjectDesignerService:
    """
    BLUISH Business Object Designer

    Creates ERP objects dynamically from user definition.

    Flow:

        User Definition
              |
              ↓
        Validation Engine
              |
              ↓
        Metadata Module
              |
              ↓
        User Fields
              |
              ↓
        Designer Provisioning
              |
              ↓
        Version History
              |
              ↓
        Runtime ERP Object
    """



    def create_object(
        self,
        db: Session,
        request: BusinessObjectCreateRequest,
    ):



        # =====================================================
        # DESIGNER VALIDATION
        # =====================================================

        designer_validation_service.validate_object(

            db,

            request.object_name,

            request.fields,

        )



        module_code = (

            request.object_name

            .lower()

            .replace(

                " ",

                "_",

            )

        )



        module = MetadataModule(


            module_code=module_code,


            module_name=request.object_name,


            display_name=request.object_name,


            description=request.description,


            application=request.application,


            category=request.category,


            route=f"/{module_code}",


            table_name=module_code,


            api_endpoint=f"/runtime-data/{module_code}",


            page_size=20,


            supports_excel=request.features.excel_import,


            supports_workflow=request.features.workflow,


            supports_dashboard=request.features.dashboard,


            supports_ai=request.features.ai,


            is_system=False,


        )




        # =====================================================
        # CREATE MODULE WITHOUT AUTO PROVISION
        # =====================================================


        created_module = metadata_service.create_module(

            db,

            module,

            provision=False,

        )





        # =====================================================
        # CREATE USER DEFINED FIELDS
        # =====================================================


        for index, field in enumerate(

            request.fields,

            start=1,

        ):



            metadata_field = MetadataField(


                module_id=created_module.id,


                field_name=(

                    field.name

                    .lower()

                    .replace(

                        " ",

                        "_",

                    )

                ),


                display_name=field.label,


                data_type=field.data_type,


                control_type=field.control_type,


                length=field.length,


                is_required=field.required,


                is_unique=field.unique,


                show_in_grid=field.show_in_grid,


                is_searchable=field.searchable,


                is_filterable=field.filterable,


                display_order=index,


            )



            db.add(

                metadata_field

            )





        db.flush()





        # =====================================================
        # DESIGNER PROVISIONING
        # =====================================================


        module_provisioning_service.provision_module(

            db,

            created_module,

            mode="DESIGNER",

        )





        # =====================================================
        # CREATE INITIAL VERSION HISTORY
        # =====================================================


        designer_version_service.create_initial_version(

            db,

            created_module.id,

            request.model_dump(),

            created_by="SYSTEM",

        )





        return created_module





business_object_designer_service = (
    BusinessObjectDesignerService()
)