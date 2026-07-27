from datetime import datetime, UTC

from sqlalchemy import (
    Column,
    Integer,
    String,
    JSON,
    DateTime,
)

from app.database.base import Base


class AuditLog(Base):

    __tablename__ = "audit_log"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    module = Column(
        String(100),
        nullable=False
    )


    action = Column(
        String(50),
        nullable=False
    )


    record_id = Column(
        Integer,
        nullable=True
    )


    user = Column(
        String(100),
        nullable=True
    )


    old_data = Column(
        JSON,
        nullable=True
    )


    new_data = Column(
        JSON,
        nullable=True
    )


    created_at = Column(
        DateTime,
        default=lambda:
            datetime.now(UTC)
    )