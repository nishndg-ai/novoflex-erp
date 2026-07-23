from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Integer,
    String,
    func,
)


from app.database.base import Base


class BaseModel(Base):
    __abstract__ = True

    # ==========================================
    # Primary Key
    # ==========================================
    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    # ==========================================
    # Master Fields
    # ==========================================
    code = Column(
        String(30),
        unique=True,
        nullable=False,
        index=True,
    )

    name = Column(
        String(200),
        nullable=False,
        index=True,
    )

    description = Column(
        String(500),
        nullable=True,
    )

    remarks = Column(
        String(1000),
        nullable=True,
    )

    is_active = Column(
        Boolean,
        default=True,
        nullable=False,
    )

    # ==========================================
    # Audit Fields
    # ==========================================
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )

    created_by = Column(
        Integer,
        nullable=True,
    )

    updated_by = Column(
        Integer,
        nullable=True,
    )

    deleted_at = Column(
        DateTime(timezone=True),
        nullable=True,
    )

    deleted_by = Column(
        Integer,
        nullable=True,
    )

    # ==========================================
    # Version Control
    # ==========================================
    version = Column(
        Integer,
        default=1,
        nullable=False,
    )