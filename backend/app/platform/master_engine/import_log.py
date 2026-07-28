from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
)

from app.database.base import Base


class ImportLog(Base):

    __tablename__ = "import_log"


    id = Column(
        Integer,
        primary_key=True,
        index=True,
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


    user = Column(
        String(100),
        default="system",
    )


    created_at = Column(
        DateTime,
        default=datetime.utcnow,
    )