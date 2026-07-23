from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.platform.runtime.runtime_engine import RuntimeEngine
from app.platform.runtime.runtime_data_engine import RuntimeDataEngine

router = APIRouter(
    prefix="/runtime-data",
    tags=["Runtime Data"],
)


@router.get(
    "/{module_code}",
    summary="Get Module Data",
)
def get_module_data(
    module_code: str,
    db: Session = Depends(get_db),
):
    """
    Returns business data for any runtime-enabled module.
    """

    runtime = RuntimeEngine(db).build_runtime(module_code)

    if runtime is None:
        raise HTTPException(
            status_code=404,
            detail=f"Module '{module_code}' not found.",
        )

    engine = RuntimeDataEngine(db)

    data = engine.get_records(
        runtime.module.table_name,
    )

    return {
        "module": runtime.module.module_code,
        "table": runtime.module.table_name,
        "total": len(data),
        "data": data,
    }