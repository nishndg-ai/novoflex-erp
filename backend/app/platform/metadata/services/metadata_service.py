from sqlalchemy.orm import Session

from app.platform.metadata.models.metadata_module import MetadataModule
from app.platform.metadata.repository.metadata_repository import (
    MetadataRepository,
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
        return self.repository.get_system_modules(db)

    def get_user_modules(
        self,
        db: Session,
    ):
        return self.repository.get_user_modules(db)

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

        return self.repository.create(
            db,
            module,
        )

    def update_module(
        self,
        db: Session,
        module: MetadataModule,
    ):
        return self.repository.update(
            db,
            module,
        )

    def delete_module(
        self,
        db: Session,
        record_id: int,
    ):
        return self.repository.soft_delete(
            db,
            record_id,
        )

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