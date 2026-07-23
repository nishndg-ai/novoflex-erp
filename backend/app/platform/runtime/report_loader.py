from sqlalchemy.orm import Session

from app.platform.runtime.types import ReportDefinition


class ReportLoader:
    """
    Loads report definitions for a module.

    This is a placeholder implementation until the
    metadata report tables are implemented.
    """

    @staticmethod
    def load_reports(
        db: Session,
        module_id: int,
    ) -> list[ReportDefinition]:
        """
        Returns report definitions for the specified module.
        """

        return []