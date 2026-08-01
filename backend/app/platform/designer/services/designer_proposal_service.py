from __future__ import annotations

from sqlalchemy.orm import Session

from app.platform.designer.models.designer_proposal import (
    DesignerProposal,
)

from app.platform.designer.services.designer_validation_service import (
    designer_validation_service,
    DesignerValidationError,
)



class DesignerProposalService:
    """
    BLUISH Designer Proposal Service.

    Handles lifecycle:

        ANALYZED
            |
            ↓
          DRAFT
            |
            ↓
        APPROVED
            |
            ↓
         CREATED

        or

        REJECTED
    """



    # =====================================================
    # CREATE PROPOSAL
    # =====================================================

    def create_proposal(
        self,
        db: Session,
        proposal_data: dict,
        source: str = "MANUAL",
        created_by: str | None = None,
    ):


        designer_validation_service.validate_object(

            db,

            proposal_data.get(
                "object_name"
            ),

            proposal_data.get(
                "fields",
                [],
            ),

        )



        proposal = DesignerProposal(

            object_name=proposal_data.get(
                "object_name"
            ),

            description=proposal_data.get(
                "description"
            ),

            application=proposal_data.get(
                "application",
                "MASTER",
            ),

            category=proposal_data.get(
                "category",
                "MASTER",
            ),

            source=source,

            definition=proposal_data,

            status="DRAFT",

            created_by=created_by,

        )


        db.add(
            proposal
        )


        db.commit()

        db.refresh(
            proposal
        )


        return proposal




    # =====================================================
    # GET PROPOSAL
    # =====================================================

    def get_proposal(
        self,
        db: Session,
        proposal_id: int,
    ):


        return (

            db.query(
                DesignerProposal
            )

            .filter(
                DesignerProposal.id == proposal_id
            )

            .first()

        )




    # =====================================================
    # LIST PROPOSALS
    # =====================================================

    def list_proposals(
        self,
        db: Session,
    ):


        return (

            db.query(
                DesignerProposal
            )

            .order_by(
                DesignerProposal.id.desc()
            )

            .all()

        )




    # =====================================================
    # APPROVE
    # =====================================================

    def approve_proposal(
        self,
        db: Session,
        proposal_id: int,
        approved_by: str,
    ):


        proposal = self.get_proposal(
            db,
            proposal_id,
        )


        if not proposal:

            raise DesignerValidationError(
                "Proposal not found."
            )



        proposal.status = "APPROVED"

        proposal.approved_by = approved_by


        db.commit()

        db.refresh(
            proposal
        )


        return proposal




    # =====================================================
    # REJECT
    # =====================================================

    def reject_proposal(
        self,
        db: Session,
        proposal_id: int,
    ):


        proposal = self.get_proposal(
            db,
            proposal_id,
        )


        if not proposal:

            raise DesignerValidationError(
                "Proposal not found."
            )



        proposal.status = "REJECTED"


        db.commit()

        db.refresh(
            proposal
        )


        return proposal




designer_proposal_service = DesignerProposalService()