from sqlalchemy import (
    JSON,
    Boolean,
    Column,
    Enum,
    ForeignKey,
    Integer,
    String,
    Text,
    UniqueConstraint,
)
from sqlalchemy.orm import relationship

from app.platform.metadata.enums import ViewComponentType
from app.platform.metadata.models.base_entity import BaseEntity


class MetadataViewComponent(BaseEntity):
    __tablename__ = "metadata_view_components"

    __table_args__ = (
        UniqueConstraint(
            "view_id",
            "component_name",
            name="uq_metadata_view_component_name",
        ),
    )

    # ---------------------------------------------------------
    # Parent View
    # ---------------------------------------------------------

    view_id = Column(
        Integer,
        ForeignKey("metadata_views.id"),
        nullable=False,
        index=True,
    )

    # ---------------------------------------------------------
    # Optional Metadata Field
    # ---------------------------------------------------------

    field_id = Column(
        Integer,
        ForeignKey("metadata_fields.id"),
        nullable=True,
        index=True,
    )

    # ---------------------------------------------------------
    # Component Definition
    # ---------------------------------------------------------

    component_type = Column(
        Enum(ViewComponentType),
        nullable=False,
        index=True,
    )

    component_name = Column(
        String(100),
        nullable=False,
    )

    display_name = Column(
        String(200),
        nullable=False,
    )

    description = Column(
        Text,
        nullable=True,
    )

    # ---------------------------------------------------------
    # Layout
    # ---------------------------------------------------------

    display_order = Column(
        Integer,
        nullable=False,
        default=1,
    )

    row_no = Column(
        Integer,
        nullable=False,
        default=1,
    )

    column_no = Column(
        Integer,
        nullable=False,
        default=1,
    )

    column_span = Column(
        Integer,
        nullable=False,
        default=1,
    )

    # ---------------------------------------------------------
    # Behaviour
    # ---------------------------------------------------------

    is_visible = Column(
        Boolean,
        nullable=False,
        default=True,
    )

    is_readonly = Column(
        Boolean,
        nullable=False,
        default=False,
    )

    # ---------------------------------------------------------
    # Styling
    # ---------------------------------------------------------

    css_class = Column(
        String(200),
        nullable=True,
    )

    style = Column(
        Text,
        nullable=True,
    )

    # ---------------------------------------------------------
    # Additional Component Properties
    # ---------------------------------------------------------

    properties = Column(
        JSON,
        nullable=True,
    )

    # ---------------------------------------------------------
    # Relationships
    # ---------------------------------------------------------

    view = relationship(
        "MetadataView",
        backref="components",
    )

    field = relationship(
        "MetadataField",
        backref="view_components",
    )