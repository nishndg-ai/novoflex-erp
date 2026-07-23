from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import relationship

from app.platform.metadata.models.base_entity import BaseEntity


class MetadataLayout(BaseEntity):
    __tablename__ = "metadata_layouts"

    module_id = Column(
        Integer,
        ForeignKey("metadata_modules.id"),
        nullable=False,
        index=True,
    )

    field_id = Column(
        Integer,
        ForeignKey("metadata_fields.id"),
        nullable=False,
        index=True,
    )

    section = Column(
        String(100),
        nullable=True,
    )

    row_no = Column(
        Integer,
        default=1,
        nullable=False,
    )

    column_no = Column(
        Integer,
        default=1,
        nullable=False,
    )

    column_span = Column(
        Integer,
        default=1,
        nullable=False,
    )

    tab_name = Column(
        String(100),
        nullable=True,
    )

    is_visible = Column(
        Boolean,
        default=True,
        nullable=False,
    )

    module = relationship(
        "MetadataModule",
        backref="layouts",
    )

    field = relationship(
        "MetadataField",
        backref="layouts",
    )