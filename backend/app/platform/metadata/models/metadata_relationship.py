from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import relationship

from app.platform.metadata.models.base_entity import BaseEntity


class MetadataRelationship(BaseEntity):
    __tablename__ = "metadata_relationships"

    parent_module_id = Column(
        Integer,
        ForeignKey("metadata_modules.id"),
        nullable=False,
        index=True,
    )

    child_module_id = Column(
        Integer,
        ForeignKey("metadata_modules.id"),
        nullable=False,
        index=True,
    )

    relationship_name = Column(
        String(100),
        nullable=False,
    )

    relationship_type = Column(
        String(50),
        nullable=False,
        default="OneToMany",
    )

    parent_key = Column(
        String(100),
        nullable=False,
        default="id",
    )

    child_key = Column(
        String(100),
        nullable=False,
    )

    cascade_delete = Column(
        Boolean,
        default=False,
        nullable=False,
    )

    lazy_loading = Column(
        Boolean,
        default=True,
        nullable=False,
    )

    parent_module = relationship(
        "MetadataModule",
        foreign_keys=[parent_module_id],
    )

    child_module = relationship(
        "MetadataModule",
        foreign_keys=[child_module_id],
    )