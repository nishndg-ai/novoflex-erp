from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    Integer,
    String,
    Text,
)
from sqlalchemy.orm import relationship

from app.platform.metadata.models.base_entity import BaseEntity


class MetadataValidation(BaseEntity):
    __tablename__ = "metadata_validations"

    field_id = Column(
        Integer,
        ForeignKey("metadata_fields.id"),
        nullable=False,
        index=True,
    )

    validation_type = Column(
        String(50),
        nullable=False,
    )

    validation_value = Column(
        String(255),
        nullable=True,
    )

    error_message = Column(
        String(255),
        nullable=False,
    )

    regex_pattern = Column(
        Text,
        nullable=True,
    )

    execution_order = Column(
        Integer,
        default=1,
        nullable=False,
    )

    is_server_side = Column(
        Boolean,
        default=True,
        nullable=False,
    )

    is_client_side = Column(
        Boolean,
        default=True,
        nullable=False,
    )

    field = relationship(
        "MetadataField",
        backref="validation_rules",
    )