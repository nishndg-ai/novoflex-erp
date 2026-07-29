from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    Integer,
    String,
)

from sqlalchemy.orm import relationship

from app.platform.metadata.models.base_entity import BaseEntity



class MetadataPermission(BaseEntity):

    __tablename__ = "metadata_permissions"



    module_id = Column(
        Integer,
        ForeignKey(
            "metadata_modules.id"
        ),
        nullable=False,
        index=True,
    )


    role_name = Column(
        String(100),
        nullable=False,
    )


    can_view = Column(
        Boolean,
        default=True,
    )


    can_create = Column(
        Boolean,
        default=False,
    )


    can_edit = Column(
        Boolean,
        default=False,
    )


    can_delete = Column(
        Boolean,
        default=False,
    )


    can_export = Column(
        Boolean,
        default=False,
    )


    can_import = Column(
        Boolean,
        default=False,
    )


    can_approve = Column(
        Boolean,
        default=False,
    )


    module = relationship(
        "MetadataModule"
    )