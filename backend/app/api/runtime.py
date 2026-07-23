from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.platform.runtime.runtime_engine import RuntimeEngine
from app.platform.runtime.types import RuntimeDefinition

router = APIRouter(
    prefix="/runtime",
    tags=["Runtime"],
)


@router.get(
    "/{module_code}",
    response_model=RuntimeDefinition,
    summary="Get Module Runtime",
    description="Returns the complete runtime definition for a module.",
)
def get_runtime(
    module_code: str,
    db: Session = Depends(get_db),
) -> RuntimeDefinition:
    """
    Returns the complete runtime definition for a module.

    The runtime contains:
    - Module information
    - Fields
    - Layout
    - Workflow
    - Permissions
    - Dashboard
    - Reports
    """

    runtime = RuntimeEngine(db).build_runtime(module_code)

    if runtime is None:
        raise HTTPException(
            status_code=404,
            detail=f"Module '{module_code}' not found.",
        )

    return runtime