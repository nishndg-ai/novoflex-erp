from sqlalchemy.orm import Session

from app.platform.metadata.repository.metadata_repository import (
    metadata_repository,
)
from app.platform.metadata.repository.metadata_field_repository import (
    metadata_field_repository,
)
from app.platform.metadata.repository.metadata_layout_repository import (
    metadata_layout_repository,
)
from app.platform.metadata.schemas.metadata_builder_schema import (
    MetadataBuilderResponse,
)


class MetadataBuilderService:
    def get_builder(self, db: Session, module_id: int):
        module = metadata_repository.get_by_id(db, module_id)

        if not module:
            return None

        fields = [
            field
            for field in metadata_field_repository.get_all(db)
            if field.module_id == module_id
        ]

        layouts = [
            layout
            for layout in metadata_layout_repository.get_all(db)
            if layout.module_id == module_id
        ]

        return MetadataBuilderResponse(
            module=module,
            fields=fields,
            layouts=layouts,
        )


metadata_builder_service = MetadataBuilderService()