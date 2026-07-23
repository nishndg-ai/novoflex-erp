from app.repositories.department_repository import department_repository
from app.services.base_service import BaseService


class DepartmentService(BaseService):

    def __init__(self):
        super().__init__(department_repository)


department_service = DepartmentService()