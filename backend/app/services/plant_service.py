from app.repositories.plant_repository import plant_repository
from app.services.base_service import BaseService


class PlantService(BaseService):

    def __init__(self):
        super().__init__(plant_repository)


plant_service = PlantService()