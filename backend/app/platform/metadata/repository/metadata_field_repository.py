from sqlalchemy.orm import Session

from app.platform.metadata.models.metadata_field import MetadataField
from app.repositories.base_repository import BaseRepository


class MetadataFieldRepository(BaseRepository[MetadataField]):

    def __init__(self):
        super().__init__(MetadataField)

    def get_fields_by_module(
        self,
        db: Session,
        module_id: int,
    ):
        return (
            db.query(MetadataField)
            .filter(
                MetadataField.module_id == module_id,
                MetadataField.is_active.is_(True),
            )
            .order_by(MetadataField.display_order)
            .all()
        )


metadata_field_repository = MetadataFieldRepository()