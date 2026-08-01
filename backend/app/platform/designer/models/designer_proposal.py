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





class DesignerProposal(Base):
    """
    BLUISH Designer Proposal

    Stores proposed ERP objects before approval.

    Lifecycle:

        DRAFT
          |
          ↓
        APPROVED
          |
          ↓
        CREATED

    or

        REJECTED
    """



    __tablename__ = "designer_proposals"



    id = Column(

        Integer,

        primary_key=True,

        index=True,

    )



    # =====================================================
    # OBJECT INFORMATION
    # =====================================================


    object_name = Column(

        String(150),

        nullable=False,

    )


    description = Column(

        Text,

        nullable=True,

    )



    application = Column(

        String(50),

        nullable=False,

    )



    category = Column(

        String(50),

        nullable=False,

    )



    # =====================================================
    # SOURCE
    # =====================================================


    source = Column(

        String(50),

        nullable=False,

        default="MANUAL",

    )



    # =====================================================
    # DESIGN DEFINITION
    # =====================================================


    definition = Column(

        JSON,

        nullable=False,

    )



    # =====================================================
    # WORKFLOW STATUS
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