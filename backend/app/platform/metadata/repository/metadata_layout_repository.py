from app.repositories.base_repository import BaseRepository
from app.platform.metadata.models.metadata_layout import MetadataLayout


class MetadataLayoutRepository(BaseRepository):
    def __init__(self):
        super().__init__(MetadataLayout)


metadata_layout_repository = MetadataLayoutRepository()