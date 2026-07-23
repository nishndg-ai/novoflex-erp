from app.models.plant import Plant
from app.repositories.base_repository import BaseRepository


class PlantRepository(BaseRepository[Plant]):
    def __init__(self):
        super().__init__(Plant)


plant_repository = PlantRepository()