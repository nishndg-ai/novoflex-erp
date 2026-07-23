from app.repositories.company_repository import company_repository
from app.services.base_service import BaseService


class CompanyService(BaseService):

    def __init__(self):
        super().__init__(company_repository)


company_service = CompanyService()