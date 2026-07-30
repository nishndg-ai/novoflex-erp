from __future__ import annotations

from sqlalchemy.orm import Session


class ValidationError(Exception):
    pass



class RuntimeValidator:
    """
    Runtime metadata based validation.

    Supports:
    - Create validation
    - Partial update validation
    - Length validation
    - Unique validation
    """

    def validate(
        self,
        db: Session,
        fields,
        values: dict,
        table,
        is_update: bool = False,
    ) -> None:


        for field in fields:


            value = values.get(
                field.field_name
            )


            # -------------------------------------------------
            # Required Validation
            # -------------------------------------------------

            if field.is_required:


                # CREATE
                # All required fields must be present

                if not is_update:


                    if value in (
                        None,
                        "",
                    ):

                        raise ValidationError(
                            f"{field.display_name} is required."
                        )


                # UPDATE
                # Validate only fields being changed

                else:


                    if (
                        field.field_name in values
                        and value in (
                            None,
                            "",
                        )
                    ):

                        raise ValidationError(
                            f"{field.display_name} is required."
                        )



            # -------------------------------------------------
            # Length Validation
            # -------------------------------------------------

            if field.length:


                if value is not None:


                    if (
                        isinstance(value, str)
                        and len(value) > field.length
                    ):

                        raise ValidationError(
                            f"{field.display_name} cannot exceed {field.length} characters."
                        )



            # -------------------------------------------------
            # Unique Validation
            # -------------------------------------------------

            if field.is_unique:


                if value not in (
                    None,
                    "",
                ):


                    query = (

                        db.query(table)

                        .filter(

                            getattr(
                                table.c,
                                field.field_name
                            ) == value

                        )

                    )


                    # Ignore current record during update

                    if is_update:


                        record_id = values.get(
                            "id"
                        )


                        if record_id:


                            query = query.filter(

                                table.c.id != record_id

                            )


                    exists = query.first()


                    if exists:


                        raise ValidationError(

                            f"{field.display_name} '{value}' already exists."

                        )