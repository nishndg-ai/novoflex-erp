from sqlalchemy.orm import Session

from app.platform.metadata.models.metadata_module import MetadataModule
from app.platform.runtime.types import ModuleDefinition


class ModuleLoader:
    """
    Loads module metadata and converts it into a Runtime ModuleDefinition.
    """

    @staticmethod
    def load(db: Session) -> list[ModuleDefinition]:
        modules = (
            db.query(MetadataModule)
            .filter(
                MetadataModule.is_active.is_(True)
            )
            .order_by(
                MetadataModule.menu_order,
                MetadataModule.module_name,
            )
            .all()
        )

        return [
            ModuleDefinition.model_validate(module)
            for module in modules
        ]

    @staticmethod
    def load_by_code(
        db: Session,
        module_code: str,
    ) -> ModuleDefinition | None:

        module = (
            db.query(MetadataModule)
            .filter(
                MetadataModule.module_code == module_code.lower(),
                MetadataModule.is_active.is_(True),
            )
            .first()
        )

        if module is None:
            return None

        return ModuleDefinition.model_validate(module)