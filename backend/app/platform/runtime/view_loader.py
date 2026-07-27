from sqlalchemy.orm import Session

from app.platform.metadata.models.metadata_view import MetadataView
from app.platform.runtime.types import ViewDefinition


class ViewLoader:
    """
    Loads runtime view definitions for a module.
    """

    @staticmethod
    def load_views(
        db: Session,
        module_id: int,
    ) -> list[ViewDefinition]:

        views = (
            db.query(MetadataView)
            .filter(
                MetadataView.module_id == module_id,
                MetadataView.is_active.is_(True),
            )
            .all()
        )


        runtime_views: list[ViewDefinition] = []


        for view in views:

            runtime_views.append(

                ViewDefinition(

                    id=view.id,

                    view_code=view.view_code,

                    view_name=view.display_name,

                    view_type=view.view_type,

                    title=view.display_name,

                    description=view.description,

                    display_order=1,

                    is_default=view.is_default,

                    is_active=view.is_active,

                )

            )


        return runtime_views