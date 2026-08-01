from fastapi import (
    APIRouter,
    Depends,
    UploadFile,
    File,
    HTTPException,
)

from sqlalchemy.orm import Session

from pathlib import Path
import tempfile
import shutil


from app.database.session import get_db


from app.platform.designer.schemas.designer_schema import (
    BusinessObjectCreateRequest,
)


from app.platform.designer.services.business_object_designer_service import (
    business_object_designer_service,
)


from app.platform.designer.services.object_analyzer_service import (
    object_analyzer_service,
)



router = APIRouter(
    prefix="/designer",
    tags=["Business Object Designer"],
)



# =====================================================
# CREATE BUSINESS OBJECT
# =====================================================

@router.post("/create-object")
def create_business_object(
    request: BusinessObjectCreateRequest,
    db: Session = Depends(get_db),
):


    module = (
        business_object_designer_service
        .create_object(
            db,
            request,
        )
    )


    return {

        "success": True,

        "message":
            "Business object created successfully.",

        "module_id":
            module.id,

        "module_code":
            module.module_code,

    }



# =====================================================
# ANALYZE EXCEL
# =====================================================

@router.post("/analyze-excel")
async def analyze_excel(
    file: UploadFile = File(...),
):


    try:


        suffix = (
            Path(file.filename)
            .suffix
            .lower()
        )


        if suffix not in [
            ".xlsx",
            ".xls",
        ]:

            raise HTTPException(

                status_code=400,

                detail=
                "Only Excel files are supported.",

            )



        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=suffix,
        ) as temp:


            shutil.copyfileobj(
                file.file,
                temp,
            )


            temp_path = temp.name



        proposal = (
            object_analyzer_service
            .analyze_excel(
                temp_path
            )
        )



        return {

            "success": True,

            "message":
                "Excel analyzed successfully.",

            "proposal":
                proposal,

        }



    except Exception as e:


        raise HTTPException(

            status_code=500,

            detail=str(e),

        )