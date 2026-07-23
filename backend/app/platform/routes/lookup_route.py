from __future__ import annotations

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.platform.lookup.lookup_service import LookupService
from app.platform.runtime.runtime_data_engine import RuntimeDataEngine
from app.platform.runtime.runtime_engine import RuntimeEngine

router = APIRouter(
    prefix="/lookup",
    tags=["Lookup"],
)


def get_lookup_service(db: Session) -> LookupService:
    runtime_engine = RuntimeEngine(db)
    data_engine = RuntimeDataEngine(db)
    return LookupService(runtime_engine, data_engine)


@router.get("/{module_code}")
def lookup(
    module_code: str,
    search: str | None = Query(default=None),
    limit: int = Query(default=25, ge=1, le=500),
    db: Session = Depends(get_db),
):
    service = get_lookup_service(db)

    return service.lookup(
        module_code=module_code,
        search=search,
        limit=limit,
    )