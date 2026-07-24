from sqlalchemy.orm import Session

from app.platform.metadata.repository.metadata_field_repository import (
    metadata_field_repository,
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
        field,
    ):
        return metadata_field_repository.create(
            db,
            field,
        )

    def update(
        self,
        db: Session,
        field,
    ):
        return metadata_field_repository.update(
            db,
            field,
        )

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