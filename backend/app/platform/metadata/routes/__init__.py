from .metadata_builder_route import (
    router as metadata_builder_router,
)


from .metadata_field_route import (
    router as metadata_field_router,
)


from .metadata_form_route import (
    router as metadata_form_router,
)


from .metadata_layout_route import (
    router as metadata_layout_router,
)


from .metadata_route import (
    router as metadata_router,
)


from .metadata_view_route import (
    router as metadata_view_router,
)


from .metadata_view_component_route import (
    router as metadata_view_component_router,
)


from .metadata_menu_route import (
    router as metadata_menu_router,
)



# Backward compatibility
# Some platform routes expect "router"

router = metadata_router



__all__ = [

    "router",

    "metadata_router",

    "metadata_builder_router",

    "metadata_field_router",

    "metadata_form_router",

    "metadata_layout_router",

    "metadata_view_router",

    "metadata_view_component_router",

    "metadata_menu_router",

]