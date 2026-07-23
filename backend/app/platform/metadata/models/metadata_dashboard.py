from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from app.platform.metadata.models.base_entity import BaseEntity


class MetadataDashboard(BaseEntity):
    __tablename__ = "metadata_dashboards"

    module_id = Column(
        Integer,
        ForeignKey("metadata_modules.id"),
        nullable=False,
        index=True,
    )

    dashboard_name = Column(
        String(150),
        nullable=False,
    )

    chart_type = Column(
        String(50),
        nullable=False,
    )

    data_source = Column(
        String(200),
        nullable=False,
    )

    display_order = Column(
        Integer,
        default=0,
    )

    is_default = Column(
        Boolean,
        default=False,
    )

    is_active = Column(
        Boolean,
        default=True,
    )