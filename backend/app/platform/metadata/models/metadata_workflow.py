from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from app.platform.metadata.models.base_entity import BaseEntity


class MetadataWorkflow(BaseEntity):
    __tablename__ = "metadata_workflows"

    module_id = Column(
        Integer,
        ForeignKey("metadata_modules.id"),
        nullable=False,
        index=True,
    )

    workflow_name = Column(
        String(150),
        nullable=False,
    )

    step_no = Column(
        Integer,
        nullable=False,
    )

    step_name = Column(
        String(150),
        nullable=False,
    )

    approver_role = Column(
        String(100),
        nullable=False,
    )

    is_final = Column(
        Boolean,
        default=False,
    )