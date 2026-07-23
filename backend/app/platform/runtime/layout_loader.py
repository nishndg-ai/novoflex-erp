from sqlalchemy.orm import Session

from app.platform.metadata.models.metadata_layout import MetadataLayout
from app.platform.runtime.types import LayoutDefinition


class LayoutLoader:
    """
    Loads runtime layout definitions for a module.
    """

    @staticmethod
    def load_layout(
        db: Session,
        module_id: int,
    ) -> list[LayoutDefinition]:

        layouts = (
            db.query(MetadataLayout)
            .filter(
                MetadataLayout.module_id == module_id,
                MetadataLayout.is_active.is_(True),
            )
            .order_by(
                MetadataLayout.row_no,
                MetadataLayout.column_no,
            )
            .all()
        )

        runtime_layouts: list[LayoutDefinition] = []

        for layout in layouts:

            runtime_layouts.append(
                LayoutDefinition(
                    id=layout.id,
                    row_no=layout.row_no,
                    column_no=layout.column_no,
                    column_span=layout.column_span,
                    field_name=layout.field.field_name,
                )
            )

        return runtime_layouts