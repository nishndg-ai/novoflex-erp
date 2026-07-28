from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    Text,
)

from app.database.base import Base



class ImportLog(Base):

    __tablename__ = "import_log"


    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )


    batch_no = Column(
        String(50),
        unique=True,
        nullable=False,
    )


    module = Column(
        String(100),
        nullable=False,
    )


    file_name = Column(
        String(255),
        nullable=False,
    )


    total_rows = Column(
        Integer,
        default=0,
    )


    success_rows = Column(
        Integer,
        default=0,
    )


    failed_rows = Column(
        Integer,
        default=0,
    )


    status = Column(
        String(50),
        default="STARTED",
    )


    error_summary = Column(
        Text,
        nullable=True,
    )


    user = Column(
        String(100),
        default="system",
    )


    started_at = Column(
        DateTime,
        default=datetime.utcnow,
    )


    completed_at = Column(
        DateTime,
        nullable=True,
    )


    duration_seconds = Column(
        Integer,
        nullable=True,
    )