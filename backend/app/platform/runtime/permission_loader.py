from sqlalchemy.orm import Session

from app.platform.runtime.types import PermissionDefinition

from app.platform.metadata.models.metadata_permission import (
    MetadataPermission,
)



class PermissionLoader:
    """
    Loads permission definitions for a module.
    """

    @staticmethod
    def load_permissions(
        db: Session,
        module_id: int,
    ) -> list[PermissionDefinition]:

        permissions = (
            db.query(MetadataPermission)
            .filter(
                MetadataPermission.module_id == module_id
            )
            .all()
        )


        print(
            "DEBUG PERMISSIONS:",
            module_id,
            len(permissions)
        )


        result = []


        for permission in permissions:

            print(
                "DEBUG ROLE:",
                permission.role_name
            )


            result.append(

                PermissionDefinition(

                    id=permission.id,

                    role_name=permission.role_name,

                    can_view=permission.can_view,

                    can_create=permission.can_create,

                    can_edit=permission.can_edit,

                    can_delete=permission.can_delete,

                    can_export=permission.can_export,

                    can_import=permission.can_import,

                    can_approve=permission.can_approve,

                )

            )


        return result