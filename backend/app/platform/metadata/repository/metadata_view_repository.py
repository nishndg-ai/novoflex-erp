from sqlalchemy.orm import Session

from app.platform.metadata.models.metadata_view import MetadataView


class MetadataViewRepository:

    def get_all(
        self,
        db: Session,
    ):
        return (
            db.query(MetadataView)
            .filter(MetadataView.is_active == True)
            .order_by(MetadataView.display_name)
            .all()
        )

    def get_by_id(
        self,
        db: Session,
        view_id: int,
    ):
        return (
            db.query(MetadataView)
            .filter(
                MetadataView.id == view_id,
                MetadataView.is_active == True,
            )
            .first()
        )

    def get_by_code(
        self,
        db: Session,
        module_id: int,
        view_code: str,
    ):
        return (
            db.query(MetadataView)
            .filter(
                MetadataView.module_id == module_id,
                MetadataView.view_code == view_code,
                MetadataView.is_active == True,
            )
            .first()
        )

    def create(
        self,
        db: Session,
        db_obj: MetadataView,
    ):
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self,
        db: Session,
        db_obj: MetadataView,
    ):
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def soft_delete(
        self,
        db: Session,
        view_id: int,
    ):
        db_obj = self.get_by_id(
            db,
            view_id,
        )

        if db_obj is None:
            return None

        db_obj.is_active = False

        db.commit()

        return {
            "message": "Metadata View deleted successfully."
        }


metadata_view_repository = MetadataViewRepository()