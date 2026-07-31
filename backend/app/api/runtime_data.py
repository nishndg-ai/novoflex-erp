from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Query,
)

from sqlalchemy.orm import Session


from app.database.database import get_db


from app.core.security import (
    get_current_user,
)


from app.platform.runtime.runtime_engine import (
    RuntimeEngine,
)


from app.platform.runtime.runtime_data_engine import (
    RuntimeDataEngine,
)



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

    include_deleted: bool = Query(
        default=False
    ),

    limit: int = Query(
        default=100,
        ge=1,
    ),

    offset: int = Query(
        default=0,
        ge=0,
    ),

    search: str | None = None,


    db: Session = Depends(
        get_db
    ),


    current_user: dict = Depends(
        get_current_user
    ),

):

    """
    Returns business data for any runtime-enabled module.

    Supports:
    - Pagination
    - Search
    - Soft deleted records
    - Company / Plant data isolation
    """



    runtime = RuntimeEngine(
        db
    ).build_runtime(
        module_code
    )



    if runtime is None:

        raise HTTPException(

            status_code=404,

            detail=f"Module '{module_code}' not found.",

        )




    engine = RuntimeDataEngine(
        db
    )



    data = engine.get_records(

        table_name=runtime.module.table_name,


        limit=limit,


        offset=offset,


        search=search,


        include_deleted=include_deleted,


        user_context=current_user,


        data_scope=runtime.module.data_scope,

    )



    return {


        "module":

            runtime.module.module_code,


        "table":

            runtime.module.table_name,


        "data":

            data,

    }