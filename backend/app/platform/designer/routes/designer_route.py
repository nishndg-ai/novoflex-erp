from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.database.session import get_db

from app.platform.designer.schemas.designer_schema import (
    BusinessObjectCreateRequest,
)

from app.platform.designer.services.business_object_designer_service import (
    business_object_designer_service,
)


router = APIRouter(
    prefix="/designer",
    tags=["Business Object Designer"],
)



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