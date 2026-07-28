from __future__ import annotations

from sqlalchemy.orm import Session


class ValidationError(Exception):
    pass



class RuntimeValidator:
    """
    Runtime metadata based validation.
    """

    def validate(
        self,
        db: Session,
        fields,
        values: dict,
        table,
    ) -> None:


        for field in fields:


            # -----------------------------
            # Required Validation
            # -----------------------------

            if field.is_required:

                value = values.get(
                    field.field_name
                )


                if value in (
                    None,
                    "",
                ):

                    raise ValidationError(
                        f"{field.display_name} is required."
                    )



            # -----------------------------
            # Length Validation
            # -----------------------------

            if field.length:

                value = values.get(
                    field.field_name
                )


                if (
                    isinstance(value, str)
                    and len(value) > field.length
                ):

                    raise ValidationError(
                        f"{field.display_name} cannot exceed {field.length} characters."
                    )



            # -----------------------------
            # Unique Validation
            # -----------------------------

            if field.is_unique:

                value = values.get(
                    field.field_name
                )


                if value not in (
                    None,
                    "",
                ):

                    exists = (
                        db.query(table)
                        .filter(
                            getattr(
                                table.c,
                                field.field_name
                            ) == value
                        )
                        .first()
                    )


                    if exists:

                        raise ValidationError(
                            f"{field.display_name} '{value}' already exists."
                        )