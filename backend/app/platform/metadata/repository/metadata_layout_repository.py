from sqlalchemy.orm import Session

from app.platform.metadata.models.metadata_layout import MetadataLayout
from app.repositories.base_repository import BaseRepository


class MetadataLayoutRepository(BaseRepository[MetadataLayout]):

    def __init__(self):
        super().__init__(MetadataLayout)

    def get_layouts_by_module(
        self,
        db: Session,
        module_id: int,
    ):
        return (
            db.query(MetadataLayout)
            .filter(
                MetadataLayout.module_id == module_id,
                MetadataLayout.is_active.is_(True),
            )
            .order_by(
                MetadataLayout.row_no,
                MetadataLayout.column_no,
            )
            .all()
        )


metadata_layout_repository = MetadataLayoutRepository()