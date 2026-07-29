from sqlalchemy.orm import Session


from app.platform.metadata.models.metadata_permission import (
    MetadataPermission,
)


from app.platform.metadata.models.metadata_module import (
    MetadataModule,
)



class PermissionService:


    def get_role_permissions(
        self,
        db: Session,
        role_name: str,
    ):


        permissions = (

            db.query(
                MetadataPermission
            )

            .join(
                MetadataModule,
                MetadataPermission.module_id
                ==
                MetadataModule.id
            )

            .filter(
                MetadataPermission.role_name
                ==
                role_name
            )

            .filter(
                MetadataPermission.is_active
                ==
                True
            )

            .all()

        )


        return [

            {

                "module_id":
                    permission.module_id,


                "module_code":
                    permission.module.module_code
                    if permission.module
                    else None,


                "module_name":
                    permission.module.module_name
                    if permission.module
                    else None,


                "display_name":
                    permission.module.display_name
                    if permission.module
                    else None,


                "can_view":
                    permission.can_view,


                "can_create":
                    permission.can_create,


                "can_edit":
                    permission.can_edit,


                "can_delete":
                    permission.can_delete,


                "can_export":
                    permission.can_export,


                "can_import":
                    permission.can_import,


                "can_approve":
                    permission.can_approve,

            }

            for permission in permissions

        ]