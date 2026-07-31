from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Integer,
    String,
    Text,
)

from app.database.base import Base



class MetadataModule(Base):

    __tablename__ = "metadata_modules"


    # ==========================================================
    # Identity
    # ==========================================================

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )


    # ==========================================================
    # Module Information
    # ==========================================================

    module_code = Column(
        String(50),
        unique=True,
        nullable=False,
        index=True,
    )


    module_name = Column(
        String(100),
        nullable=False,
    )


    display_name = Column(
        String(150),
        nullable=False,
    )


    description = Column(
        Text
    )


    application = Column(
        String(100),
        nullable=False,
    )


    category = Column(
        String(100),
        nullable=False,
    )



    # ==========================================================
    # Navigation
    # ==========================================================

    route = Column(
        String(200),
        nullable=False,
    )


    icon = Column(
        String(100)
    )


    menu_order = Column(
        Integer,
        default=0,
    )



    # ==========================================================
    # Runtime
    # ==========================================================

    table_name = Column(
        String(100),
        nullable=False,
    )


    api_endpoint = Column(
        String(200),
        nullable=False,
    )


    page_size = Column(
        Integer,
        default=20,
    )


    # ==========================================================
    # Data Security Scope
    # ==========================================================
    #
    # GLOBAL  -> No restriction
    # COMPANY -> Filter by company_id
    # PLANT   -> Filter by plant_id
    #

    data_scope = Column(
        String(50),
        default="GLOBAL",
    )



    # ==========================================================
    # Features
    # ==========================================================

    supports_excel = Column(
        Boolean,
        default=True,
    )


    supports_workflow = Column(
        Boolean,
        default=False,
    )


    supports_dashboard = Column(
        Boolean,
        default=False,
    )


    supports_ai = Column(
        Boolean,
        default=False,
    )


    is_system = Column(
        Boolean,
        default=False,
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