from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Integer,
    String,
    ForeignKey,
)

from sqlalchemy.orm import relationship

from app.database.base import Base



class MetadataMenu(Base):

    __tablename__ = "metadata_menus"


    # ==========================================================
    # Identity
    # ==========================================================

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )


    # ==========================================================
    # Hierarchy
    # ==========================================================

    parent_id = Column(
        Integer,
        ForeignKey(
            "metadata_menus.id"
        ),
        nullable=True,
    )


    parent = relationship(
        "MetadataMenu",
        remote_side=[id],
        backref="children",
    )



    # ==========================================================
    # Menu Information
    # ==========================================================

    menu_code = Column(
        String(100),
        unique=True,
        nullable=False,
        index=True,
    )


    menu_name = Column(
        String(150),
        nullable=False,
    )


    display_name = Column(
        String(150),
        nullable=False,
    )


    description = Column(
        String(500),
        nullable=True,
    )



    # ==========================================================
    # Menu Type
    # ==========================================================
    #
    # GROUP  -> Folder only
    # PAGE   -> Custom page
    # MODULE -> Runtime module link
    #

    menu_type = Column(
        String(50),
        nullable=False,
        default="GROUP",
    )



    # ==========================================================
    # Module Link
    # ==========================================================

    module_id = Column(
        Integer,
        ForeignKey(
            "metadata_modules.id"
        ),
        nullable=True,
    )


    module = relationship(
        "MetadataModule"
    )



    # ==========================================================
    # Navigation
    # ==========================================================

    route = Column(
        String(200),
        nullable=True,
    )


    icon = Column(
        String(100),
        nullable=True,
    )


    menu_order = Column(
        Integer,
        default=0,
    )



    # ==========================================================
    # Security
    # ==========================================================

    is_visible = Column(
        Boolean,
        default=True,
    )


    # ==========================================================
    # Audit
    # ==========================================================

    is_active = Column(
        Boolean,
        default=True,
    )


    created_at = Column(
        DateTime
    )


    updated_at = Column(
        DateTime
    )


    created_by = Column(
        String(100)
    )


    updated_by = Column(
        String(100)
    )


    version = Column(
        Integer,
        default=1,
    )