from app.repositories.uom_repository import uom_repository
from app.services.base_service import BaseService


class UOMService(BaseService):

    def __init__(self):
        super().__init__(uom_repository)


uom_service = UOMService()