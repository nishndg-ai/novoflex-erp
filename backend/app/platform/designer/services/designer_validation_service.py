from __future__ import annotations

import re

from sqlalchemy.orm import Session


from app.platform.metadata.repository.metadata_repository import (
    MetadataRepository,
)



class DesignerValidationError(Exception):
    """
    Designer validation exception.
    """

    pass





class DesignerValidationService:
    """
    BLUISH Designer Validation Engine.

    Validates Business Object proposals
    before module creation.

    Checks:

    - Object name
    - Duplicate module
    - Field names
    - SQL safety
    - Reserved words
    - Minimum fields
    """



    RESERVED_WORDS = {

        "user",
        "order",
        "group",
        "table",
        "select",
        "insert",
        "update",
        "delete",
        "create",
        "drop",

    }



    def __init__(self):

        self.repository = MetadataRepository()



    # =====================================================
    # COMPLETE VALIDATION
    # =====================================================

    def validate_object(
        self,
        db: Session,
        object_name: str,
        fields: list,
    ):


        self.validate_object_name(
            object_name
        )


        self.validate_fields(
            fields
        )


        self.validate_duplicate_module(
            db,
            object_name,
        )


        return True




    # =====================================================
    # OBJECT NAME VALIDATION
    # =====================================================

    def validate_object_name(
        self,
        object_name: str,
    ):


        if not object_name:

            raise DesignerValidationError(
                "Object name is required."
            )



        if len(object_name) < 3:

            raise DesignerValidationError(
                "Object name must contain minimum 3 characters."
            )



        if not re.match(
            r"^[A-Za-z][A-Za-z0-9_ ]*$",
            object_name,
        ):

            raise DesignerValidationError(
                "Object name contains invalid characters."
            )



    # =====================================================
    # FIELD VALIDATION
    # =====================================================

    def validate_fields(
        self,
        fields: list,
    ):


        if not fields:

            raise DesignerValidationError(
                "At least one field is required."
            )



        field_names = set()



        for field in fields:


            name = (

                field.name
                if hasattr(
                    field,
                    "name",
                )
                else field.get(
                    "name"
                )

            )



            if not name:

                raise DesignerValidationError(
                    "Field name cannot be empty."
                )



            self.validate_field_name(
                name
            )



            if name in field_names:

                raise DesignerValidationError(
                    f"Duplicate field: {name}"
                )



            field_names.add(
                name
            )



    # =====================================================
    # FIELD NAME VALIDATION
    # =====================================================

    def validate_field_name(
        self,
        field_name: str,
    ):


        if not re.match(
            r"^[a-z][a-z0-9_]*$",
            field_name,
        ):

            raise DesignerValidationError(
                f"Invalid field name: {field_name}"
            )



        if field_name.lower() in self.RESERVED_WORDS:

            raise DesignerValidationError(
                f"Reserved SQL word not allowed: {field_name}"
            )



    # =====================================================
    # DUPLICATE MODULE CHECK
    # =====================================================

    def validate_duplicate_module(
        self,
        db: Session,
        object_name: str,
    ):


        module_code = (

            object_name
            .lower()
            .replace(
                " ",
                "_",
            )

        )


        existing = (

            self.repository
            .get_module_by_code(
                db,
                module_code,
            )

        )



        if existing:

            raise DesignerValidationError(

                f"Business object '{object_name}' already exists."

            )





designer_validation_service = DesignerValidationService()