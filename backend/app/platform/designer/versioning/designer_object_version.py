from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime,
    JSON,
)


from app.database.base import Base




class DesignerObjectVersion(Base):
    """
    BLUISH Designer Object Version

    Maintains version history of dynamically
    created ERP objects.

    Lifecycle:

        CREATE
          |
          ↓
        DRAFT
          |
          ↓
       APPROVED
          |
          ↓
        APPLIED


    Example:

        Customer Master

        Version 1:
            customer_code
            customer_name


        Version 2:
            customer_code
            customer_name
            gst_no
    """



    __tablename__ = "designer_object_versions"



    id = Column(

        Integer,

        primary_key=True,

        index=True,

    )



    # =====================================================
    # OBJECT REFERENCE
    # =====================================================


    module_id = Column(

        Integer,

        nullable=False,

        index=True,

    )



    version_no = Column(

        Integer,

        nullable=False,

    )



    # =====================================================
    # CHANGE INFORMATION
    # =====================================================


    change_type = Column(

        String(50),

        nullable=False,

        default="CREATE",

    )


    description = Column(

        Text,

        nullable=True,

    )



    # =====================================================
    # OBJECT SNAPSHOT
    # =====================================================


    definition = Column(

        JSON,

        nullable=False,

    )



    # =====================================================
    # VERSION STATUS
    # =====================================================


    status = Column(

        String(30),

        nullable=False,

        default="DRAFT",

    )



    # =====================================================
    # AUDIT
    # =====================================================


    created_by = Column(

        String(100),

        nullable=True,

    )


    approved_by = Column(

        String(100),

        nullable=True,

    )


    created_at = Column(

        DateTime,

        default=datetime.utcnow,

    )


    updated_at = Column(

        DateTime,

        default=datetime.utcnow,

        onupdate=datetime.utcnow,

    )