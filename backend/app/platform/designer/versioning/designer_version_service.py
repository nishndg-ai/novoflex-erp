from __future__ import annotations

from sqlalchemy.orm import Session


from app.platform.designer.versioning.designer_object_version import (
    DesignerObjectVersion,
)




class DesignerVersionService:
    """
    BLUISH Designer Version Management Service.

    Handles object lifecycle versions.

    Flow:

        Object Created
              |
              ↓
        Version 1 (APPLIED)
              |
              ↓
        Change Request
              |
              ↓
        Version 2 (DRAFT)
              |
              ↓
        APPROVED
              |
              ↓
        APPLIED
    """



    # =====================================================
    # CREATE INITIAL VERSION
    # =====================================================

    def create_initial_version(

        self,

        db: Session,

        module_id: int,

        definition: dict,

        created_by: str | None = None,

    ):


        version = DesignerObjectVersion(

            module_id=module_id,

            version_no=1,

            change_type="CREATE",

            description="Initial object creation",

            definition=definition,

            status="APPLIED",

            created_by=created_by,

        )


        db.add(

            version

        )


        db.commit()


        db.refresh(

            version

        )


        return version




    # =====================================================
    # GET CURRENT VERSION
    # =====================================================

    def get_current_version(

        self,

        db: Session,

        module_id: int,

    ):


        return (

            db.query(

                DesignerObjectVersion

            )

            .filter(

                DesignerObjectVersion.module_id == module_id

            )

            .order_by(

                DesignerObjectVersion.version_no.desc()

            )

            .first()

        )




    # =====================================================
    # CREATE NEW REVISION
    # =====================================================

    def create_revision(

        self,

        db: Session,

        module_id: int,

        definition: dict,

        description: str | None = None,

        created_by: str | None = None,

    ):


        current = self.get_current_version(

            db,

            module_id,

        )



        # =====================================================
        # VERSION CONTROL VALIDATION
        #
        # Revision allowed only when
        # applied baseline exists.
        #
        # =====================================================

        if not current:

            raise Exception(

                "Cannot create revision. "
                "Object has no applied baseline version."

            )



        if current.status != "APPLIED":

            raise Exception(

                "Cannot create revision. "
                "Current version is not applied."

            )



        next_version = (

            current.version_no + 1

        )



        revision = DesignerObjectVersion(

            module_id=module_id,

            version_no=next_version,

            change_type="MODIFY",

            description=description,

            definition=definition,

            status="DRAFT",

            created_by=created_by,

        )


        db.add(

            revision

        )


        db.commit()


        db.refresh(

            revision

        )


        return revision




    # =====================================================
    # APPROVE REVISION
    # =====================================================

    def approve_revision(

        self,

        db: Session,

        version_id: int,

        approved_by: str,

    ):


        version = (

            db.query(

                DesignerObjectVersion

            )

            .filter(

                DesignerObjectVersion.id == version_id

            )

            .first()

        )


        if not version:

            raise Exception(

                "Version not found."

            )



        if version.status != "DRAFT":

            raise Exception(

                "Only DRAFT versions can be approved."

            )



        version.status = "APPROVED"

        version.approved_by = approved_by



        db.commit()


        db.refresh(

            version

        )


        return version




    # =====================================================
    # APPLY REVISION
    # =====================================================

    def apply_revision(

        self,

        db: Session,

        version_id: int,

    ):


        version = (

            db.query(

                DesignerObjectVersion

            )

            .filter(

                DesignerObjectVersion.id == version_id

            )

            .first()

        )


        if not version:

            raise Exception(

                "Version not found."

            )



        if version.status != "APPROVED":

            raise Exception(

                "Only APPROVED versions can be applied."

            )



        version.status = "APPLIED"



        db.commit()


        db.refresh(

            version

        )


        return version





designer_version_service = DesignerVersionService()