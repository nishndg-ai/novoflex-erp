from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
)

from sqlalchemy.orm import Session


from app.database.session import get_db


from app.platform.designer.versioning.designer_version_service import (
    designer_version_service,
)


from app.platform.designer.versioning.designer_object_version import (
    DesignerObjectVersion,
)



router = APIRouter(

    prefix="/designer/versions",

    tags=["Designer Versions"],

)



# =====================================================
# CREATE REVISION
# =====================================================

@router.post("/{module_id}/revision")
def create_revision(

    module_id: int,

    definition: dict,

    description: str | None = None,

    db: Session = Depends(get_db),

):


    try:

        version = (

            designer_version_service

            .create_revision(

                db,

                module_id,

                definition,

                description,

                created_by="SYSTEM",

            )

        )


    except Exception as e:


        raise HTTPException(

            status_code=400,

            detail=str(e),

        )



    return {

        "success": True,

        "message":
            "Revision created successfully.",

        "version_id":
            version.id,

        "module_id":
            version.module_id,

        "version_no":
            version.version_no,

        "status":
            version.status,

    }





# =====================================================
# LIST VERSIONS
# =====================================================

@router.get("/{module_id}")
def list_versions(

    module_id: int,

    db: Session = Depends(get_db),

):


    versions = (

        db.query(

            DesignerObjectVersion

        )

        .filter(

            DesignerObjectVersion.module_id == module_id

        )

        .order_by(

            DesignerObjectVersion.version_no

        )

        .all()

    )



    return {

        "success": True,

        "count":
            len(versions),

        "data":

            [

                {

                    "id":
                        version.id,

                    "module_id":
                        version.module_id,

                    "version_no":
                        version.version_no,

                    "change_type":
                        version.change_type,

                    "description":
                        version.description,

                    "status":
                        version.status,

                    "created_by":
                        version.created_by,

                    "approved_by":
                        version.approved_by,

                    "created_at":
                        version.created_at,

                    "updated_at":
                        version.updated_at,

                }

                for version in versions

            ]

    }





# =====================================================
# APPROVE REVISION
# =====================================================

@router.post("/{version_id}/approve")
def approve_revision(

    version_id: int,

    approved_by: str = "ADMIN",

    db: Session = Depends(get_db),

):


    try:

        version = (

            designer_version_service

            .approve_revision(

                db,

                version_id,

                approved_by,

            )

        )


    except Exception as e:


        raise HTTPException(

            status_code=400,

            detail=str(e),

        )



    return {

        "success": True,

        "message":
            "Revision approved successfully.",

        "version_id":
            version.id,

        "status":
            version.status,

    }





# =====================================================
# APPLY REVISION
# =====================================================

@router.post("/{version_id}/apply")
def apply_revision(

    version_id: int,

    db: Session = Depends(get_db),

):


    try:

        version = (

            designer_version_service

            .apply_revision(

                db,

                version_id,

            )

        )


    except Exception as e:


        raise HTTPException(

            status_code=400,

            detail=str(e),

        )



    return {

        "success": True,

        "message":
            "Revision applied successfully.",

        "version_id":
            version.id,

        "status":
            version.status,

    }