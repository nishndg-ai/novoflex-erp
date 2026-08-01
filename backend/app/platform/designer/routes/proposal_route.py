from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
)

from sqlalchemy.orm import Session


from app.database.session import get_db


from app.platform.designer.services.designer_proposal_service import (
    designer_proposal_service,
    DesignerValidationError,
)


from app.platform.designer.services.proposal_conversion_service import (
    proposal_conversion_service,
)


from app.platform.designer.services.business_object_designer_service import (
    business_object_designer_service,
)



router = APIRouter(

    prefix="/designer/proposals",

    tags=["Designer Proposals"],

)



# =====================================================
# CREATE PROPOSAL
# =====================================================

@router.post("")
def create_proposal(

    proposal_data: dict,

    db: Session = Depends(get_db),

):


    try:

        proposal = (
            designer_proposal_service
            .create_proposal(

                db,

                proposal_data,

                source="MANUAL",

            )
        )


    except DesignerValidationError as e:

        raise HTTPException(

            status_code=400,

            detail=str(e),

        )



    return {

        "success": True,

        "message":
            "Proposal created successfully.",

        "proposal_id":
            proposal.id,

        "status":
            proposal.status,

    }




# =====================================================
# LIST PROPOSALS
# =====================================================

@router.get("")
def list_proposals(

    db: Session = Depends(get_db),

):


    proposals = (

        designer_proposal_service

        .list_proposals(

            db

        )

    )


    return {

        "success": True,

        "count":
            len(proposals),

        "data":
            proposals,

    }




# =====================================================
# GET PROPOSAL
# =====================================================

@router.get("/{proposal_id}")
def get_proposal(

    proposal_id: int,

    db: Session = Depends(get_db),

):


    proposal = (

        designer_proposal_service

        .get_proposal(

            db,

            proposal_id,

        )

    )


    if not proposal:

        raise HTTPException(

            status_code=404,

            detail="Proposal not found.",

        )



    return proposal




# =====================================================
# APPROVE PROPOSAL
# =====================================================

@router.post("/{proposal_id}/approve")
def approve_proposal(

    proposal_id: int,

    approved_by: str = "ADMIN",

    db: Session = Depends(get_db),

):


    try:

        proposal = (

            designer_proposal_service

            .approve_proposal(

                db,

                proposal_id,

                approved_by,

            )

        )


    except DesignerValidationError as e:

        raise HTTPException(

            status_code=400,

            detail=str(e),

        )



    return {

        "success": True,

        "message":
            "Proposal approved successfully.",

        "proposal_id":
            proposal.id,

        "status":
            proposal.status,

    }




# =====================================================
# REJECT PROPOSAL
# =====================================================

@router.post("/{proposal_id}/reject")
def reject_proposal(

    proposal_id: int,

    db: Session = Depends(get_db),

):


    try:

        proposal = (

            designer_proposal_service

            .reject_proposal(

                db,

                proposal_id,

            )

        )


    except DesignerValidationError as e:

        raise HTTPException(

            status_code=400,

            detail=str(e),

        )



    return {

        "success": True,

        "message":
            "Proposal rejected successfully.",

        "proposal_id":
            proposal.id,

        "status":
            proposal.status,

    }




# =====================================================
# CREATE BUSINESS OBJECT FROM APPROVED PROPOSAL
# =====================================================

@router.post("/{proposal_id}/create-object")
def create_object_from_proposal(

    proposal_id: int,

    db: Session = Depends(get_db),

):


    proposal = (

        designer_proposal_service

        .get_proposal(

            db,

            proposal_id,

        )

    )



    if not proposal:

        raise HTTPException(

            status_code=404,

            detail="Proposal not found.",

        )



    if proposal.status != "APPROVED":

        raise HTTPException(

            status_code=400,

            detail=
            "Only approved proposals can create business objects.",

        )



    try:


        request = (

            proposal_conversion_service

            .convert(

                proposal.definition

            )

        )



        module = (

            business_object_designer_service

            .create_object(

                db,

                request,

            )

        )



        proposal.status = "CREATED"


        db.commit()



    except DesignerValidationError as e:


        raise HTTPException(

            status_code=400,

            detail=str(e),

        )



    return {

        "success": True,

        "message":
            "Business object created from proposal.",

        "proposal_id":
            proposal.id,

        "module_id":
            module.id,

        "module_code":
            module.module_code,

        "status":
            proposal.status,

    }