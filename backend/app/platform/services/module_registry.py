from sqlalchemy.orm import Session

from app.platform.metadata.models.metadata_module import MetadataModule


class ModuleRegistry:

    @staticmethod
    def get_all_modules(db: Session):
        return (
            db.query(MetadataModule)
            .filter(MetadataModule.is_active == 1)
            .order_by(MetadataModule.menu_order)
            .all()
        )

    @staticmethod
    def get_module_by_code(db: Session, module_code: str):
        return (
            db.query(MetadataModule)
            .filter(MetadataModule.module_code == module_code)
            .first()
        )