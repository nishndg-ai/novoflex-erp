from sqlalchemy.orm import Session

from app.platform.metadata.models.metadata_menu import (
    MetadataMenu,
)



class MetadataMenuRepository:


    # ==========================================================
    # GET ALL ROOT MENUS
    # ==========================================================

    def get_root_menus(
        self,
        db: Session,
    ):

        return (

            db.query(
                MetadataMenu
            )

            .filter(
                MetadataMenu.parent_id == None
            )

            .filter(
                MetadataMenu.is_active == True
            )

            .order_by(
                MetadataMenu.menu_order
            )

            .all()

        )



    # ==========================================================
    # GET CHILD MENUS
    # ==========================================================

    def get_children(
        self,
        db: Session,
        parent_id: int,
    ):

        return (

            db.query(
                MetadataMenu
            )

            .filter(
                MetadataMenu.parent_id == parent_id
            )

            .filter(
                MetadataMenu.is_active == True
            )

            .order_by(
                MetadataMenu.menu_order
            )

            .all()

        )



    # ==========================================================
    # GET BY ID
    # ==========================================================

    def get_by_id(
        self,
        db: Session,
        record_id: int,
    ):

        return (

            db.query(
                MetadataMenu
            )

            .filter(
                MetadataMenu.id == record_id
            )

            .first()

        )



    # ==========================================================
    # CHECK DUPLICATE CODE
    # ==========================================================

    def exists(
        self,
        db: Session,
        menu_code: str,
    ):

        return (

            db.query(
                MetadataMenu
            )

            .filter(
                MetadataMenu.menu_code == menu_code
            )

            .first()

            is not None

        )



    # ==========================================================
    # CREATE
    # ==========================================================

    def create(
        self,
        db: Session,
        menu: MetadataMenu,
    ):

        db.add(
            menu
        )

        db.commit()

        db.refresh(
            menu
        )

        return menu



    # ==========================================================
    # UPDATE
    # ==========================================================

    def update(
        self,
        db: Session,
        menu: MetadataMenu,
    ):

        db.commit()

        db.refresh(
            menu
        )

        return menu



    # ==========================================================
    # SOFT DELETE
    # ==========================================================

    def soft_delete(
        self,
        db: Session,
        record_id: int,
    ):

        menu = self.get_by_id(
            db,
            record_id,
        )


        if menu:

            menu.is_active = False

            db.commit()


        return menu



metadata_menu_repository = MetadataMenuRepository()