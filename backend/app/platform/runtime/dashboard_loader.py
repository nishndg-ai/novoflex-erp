from sqlalchemy.orm import Session

from app.platform.runtime.types import DashboardDefinition


class DashboardLoader:
    """
    Loads dashboard definitions for a module.

    This is a placeholder implementation until the
    metadata dashboard tables are implemented.
    """

    @staticmethod
    def load_dashboard(
        db: Session,
        module_id: int,
    ) -> list[DashboardDefinition]:
        """
        Returns dashboard definitions for the specified module.
        """

        return []