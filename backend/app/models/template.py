from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    Boolean,
    func,
)

from app.database.base import Base


class Template(Base):
    __tablename__ = "templates"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    name = Column(
        String(200),
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

    sheet_name = Column(
        String(100),
        nullable=True,
    )

    version = Column(
        Integer,
        default=1,
    )

    is_active = Column(
        Boolean,
        default=True,
    )

    created_at = Column(
        DateTime,
        server_default=func.now(),
    )