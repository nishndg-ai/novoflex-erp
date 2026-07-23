from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    JSON,
    DateTime,
    func,
)

from app.database.base import Base


class TemplateData(Base):
    __tablename__ = "template_data"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    template_id = Column(
        Integer,
        ForeignKey("templates.id"),
        nullable=False,
    )

    row_no = Column(
        Integer,
        nullable=False,
    )

    data = Column(
        JSON,
        nullable=False,
    )

    created_at = Column(
        DateTime,
        server_default=func.now(),
    )

    updated_at = Column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now(),
    )