from sqlalchemy.orm import Session

from app.platform.metadata.models.metadata_module import MetadataModule
from app.repositories.base_repository import BaseRepository


class MetadataRepository(BaseRepository[MetadataModule]):

    def __init__(self):
        super().__init__(MetadataModule)

    def get_module_by_code(
        self,
        db: Session,
        module_code: str,
    ):
        return (
            db.query(MetadataModule)
            .filter(
                MetadataModule.module_code == module_code,
                MetadataModule.is_active.is_(True),
            )
            .first()
        )

    def get_system_modules(
        self,
        db: Session,
    ):
        return (
            db.query(MetadataModule)
            .filter(
                MetadataModule.is_system.is_(True),
                MetadataModule.is_active.is_(True),
            )
            .order_by(MetadataModule.display_order)
            .all()
        )

    def get_user_modules(
        self,
        db: Session,
    ):
        return (
            db.query(MetadataModule)
            .filter(
                MetadataModule.is_system.is_(False),
                MetadataModule.is_active.is_(True),
            )
            .order_by(MetadataModule.display_order)
            .all()
        )