from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.platform.crud import CrudEngine
from app.platform.runtime.runtime_data_engine import RuntimeDataEngine
from app.platform.runtime.runtime_engine import RuntimeEngine

router = APIRouter(prefix="/runtime", tags=["Runtime CRUD"])


def get_crud_engine(db: Session) -> CrudEngine:
    runtime_engine = RuntimeEngine(db)
    data_engine = RuntimeDataEngine(db)
    return CrudEngine(runtime_engine, data_engine)


@router.get("/{module_code}")
def list_records(
    module_code: str,
    limit: int = Query(100, ge=1),
    offset: int = Query(0, ge=0),
    search: str | None = None,
    order_by: str | None = None,
    descending: bool = False,
    db: Session = Depends(get_db),
):

    engine = get_crud_engine(db)

    return engine.list(
        module_code=module_code,
        search=search,
        limit=limit,
        offset=offset,
        order_by=order_by,
        descending=descending,
    )


@router.get("/{module_code}/{record_id}")
def get_record(
    module_code: str,
    record_id: int,
    db: Session = Depends(get_db),
):

    engine = get_crud_engine(db)

    return engine.get(
        module_code=module_code,
        record_id=record_id,
    )


@router.post("/{module_code}")
def create_record(
    module_code: str,
    values: dict[str, Any],
    db: Session = Depends(get_db),
):

    engine = get_crud_engine(db)

    return engine.create(
        module_code=module_code,
        values=values,
    )


@router.put("/{module_code}/{record_id}")
def update_record(
    module_code: str,
    record_id: int,
    values: dict[str, Any],
    db: Session = Depends(get_db),
):

    engine = get_crud_engine(db)

    engine.update(
        module_code=module_code,
        record_id=record_id,
        values=values,
    )

    return {"success": True}


@router.delete("/{module_code}/{record_id}")
def delete_record(
    module_code: str,
    record_id: int,
    db: Session = Depends(get_db),
):

    engine = get_crud_engine(db)

    engine.delete(
        module_code=module_code,
        record_id=record_id,
    )

    return {"success": True}