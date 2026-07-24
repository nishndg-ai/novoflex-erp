from sqlalchemy.orm import Session

from app.platform.metadata.models.metadata_field import MetadataField
from app.platform.metadata.repository.metadata_field_repository import (
    metadata_field_repository,
)
from app.platform.metadata.schemas.metadata_field_schema import (
    MetadataFieldCreate,
    MetadataFieldUpdate,
)


class MetadataFieldService:

    def get_fields_by_module(
        self,
        db: Session,
        module_id: int,
    ):
        return metadata_field_repository.get_fields_by_module(
            db,
            module_id,
        )

    def create(
        self,
        db: Session,
        field: MetadataFieldCreate,
    ):
        db_obj = MetadataField(**field.model_dump())
        return metadata_field_repository.create(db, db_obj)

    def update(
        self,
        db: Session,
        field_id: int,
        field: MetadataFieldUpdate,
    ):
        db_obj = metadata_field_repository.get_by_id(db, field_id)

        if db_obj is None:
            return None

        for key, value in field.model_dump().items():
            setattr(db_obj, key, value)

        return metadata_field_repository.update(db, db_obj)

    def delete(
        self,
        db: Session,
        record_id: int,
    ):
        return metadata_field_repository.soft_delete(
            db,
            record_id,
        )


metadata_field_service = MetadataFieldService()