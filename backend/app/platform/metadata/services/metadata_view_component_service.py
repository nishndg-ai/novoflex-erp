from sqlalchemy.orm import Session

from app.platform.metadata.models.metadata_view_component import (
    MetadataViewComponent,
)
from app.platform.metadata.repository.metadata_view_component_repository import (
    metadata_view_component_repository,
)
from app.platform.metadata.schemas.metadata_view_component import (
    MetadataViewComponentCreate,
    MetadataViewComponentUpdate,
)


class MetadataViewComponentService:

    def get_all(
        self,
        db: Session,
    ):
        return metadata_view_component_repository.get_all(db)

    def get_by_id(
        self,
        db: Session,
        component_id: int,
    ):
        return metadata_view_component_repository.get_by_id(
            db,
            component_id,
        )

    def get_by_view(
        self,
        db: Session,
        view_id: int,
    ):
        return metadata_view_component_repository.get_by_view(
            db,
            view_id,
        )

    def create(
        self,
        db: Session,
        component: MetadataViewComponentCreate,
    ):
        db_obj = MetadataViewComponent(
            **component.model_dump()
        )

        return metadata_view_component_repository.create(
            db,
            db_obj,
        )

    def update(
        self,
        db: Session,
        component_id: int,
        component: MetadataViewComponentUpdate,
    ):
        db_obj = metadata_view_component_repository.get_by_id(
            db,
            component_id,
        )

        if db_obj is None:
            return None

        for key, value in component.model_dump(
            exclude_unset=True
        ).items():
            setattr(db_obj, key, value)

        return metadata_view_component_repository.update(
            db,
            db_obj,
        )

    def delete(
        self,
        db: Session,
        component_id: int,
    ):
        return metadata_view_component_repository.soft_delete(
            db,
            component_id,
        )


metadata_view_component_service = MetadataViewComponentService()