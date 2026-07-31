from __future__ import annotations

from typing import Any

from fastapi import (
    APIRouter,
    Depends,
    Query,
    HTTPException,
    Request,
    status,
)

from sqlalchemy.orm import Session


from app.database.session import get_db

from app.core.security import get_current_user

from app.platform.crud import CrudEngine

from app.platform.runtime.runtime_data_engine import (
    RuntimeDataEngine,
    RuntimeAccessError,
)

from app.platform.runtime.runtime_engine import (
    RuntimeEngine,
)



router = APIRouter(
    prefix="/runtime-data",
    tags=["Runtime CRUD"],
)





def check_runtime_permission(
    action: str,
):

    def checker(
        request: Request,
        current_user: dict = Depends(
            get_current_user
        ),
    ):

        module_code = request.path_params.get(
            "module_code"
        )


        permissions = current_user.get(
            "permissions",
            []
        )


        for permission in permissions:

            if permission.get(
                "module_code"
            ) == module_code:


                if permission.get(
                    f"can_{action}",
                    False,
                ):

                    return current_user



        raise HTTPException(

            status_code=status.HTTP_403_FORBIDDEN,

            detail="Permission denied",

        )


    return checker






def get_crud_engine(
    db: Session,
    user_context: dict,
) -> CrudEngine:


    runtime_engine = RuntimeEngine(
        db
    )


    data_engine = RuntimeDataEngine(
        db
    )


    return CrudEngine(

        runtime_engine=runtime_engine,

        data_engine=data_engine,

        user_context=user_context,

    )








# =====================================================
# LIST
# =====================================================

@router.get("/{module_code}")
def list_records(

    module_code: str,

    limit: int = Query(
        default=100,
        ge=1,
    ),

    offset: int = Query(
        default=0,
        ge=0,
    ),

    search: str | None = None,

    order_by: str | None = None,

    descending: bool = False,

    include_deleted: bool = False,


    db: Session = Depends(
        get_db
    ),


    current_user: dict = Depends(
        check_runtime_permission("view")
    ),

):


    engine = get_crud_engine(

        db,

        current_user,

    )


    return engine.list(

        module_code=module_code,

        search=search,

        limit=limit,

        offset=offset,

        order_by=order_by,

        descending=descending,

        include_deleted=include_deleted,

    )








# =====================================================
# GET
# =====================================================

@router.get("/{module_code}/{record_id}")
def get_record(

    module_code: str,

    record_id: int,


    db: Session = Depends(
        get_db
    ),


    current_user: dict = Depends(
        check_runtime_permission("view")
    ),

):


    engine = get_crud_engine(

        db,

        current_user,

    )


    return engine.get(

        module_code=module_code,

        record_id=record_id,

    )








# =====================================================
# CREATE
# =====================================================

@router.post("/{module_code}")
def create_record(

    module_code: str,

    values: dict[str, Any],


    db: Session = Depends(
        get_db
    ),


    current_user: dict = Depends(
        check_runtime_permission("create")
    ),

):


    engine = get_crud_engine(

        db,

        current_user,

    )


    return engine.create(

        module_code=module_code,

        values=values,

    )








# =====================================================
# UPDATE
# =====================================================

@router.put("/{module_code}/{record_id}")
def update_record(

    module_code: str,

    record_id: int,

    values: dict[str, Any],


    db: Session = Depends(
        get_db
    ),


    current_user: dict = Depends(
        check_runtime_permission("edit")
    ),

):


    engine = get_crud_engine(

        db,

        current_user,

    )


    try:

        engine.update(

            module_code=module_code,

            record_id=record_id,

            values=values,

        )


    except RuntimeAccessError as e:

        raise HTTPException(

            status_code=403,

            detail=str(e),

        )



    return {

        "success": True,

        "message":
            "Record updated successfully.",

    }








# =====================================================
# DELETE
# =====================================================

@router.delete("/{module_code}/{record_id}")
def delete_record(

    module_code: str,

    record_id: int,


    db: Session = Depends(
        get_db
    ),


    current_user: dict = Depends(
        check_runtime_permission("delete")
    ),

):


    engine = get_crud_engine(

        db,

        current_user,

    )


    try:

        engine.delete(

            module_code=module_code,

            record_id=record_id,

        )


    except RuntimeAccessError as e:

        raise HTTPException(

            status_code=403,

            detail=str(e),

        )



    return {

        "success": True,

        "message":
            "Record deleted successfully.",

    }








# =====================================================
# RESTORE
# =====================================================

@router.post("/{module_code}/{record_id}/restore")
def restore_record(

    module_code: str,

    record_id: int,


    db: Session = Depends(
        get_db
    ),


    current_user: dict = Depends(
        check_runtime_permission("restore")
    ),

):


    engine = get_crud_engine(

        db,

        current_user,

    )


    try:

        engine.restore(

            module_code=module_code,

            record_id=record_id,

        )


    except RuntimeAccessError as e:

        raise HTTPException(

            status_code=403,

            detail=str(e),

        )



    return {

        "success": True,

        "message":
            "Record restored successfully.",

    }