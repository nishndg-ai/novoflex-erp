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

from app.platform.metadata.schemas.metadata_form_schema import (
    MetadataFormField,
    MetadataFormResponse,
)


class MetadataFormService:

    def get_form(
        self,
        db: Session,
        module_code: str,
    ):
        # Get module
        module = metadata_repository.get_module_by_code(
            db,
            module_code,
        )

        if module is None:
            return None

        # Get fields
        fields = metadata_field_repository.get_fields_by_module(
            db,
            module.id,
        )

        # Get layouts
        layouts = metadata_layout_repository.get_layouts_by_module(
            db,
            module.id,
        )

        # Create lookup dictionary
        layout_map = {
            layout.field_id: layout
            for layout in layouts
        }

        form_fields = []

        for field in fields:
            form_fields.append(
                MetadataFormField(
                    field=field,
                    layout=layout_map.get(field.id),
                )
            )

        return MetadataFormResponse(
            module=module,
            fields=form_fields,
        )


metadata_form_service = MetadataFormService()