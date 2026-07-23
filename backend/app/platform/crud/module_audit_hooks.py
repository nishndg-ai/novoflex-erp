from __future__ import annotations

from .audit_hooks import AuditCrudHooks
from .module_hooks import register_hooks


class CompanyAuditHooks(AuditCrudHooks):
    module_code = "company"


class PlantAuditHooks(AuditCrudHooks):
    module_code = "plant"


class DepartmentAuditHooks(AuditCrudHooks):
    module_code = "department"


class EmployeeAuditHooks(AuditCrudHooks):
    module_code = "employee"


class WarehouseAuditHooks(AuditCrudHooks):
    module_code = "warehouse"


register_hooks("company", CompanyAuditHooks)
register_hooks("plant", PlantAuditHooks)
register_hooks("department", DepartmentAuditHooks)
register_hooks("employee", EmployeeAuditHooks)
register_hooks("warehouse", WarehouseAuditHooks)