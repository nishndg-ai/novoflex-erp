from app.models.company import Company
from app.repositories.base_repository import BaseRepository


class CompanyRepository(BaseRepository):

    def __init__(self):
        super().__init__(Company)


company_repository = CompanyRepository()