from app.repositories.role_repository import role_repository
from app.services.base_service import BaseService


class RoleService(BaseService):

    def __init__(self):
        super().__init__(role_repository)


role_service = RoleService()