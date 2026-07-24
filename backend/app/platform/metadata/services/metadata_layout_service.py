from sqlalchemy.orm import Session

from app.platform.metadata.models.metadata_layout import MetadataLayout
from app.platform.metadata.schemas.metadata_layout_schema import (
    MetadataLayoutCreate,
    MetadataLayoutUpdate,
)
from app.platform.metadata.repository.metadata_layout_repository import (
    metadata_layout_repository,
)


class MetadataLayoutService:
    def get_all(self, db: Session):
        return metadata_layout_repository.get_all(db)

    def get_by_id(self, db: Session, layout_id: int):
        return metadata_layout_repository.get_by_id(db, layout_id)

    def create(self, db: Session, layout: MetadataLayoutCreate):
        db_obj = MetadataLayout(**layout.model_dump())
        return metadata_layout_repository.create(db, db_obj)

    def update(
        self,
        db: Session,
        layout_id: int,
        layout: MetadataLayoutUpdate,
    ):
        db_obj = metadata_layout_repository.get_by_id(db, layout_id)

        if not db_obj:
            return None

        for key, value in layout.model_dump(exclude_unset=True).items():
            setattr(db_obj, key, value)

        db.commit()
        db.refresh(db_obj)

        return db_obj

    def delete(self, db: Session, layout_id: int):
        db_obj = metadata_layout_repository.get_by_id(db, layout_id)

        if not db_obj:
            return None

        db.delete(db_obj)
        db.commit()

        return True


metadata_layout_service = MetadataLayoutService()