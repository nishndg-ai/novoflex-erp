from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime,
)

from app.database.base import Base



class ImportErrorDetail(Base):

    __tablename__ = "import_error_detail"


    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )


    batch_no = Column(
        String(50),
        nullable=False,
    )


    row_number = Column(
        Integer,
        nullable=False,
    )


    column_name = Column(
        String(100),
        nullable=True,
    )


    invalid_value = Column(
        Text,
        nullable=True,
    )


    error_message = Column(
        Text,
        nullable=False,
    )


    created_at = Column(
        DateTime,
        default=datetime.utcnow,
    )