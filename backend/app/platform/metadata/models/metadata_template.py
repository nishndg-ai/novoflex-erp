from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from app.platform.metadata.models.base_entity import BaseEntity


class MetadataTemplate(BaseEntity):
    __tablename__ = "metadata_templates"

    module_id = Column(
        Integer,
        ForeignKey("metadata_modules.id"),
        nullable=False,
        index=True,
    )

    template_name = Column(
        String(150),
        nullable=False,
    )

    file_name = Column(
        String(255),
        nullable=False,
    )

    template_type = Column(
        String(50),
        default="Excel",
    )

    is_default = Column(
        Boolean,
        default=False,
    )

    is_active = Column(
        Boolean,
        default=True,
    )