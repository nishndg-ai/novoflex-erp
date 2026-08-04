from __future__ import annotations

from sqlalchemy.orm import Session


from app.platform.metadata.models.metadata_field import (
    MetadataField,
)


class RuntimeSchemaService:
    """
    BLUISH Runtime Schema Synchronization Service

    Converts metadata definitions into
    runtime object schemas.

    Flow:

        metadata_fields

              |

              ↓

        Runtime Schema

              |

              ↓

        Dynamic CRUD Engine

              |

              ↓

        UI Generator
    """



    # =====================================================
    # GET RUNTIME SCHEMA
    # =====================================================

    def get_runtime_schema(

        self,

        db: Session,

        module_id: int,

    ):


        fields = (

            db.query(

                MetadataField

            )

            .filter(

                MetadataField.module_id == module_id

            )

            .order_by(

                MetadataField.display_order

            )

            .all()

        )



        schema_fields = []



        for field in fields:


            schema_fields.append(

                {


                    "field":

                        field.field_name,


                    "label":

                        field.display_name,


                    "data_type":

                        field.data_type,


                    "control_type":

                        field.control_type,


                    "length":

                        field.length,


                    "required":

                        field.is_required,


                    "unique":

                        field.is_unique,


                    "show_in_grid":

                        field.show_in_grid,


                    "searchable":

                        field.is_searchable,


                    "filterable":

                        field.is_filterable,


                }

            )



        return {


            "success":

                True,


            "module_id":

                module_id,


            "field_count":

                len(schema_fields),


            "fields":

                schema_fields,

        }





    # =====================================================
    # GET SINGLE FIELD MAP
    # =====================================================

    def get_field_map(

        self,

        db: Session,

        module_id: int,

    ):


        schema = self.get_runtime_schema(

            db,

            module_id,

        )


        return {


            field["field"]:

                field

            for field in schema["fields"]

        }





runtime_schema_service = RuntimeSchemaService()