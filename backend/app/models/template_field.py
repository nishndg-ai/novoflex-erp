from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    ForeignKey,
)

from app.database.base import Base


class TemplateField(Base):
    __tablename__ = "template_fields"

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

    field_name = Column(
        String(200),
        nullable=False,
    )

    display_name = Column(
        String(200),
        nullable=False,
    )

    data_type = Column(
        String(50),
        nullable=False,
    )

    is_required = Column(
        Boolean,
        default=False,
    )

    is_unique = Column(
        Boolean,
        default=False,
    )

    lookup_table = Column(
        String(100),
        nullable=True,
    )

    display_order = Column(
        Integer,
        default=1,
    )