from sqlalchemy.orm import Session

from app.platform.runtime.types import PermissionDefinition


class PermissionLoader:
    """
    Loads permission definitions for a module.

    This is a placeholder implementation until the
    metadata permission tables are implemented.
    """

    @staticmethod
    def load_permissions(
        db: Session,
        module_id: int,
    ) -> list[PermissionDefinition]:
        """
        Returns permission definitions for the specified module.
        """

        return []