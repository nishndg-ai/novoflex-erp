from sqlalchemy.orm import Session

from app.platform.metadata.models.metadata_field import MetadataField
from app.platform.runtime.types import FieldDefinition


class FieldLoader:
    """
    Loads runtime field definitions for a module.
    """

    @staticmethod
    def load_fields(
        db: Session,
        module_id: int,
    ) -> list[FieldDefinition]:

        fields = (
            db.query(MetadataField)
            .filter(
                MetadataField.module_id == module_id,
                MetadataField.is_active.is_(True),
            )
            .order_by(
                MetadataField.display_order,
                MetadataField.field_name,
            )
            .all()
        )

        runtime_fields: list[FieldDefinition] = []

        for field in fields:

            runtime_fields.append(
                FieldDefinition(
                    id=field.id,
                    field_name=field.field_name,
                    display_name=field.display_name,
                    data_type=field.data_type,
                    control_type=field.control_type,
                    display_order=field.display_order,
                    is_required=field.is_required,
                    is_unique=field.is_unique,
                    is_visible=field.is_visible,
                    is_editable=field.is_editable,
                    is_primary=field.is_primary,
                    length=field.length,
                    decimal_places=field.decimal_places,
                    default_value=field.default_value,
                    validation_rules=[],
                )
            )

        return runtime_fields