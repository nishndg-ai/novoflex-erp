from sqlalchemy.orm import Session

from app.platform.metadata.models.metadata_module import (
    MetadataModule,
)

from app.platform.metadata.repository.metadata_repository import (
    MetadataRepository,
)

from app.platform.metadata.services.module_provisioning_service import (
    module_provisioning_service,
)



class MetadataService:

    def __init__(self):

        self.repository = MetadataRepository()



    # ------------------------------------------------------------------
    # MODULES
    # ------------------------------------------------------------------

    def get_all_modules(
        self,
        db: Session,
    ):

        return self.repository.get_all(db)



    def get_module(
        self,
        db: Session,
        record_id: int,
    ):

        return self.repository.get_by_id(
            db,
            record_id,
        )



    def get_module_by_code(
        self,
        db: Session,
        module_code: str,
    ):

        return self.repository.get_module_by_code(
            db,
            module_code,
        )



    def get_system_modules(
        self,
        db: Session,
    ):

        return self.repository.get_system_modules(
            db
        )



    def get_user_modules(
        self,
        db: Session,
    ):

        return self.repository.get_user_modules(
            db
        )



    # ------------------------------------------------------------------
    # CREATE MODULE + BLUISH AUTO PROVISIONING
    # ------------------------------------------------------------------

    def create_module(
        self,
        db: Session,
        module: MetadataModule,
    ):


        if self.repository.exists(
            db,
            module_code=module.module_code,
        ):

            raise ValueError(
                f"Module '{module.module_code}' already exists."
            )



        # Create module registry entry

        created_module = self.repository.create(
            db,
            module,
        )



        # ==========================================================
        # BLUISH PLATFORM AUTO PROVISIONING
        # ==========================================================
        #
        # Whenever a user creates a new master/module:
        #
        # Item Master
        # Gauge Master
        # Specification Master
        #
        # BLUISH automatically creates:
        #
        # - Security permissions
        # - Future: menu
        # - Future: audit
        # - Future: workflow
        # - Future: reports
        #
        # ==========================================================


        module_provisioning_service.provision_permissions(
            db,
            created_module.id,
        )



        return created_module



    # ------------------------------------------------------------------
    # UPDATE MODULE
    # ------------------------------------------------------------------

    def update_module(
        self,
        db: Session,
        module: MetadataModule,
    ):

        return self.repository.update(
            db,
            module,
        )



    # ------------------------------------------------------------------
    # DELETE MODULE
    # ------------------------------------------------------------------

    def delete_module(
        self,
        db: Session,
        record_id: int,
    ):

        return self.repository.soft_delete(
            db,
            record_id,
        )



    # ------------------------------------------------------------------
    # RESTORE MODULE
    # ------------------------------------------------------------------

    def restore_module(
        self,
        db: Session,
        record_id: int,
    ):

        return self.repository.restore(
            db,
            record_id,
        )



metadata_service = MetadataService()