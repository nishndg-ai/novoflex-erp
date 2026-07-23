from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text

from app.platform.metadata.models.base_entity import BaseEntity


class MetadataReport(BaseEntity):
    __tablename__ = "metadata_reports"

    module_id = Column(
        Integer,
        ForeignKey("metadata_modules.id"),
        nullable=False,
        index=True,
    )

    report_name = Column(
        String(150),
        nullable=False,
    )

    report_type = Column(
        String(50),
        nullable=False,
    )

    query_definition = Column(
        Text,
        nullable=False,
    )

    is_default = Column(
        Boolean,
        default=False,
    )

    is_active = Column(
        Boolean,
        default=True,
    )