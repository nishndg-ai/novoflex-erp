from __future__ import annotations

from typing import Any



class ImportValidator:
    """
    Pre-import validation engine.

    Validates imported rows before database insert.

    Returns structured error details:
    - column
    - invalid value
    - message
    """



    def validate(
        self,
        runtime,
        rows: list[dict[str, Any]],
    ) -> dict[str, Any]:


        valid_rows = []

        failed_rows = []



        for index, row in enumerate(
            rows,
            start=1
        ):


            errors = self.validate_row(
                runtime,
                row,
            )



            if errors:


                failed_rows.append(

                    {

                        "row":
                            index,


                        "errors":
                            errors,

                    }

                )


            else:


                valid_rows.append(
                    row
                )



        return {


            "total_rows":
                len(rows),


            "valid_rows":
                len(valid_rows),


            "failed_rows":
                len(failed_rows),


            "valid_data":
                valid_rows,


            "errors":
                failed_rows,

        }




    def validate_row(
        self,
        runtime,
        row: dict[str, Any],
    ) -> list[dict[str, Any]]:


        errors = []



        for field in runtime.fields:



            if field.is_required:


                value = row.get(
                    field.field_name
                )



                if value in (
                    None,
                    "",
                ):


                    display_name = (

                        getattr(
                            field,
                            "display_name",
                            None
                        )

                        or

                        field.field_name

                    )



                    errors.append(

                        {


                            "column":
                                display_name,


                            "value":
                                "BLANK",


                            "message":
                                f"{display_name} is required.",


                        }

                    )



        return errors