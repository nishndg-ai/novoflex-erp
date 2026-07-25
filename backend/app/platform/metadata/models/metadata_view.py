from sqlalchemy import (
    Boolean,
    Column,
    Enum,
    ForeignKey,
    Integer,
    String,
    UniqueConstraint,
)
from sqlalchemy.orm import relationship

from app.platform.metadata.enums import ViewType
from app.platform.metadata.models.base_entity import BaseEntity


class MetadataView(BaseEntity):
    __tablename__ = "metadata_views"

    __table_args__ = (
        UniqueConstraint(
            "module_id",
            "view_code",
            name="uq_metadata_view_module_code",
        ),
    )

    module_id = Column(
        Integer,
        ForeignKey("metadata_modules.id"),
        nullable=False,
        index=True,
    )

    view_code = Column(
        String(100),
        nullable=False,
        index=True,
    )

    display_name = Column(
        String(200),
        nullable=False,
    )

    description = Column(
        String(500),
        nullable=True,
    )

    view_type = Column(
        Enum(ViewType),
        nullable=False,
        index=True,
    )

    page_size = Column(
        Integer,
        nullable=False,
        default=20,
    )

    default_sort_field = Column(
        String(100),
        nullable=True,
    )

    default_sort_order = Column(
        String(4),
        nullable=True,
        default="ASC",
    )

    is_default = Column(
        Boolean,
        nullable=False,
        default=False,
    )

    allow_search = Column(
        Boolean,
        nullable=False,
        default=True,
    )

    allow_filter = Column(
        Boolean,
        nullable=False,
        default=True,
    )

    allow_sort = Column(
        Boolean,
        nullable=False,
        default=True,
    )

    allow_export = Column(
        Boolean,
        nullable=False,
        default=True,
    )

    allow_grouping = Column(
        Boolean,
        nullable=False,
        default=False,
    )

    allow_column_resize = Column(
        Boolean,
        nullable=False,
        default=True,
    )

    allow_column_reorder = Column(
        Boolean,
        nullable=False,
        default=True,
    )

    allow_pivot = Column(
        Boolean,
        nullable=False,
        default=False,
    )

    module = relationship(
        "MetadataModule",
        backref="views",
    )