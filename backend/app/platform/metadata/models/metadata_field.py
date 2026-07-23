from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import relationship

from app.platform.metadata.models.base_entity import BaseEntity


class MetadataField(BaseEntity):
    __tablename__ = "metadata_fields"

    module_id = Column(
        Integer,
        ForeignKey("metadata_modules.id"),
        nullable=False,
        index=True,
    )

    field_name = Column(
        String(100),
        nullable=False,
    )

    display_name = Column(
        String(150),
        nullable=False,
    )

    data_type = Column(
        String(50),
        nullable=False,
    )

    control_type = Column(
        String(50),
        nullable=False,
    )

    length = Column(
        Integer,
        nullable=True,
    )

    decimal_places = Column(
        Integer,
        default=0,
        nullable=True,
    )

    default_value = Column(
        String(255),
        nullable=True,
    )

    is_primary = Column(
        Boolean,
        default=False,
        nullable=False,
    )

    is_required = Column(
        Boolean,
        default=False,
        nullable=False,
    )

    is_unique = Column(
        Boolean,
        default=False,
        nullable=False,
    )

    is_visible = Column(
        Boolean,
        default=True,
        nullable=False,
    )

    is_editable = Column(
        Boolean,
        default=True,
        nullable=False,
    )

    display_order = Column(
        Integer,
        default=1,
        nullable=False,
    )

    module = relationship(
        "MetadataModule",
        backref="fields",
    )