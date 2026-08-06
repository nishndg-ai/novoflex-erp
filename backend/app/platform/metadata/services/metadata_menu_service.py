from sqlalchemy.orm import Session

from app.platform.metadata.models.metadata_menu import (
    MetadataMenu,
)

from app.platform.metadata.repository.metadata_menu_repository import (
    metadata_menu_repository,
)



class MetadataMenuService:


    def __init__(self):

        self.repository = metadata_menu_repository



    # ==========================================================
    # BUILD MENU TREE
    # ==========================================================

    def build_tree(
        self,
        menus,
    ):

        result = []


        for menu in menus:

            item = {

                "id":
                    menu.id,

                "menu_code":
                    menu.menu_code,

                "menu_name":
                    menu.menu_name,

                "display_name":
                    menu.display_name,

                "menu_type":
                    menu.menu_type,

                "icon":
                    menu.icon,

                "route":
                    menu.route,

                "module_id":
                    menu.module_id,

                "menu_order":
                    menu.menu_order,

                "children":
                    self.build_tree(
                        menu.children
                    )
            }


            result.append(
                item
            )


        return result



    # ==========================================================
    # GET COMPLETE MENU TREE
    # ==========================================================

    def get_menu_tree(
        self,
        db: Session,
    ):

        root_menus = (

            self.repository.get_root_menus(
                db
            )

        )


        return self.build_tree(
            root_menus
        )



    # ==========================================================
    # CREATE MENU
    # ==========================================================

    def create_menu(
        self,
        db: Session,
        menu: MetadataMenu,
    ):


        if self.repository.exists(
            db,
            menu.menu_code,
        ):

            raise ValueError(
                f"Menu '{menu.menu_code}' already exists."
            )


        return self.repository.create(
            db,
            menu,
        )



    # ==========================================================
    # GET MENU BY ID
    # ==========================================================

    def get_menu(
        self,
        db: Session,
        record_id: int,
    ):

        return self.repository.get_by_id(
            db,
            record_id,
        )



    # ==========================================================
    # UPDATE MENU
    # ==========================================================

    def update_menu(
        self,
        db: Session,
        menu: MetadataMenu,
    ):

        return self.repository.update(
            db,
            menu,
        )



    # ==========================================================
    # DELETE MENU
    # ==========================================================

    def delete_menu(
        self,
        db: Session,
        record_id: int,
    ):

        return self.repository.soft_delete(
            db,
            record_id,
        )



metadata_menu_service = MetadataMenuService()