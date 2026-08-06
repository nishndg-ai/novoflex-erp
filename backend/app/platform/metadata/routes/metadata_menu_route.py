from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
)

from sqlalchemy.orm import Session


from app.database.database import get_db


from app.platform.metadata.models.metadata_menu import (
    MetadataMenu,
)


from app.platform.metadata.services.metadata_menu_service import (
    metadata_menu_service,
)



router = APIRouter(
    prefix="/metadata/menu",
    tags=["Metadata Menu"],
)



# ==========================================================
# GET MENU TREE
# ==========================================================

@router.get(
    "/tree",
)
def get_menu_tree(
    db: Session = Depends(get_db),
):

    return metadata_menu_service.get_menu_tree(
        db
    )



# ==========================================================
# CREATE MENU
# ==========================================================

@router.post(
    "/",
)
def create_menu(
    data: dict,
    db: Session = Depends(get_db),
):


    menu = MetadataMenu(

        menu_code=data.get(
            "menu_code"
        ),

        menu_name=data.get(
            "menu_name"
        ),

        display_name=data.get(
            "display_name"
        ),

        description=data.get(
            "description"
        ),

        menu_type=data.get(
            "menu_type",
            "GROUP",
        ),

        parent_id=data.get(
            "parent_id"
        ),

        module_id=data.get(
            "module_id"
        ),

        route=data.get(
            "route"
        ),

        icon=data.get(
            "icon"
        ),

        menu_order=data.get(
            "menu_order",
            0,
        ),

    )


    try:

        return metadata_menu_service.create_menu(
            db,
            menu,
        )


    except ValueError as ex:

        raise HTTPException(
            status_code=400,
            detail=str(ex),
        )



# ==========================================================
# GET MENU BY ID
# ==========================================================

@router.get(
    "/{menu_id}",
)
def get_menu(
    menu_id: int,
    db: Session = Depends(get_db),
):

    menu = metadata_menu_service.get_menu(
        db,
        menu_id,
    )


    if menu is None:

        raise HTTPException(
            status_code=404,
            detail="Menu not found",
        )


    return menu



# ==========================================================
# DELETE MENU
# ==========================================================

@router.delete(
    "/{menu_id}",
)
def delete_menu(
    menu_id: int,
    db: Session = Depends(get_db),
):

    menu = metadata_menu_service.delete_menu(
        db,
        menu_id,
    )


    if menu is None:

        raise HTTPException(
            status_code=404,
            detail="Menu not found",
        )


    return {

        "message":
            "Menu deleted successfully"

    }