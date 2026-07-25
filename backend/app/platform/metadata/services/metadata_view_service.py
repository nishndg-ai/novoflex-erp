from sqlalchemy.orm import Session

from app.platform.metadata.models.metadata_view import MetadataView
from app.platform.metadata.repository.metadata_view_repository import (
    metadata_view_repository,
)
from app.platform.metadata.schemas.metadata_view import (
    MetadataViewCreate,
    MetadataViewUpdate,
)


class MetadataViewService:

    def get_all(
        self,
        db: Session,
    ):
        return metadata_view_repository.get_all(db)

    def get_by_id(
        self,
        db: Session,
        view_id: int,
    ):
        return metadata_view_repository.get_by_id(
            db,
            view_id,
        )

    def get_by_code(
        self,
        db: Session,
        module_id: int,
        view_code: str,
    ):
        return metadata_view_repository.get_by_code(
            db,
            module_id,
            view_code,
        )

    def create(
        self,
        db: Session,
        view: MetadataViewCreate,
    ):
        db_obj = MetadataView(**view.model_dump())
        return metadata_view_repository.create(
            db,
            db_obj,
        )

    def update(
        self,
        db: Session,
        view_id: int,
        view: MetadataViewUpdate,
    ):
        db_obj = metadata_view_repository.get_by_id(
            db,
            view_id,
        )

        if db_obj is None:
            return None

        for key, value in view.model_dump(
            exclude_unset=True
        ).items():
            setattr(db_obj, key, value)

        return metadata_view_repository.update(
            db,
            db_obj,
        )

    def delete(
        self,
        db: Session,
        view_id: int,
    ):
        return metadata_view_repository.soft_delete(
            db,
            view_id,
        )


metadata_view_service = MetadataViewService()