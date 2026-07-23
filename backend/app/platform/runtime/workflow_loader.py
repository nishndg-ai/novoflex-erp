from sqlalchemy.orm import Session

from app.platform.runtime.types import WorkflowDefinition


class WorkflowLoader:
    """
    Loads workflow definitions for a module.

    This is a placeholder implementation until the
    metadata workflow tables are implemented.
    """

    @staticmethod
    def load_workflow(
        db: Session,
        module_id: int,
    ) -> list[WorkflowDefinition]:
        """
        Returns workflow definitions for the specified module.
        """

        return []