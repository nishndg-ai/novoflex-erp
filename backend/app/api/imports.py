from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.platform.master_engine.import_service import (
    ImportService,
)


router = APIRouter(
    prefix="/import",
    tags=["Master Import"],
)



@router.post(
    "/{module_code}/preview",
)
async def preview_import(
    module_code: str,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):

    try:

        temp_path = (
            f"temp_{file.filename}"
        )

        content = await file.read()

        with open(
            temp_path,
            "wb"
        ) as f:

            f.write(content)


        service = ImportService(
            db
        )


        return service.preview(
            module_code,
            temp_path,
        )


    except Exception as e:

        raise HTTPException(
            status_code=400,
            detail=str(e),
        )





@router.post(
    "/{module_code}/execute",
)
async def execute_import(
    module_code: str,
    file: UploadFile = File(...),
    user: str = "admin",
    db: Session = Depends(get_db),
):

    try:

        temp_path = (
            f"temp_{file.filename}"
        )

        content = await file.read()

        with open(
            temp_path,
            "wb"
        ) as f:

            f.write(content)



        service = ImportService(
            db
        )


        return service.import_records(
            module_code,
            temp_path,
            user=user,
        )


    except Exception as e:

        raise HTTPException(
            status_code=400,
            detail=str(e),
        )