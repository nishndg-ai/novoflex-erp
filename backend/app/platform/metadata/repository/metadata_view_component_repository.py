from sqlalchemy.orm import Session

from app.platform.metadata.models.metadata_view_component import (
    MetadataViewComponent,
)


class MetadataViewComponentRepository:

    def get_all(
        self,
        db: Session,
    ):
        return (
            db.query(MetadataViewComponent)
            .filter(MetadataViewComponent.is_active == True)
            .order_by(
                MetadataViewComponent.display_order,
            )
            .all()
        )

    def get_by_id(
        self,
        db: Session,
        component_id: int,
    ):
        return (
            db.query(MetadataViewComponent)
            .filter(
                MetadataViewComponent.id == component_id,
                MetadataViewComponent.is_active == True,
            )
            .first()
        )

    def get_by_view(
        self,
        db: Session,
        view_id: int,
    ):
        return (
            db.query(MetadataViewComponent)
            .filter(
                MetadataViewComponent.view_id == view_id,
                MetadataViewComponent.is_active == True,
            )
            .order_by(
                MetadataViewComponent.display_order,
            )
            .all()
        )

    def create(
        self,
        db: Session,
        db_obj: MetadataViewComponent,
    ):
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self,
        db: Session,
        db_obj: MetadataViewComponent,
    ):
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def soft_delete(
        self,
        db: Session,
        component_id: int,
    ):
        db_obj = self.get_by_id(
            db,
            component_id,
        )

        if db_obj is None:
            return None

        db_obj.is_active = False

        db.commit()

        return {
            "message": "Metadata View Component deleted successfully."
        }


metadata_view_component_repository = MetadataViewComponentRepository()