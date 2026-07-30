from sqlalchemy.orm import Session

from app.platform.metadata.models.metadata_permission import (
    MetadataPermission,
)


class ModuleProvisioningService:
    """
    Automatic setup of common BLUISH platform features
    when a new module is created.
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


        db.commit()



module_provisioning_service = ModuleProvisioningService()