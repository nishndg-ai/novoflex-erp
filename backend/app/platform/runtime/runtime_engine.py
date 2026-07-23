import logging

from sqlalchemy.orm import Session

from app.platform.runtime.dashboard_loader import DashboardLoader
from app.platform.runtime.field_loader import FieldLoader
from app.platform.runtime.layout_loader import LayoutLoader
from app.platform.runtime.module_loader import ModuleLoader
from app.platform.runtime.permission_loader import PermissionLoader
from app.platform.runtime.report_loader import ReportLoader
from app.platform.runtime.types import RuntimeDefinition
from app.platform.runtime.workflow_loader import WorkflowLoader

logger = logging.getLogger(__name__)


class RuntimeEngine:
    """
    Runtime Engine

    Builds the complete runtime definition for a module.
    The RuntimeDefinition returned by this class is consumed
    directly by the frontend.
    """

    def __init__(self, db: Session):
        self.db = db

    def build_runtime(
        self,
        module_code: str,
    ) -> RuntimeDefinition | None:

        logger.info("Building runtime for module '%s'", module_code)

        module = ModuleLoader.load_by_code(
            self.db,
            module_code,
        )

        if module is None:
            logger.warning(
                "Module '%s' not found.",
                module_code,
            )
            return None

        runtime = RuntimeDefinition(module=module)

        runtime.fields = self._safe_load(
            "FieldLoader",
            FieldLoader.load_fields,
            module.id,
        )

        runtime.layout = self._safe_load(
            "LayoutLoader",
            LayoutLoader.load_layout,
            module.id,
        )

        runtime.workflow = self._safe_load(
            "WorkflowLoader",
            WorkflowLoader.load_workflow,
            module.id,
        )

        runtime.permissions = self._safe_load(
            "PermissionLoader",
            PermissionLoader.load_permissions,
            module.id,
        )

        runtime.dashboard = self._safe_load(
            "DashboardLoader",
            DashboardLoader.load_dashboard,
            module.id,
        )

        runtime.reports = self._safe_load(
            "ReportLoader",
            ReportLoader.load_reports,
            module.id,
        )

        return runtime

    def _safe_load(
        self,
        loader_name: str,
        loader,
        module_id: int,
    ):
        """
        Executes a loader safely.

        If a loader fails,
        an empty list is returned.
        """

        try:
            result = loader(
                self.db,
                module_id,
            )

            return result or []

        except Exception:
            logger.exception(
                "%s failed while loading module_id=%s",
                loader_name,
                module_id,
            )

            return []