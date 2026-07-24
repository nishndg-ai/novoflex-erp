from fastapi import APIRouter

from app.platform.metadata.routes import (
    router as module_router,
    metadata_field_router,
)

router = APIRouter()

router.include_router(module_router)
router.include_router(metadata_field_router)