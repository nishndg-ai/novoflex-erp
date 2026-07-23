from app.models.uom import UOM
from app.repositories.base_repository import BaseRepository


class UOMRepository(BaseRepository):

    def __init__(self):
        super().__init__(UOM)


uom_repository = UOMRepository()