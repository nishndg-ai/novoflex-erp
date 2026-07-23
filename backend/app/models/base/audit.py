from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Integer,
    func,
    text,
)

from app.database.base import Base


class AuditMixin(Base):
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
    # Status
    # ==========================================
    is_active = Column(
        Boolean,
        nullable=False,
        server_default=text("true"),
    )

    # ==========================================
    # Audit Fields
    # ==========================================
    created_at = Column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )

    updated_at = Column(
        DateTime(timezone=True),
        nullable=True,
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
    # Version
    # ==========================================
    version = Column(
        Integer,
        nullable=False,
        default=1,
    )