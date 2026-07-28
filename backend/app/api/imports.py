from fastapi import (
    APIRouter,
    Depends,
    UploadFile,
    File,
    HTTPException,
)

from fastapi.responses import FileResponse

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.platform.runtime.runtime_engine import (
    RuntimeEngine,
)

from app.platform.master_engine.import_service import (
    ImportService,
)

from app.platform.master_engine.template_generator import (
    TemplateGenerator,
)



router = APIRouter(
    prefix="/import",
    tags=["Master Import"],
)



# =========================================================
# Preview Import
# =========================================================

@router.post(
    "/{module_code}/preview",
)
async def preview_import(
    module_code: str,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):

    try:

        temp_path = f"temp_{file.filename}"


        content = await file.read()


        with open(
            temp_path,
            "wb",
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



# =========================================================
# Validate Import Only
# =========================================================

@router.post(
    "/{module_code}/validate",
)
async def validate_import(
    module_code: str,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):

    try:

        temp_path = f"temp_{file.filename}"


        content = await file.read()


        with open(
            temp_path,
            "wb",
        ) as f:

            f.write(content)



        service = ImportService(
            db
        )


        runtime = service.runtime_engine.build_runtime(
            module_code
        )


        if runtime is None:

            raise HTTPException(
                status_code=404,
                detail=(
                    f"Module '{module_code}' not found."
                ),
            )



        rows = service.importer.import_data(
            temp_path
        )


        if rows:

            service.validate_columns(
                runtime,
                list(rows[0].keys()),
            )



        mapped_rows = []


        for row in rows:

            mapped_row = service.map_columns(
                runtime,
                row,
            )


            mapped_row = service.clean_values(
                mapped_row
            )


            mapped_row = service.apply_defaults(
                runtime,
                mapped_row,
            )


            mapped_rows.append(
                mapped_row
            )



        return service.import_validator.validate(
            runtime,
            mapped_rows,
        )


    except Exception as e:

        raise HTTPException(
            status_code=400,
            detail=str(e),
        )



# =========================================================
# Execute Import
# =========================================================

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

        temp_path = f"temp_{file.filename}"


        content = await file.read()


        with open(
            temp_path,
            "wb",
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



# =========================================================
# Download Template
# =========================================================

@router.get(
    "/{module_code}/template",
)
def download_template(
    module_code: str,
    db: Session = Depends(get_db),
):

    try:

        runtime = RuntimeEngine(
            db
        ).build_runtime(
            module_code
        )


        if runtime is None:

            raise HTTPException(
                status_code=404,
                detail=(
                    f"Module '{module_code}' not found."
                ),
            )



        file_path = (
            f"template_{module_code}.xlsx"
        )


        TemplateGenerator().generate(
            runtime,
            file_path,
        )


        return FileResponse(
            path=file_path,
            filename=file_path,
            media_type=(
                "application/"
                "vnd.openxmlformats-officedocument."
                "spreadsheetml.sheet"
            ),
        )


    except Exception as e:

        raise HTTPException(
            status_code=400,
            detail=str(e),
        )