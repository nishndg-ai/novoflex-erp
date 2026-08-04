from __future__ import annotations

from sqlalchemy.orm import Session


from app.platform.designer.runtime_sync.runtime_schema_service import (
    runtime_schema_service,
)



class RuntimeValidationSync:
    """
    BLUISH Runtime Validation Synchronization Engine

    Validates runtime data dynamically using
    metadata-driven runtime schema.

    Flow:

        API Request

             |

             ↓

        Runtime Schema

             |

             ↓

        Validation Engine

             |

             ↓

        Runtime CRUD

    """



    # =====================================================
    # VALIDATE DATA
    # =====================================================

    def validate(

        self,

        db: Session,

        module_id: int,

        data: dict,

    ):


        schema = runtime_schema_service.get_runtime_schema(

            db,

            module_id,

        )


        fields = {


            field["field"]:

                field

            for field in schema["fields"]

        }



        errors = []



        # =====================================================
        # UNKNOWN FIELD CHECK
        # =====================================================

        for key in data.keys():


            if key not in fields:


                errors.append(

                    f"Field '{key}' is not defined for this object."

                )



        # =====================================================
        # REQUIRED FIELD CHECK
        # =====================================================

        for field_name, field in fields.items():


            if field.get(

                "required",

                False,

            ):


                if (

                    field_name not in data

                    or data[field_name] in (

                        None,

                        "",

                    )

                ):


                    errors.append(

                        f"Field '{field_name}' is required."

                    )



        return {


            "success":

                len(errors) == 0,


            "valid":

                len(errors) == 0,


            "errors":

                errors,

        }





runtime_validation_sync = RuntimeValidationSync()