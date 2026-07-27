from sqlalchemy.orm import Session

from app.platform.metadata.models.metadata_view_component import (
    MetadataViewComponent,
)

from app.platform.runtime.types import ViewComponentDefinition



class ViewComponentLoader:
    """
    Loads runtime view component definitions for all
    views belonging to a module.
    """

    @staticmethod
    def load_view_components(
        db: Session,
        module_id: int,
    ) -> list[ViewComponentDefinition]:


        components = (

            db.query(MetadataViewComponent)

            .join(
                MetadataViewComponent.view,
            )

            .filter(

                MetadataViewComponent.view.has(
                    module_id=module_id,
                ),

                MetadataViewComponent.is_visible.is_(True),

            )

            .order_by(

                MetadataViewComponent.display_order,

                MetadataViewComponent.id,

            )

            .all()

        )



        runtime_components: list[ViewComponentDefinition] = []



        for component in components:


            runtime_components.append(

                ViewComponentDefinition(


                    id=component.id,


                    view_id=component.view_id,


                    component_type=
                        component.component_type,


                    component_key=
                        component.component_name,


                    title=
                        component.display_name,


                    field_name=(

                        component.field.field_name

                        if component.field

                        else None

                    ),



                    row_no=
                        component.row_no,


                    column_no=
                        component.column_no,


                    column_span=
                        component.column_span,



                    width=None,


                    height=None,



                    # IMPORTANT
                    # Sends database properties
                    # to frontend
                    properties=
                        component.properties,



                    # Legacy support
                    config=None,



                    display_order=
                        component.display_order,


                    is_visible=
                        component.is_visible,


                )

            )



        return runtime_components