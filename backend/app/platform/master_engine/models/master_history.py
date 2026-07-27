from datetime import datetime, UTC

from sqlalchemy import (
    Column,
    Integer,
    String,
    JSON,
    DateTime,
    Text,
)

from app.database.base import Base


class MasterHistory(Base):

    __tablename__ = "master_history"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    module = Column(
        String(100),
        nullable=False
    )


    record_id = Column(
        Integer,
        nullable=False
    )


    action = Column(
        String(50),
        nullable=False
    )


    old_data = Column(
        JSON,
        nullable=True
    )


    new_data = Column(
        JSON,
        nullable=True
    )


    reason = Column(
        Text,
        nullable=True
    )


    changed_by = Column(
        String(100),
        nullable=True
    )


    changed_at = Column(
        DateTime,
        default=lambda:
            datetime.now(UTC)
    )