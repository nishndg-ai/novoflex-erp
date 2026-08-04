from __future__ import annotations

from sqlalchemy.orm import Session


from app.platform.metadata.models.metadata_field import (
    MetadataField,
)


class MetadataSyncService:
    """
    BLUISH Metadata Synchronization Service

    Synchronizes approved runtime changes
    with BLUISH metadata engine.

    Flow:

        Migration Applied

              |
              ↓

        Metadata Sync

              |
              ↓

        metadata_fields

              |
              ↓

        Runtime ERP Updates
    """



    # =====================================================
    # SYNC ADD FIELD
    # =====================================================

    def sync_add_field(

        self,

        db: Session,

        module_id: int,

        field_definition: dict,

    ):


        field_name = (

            field_definition["name"]

            .lower()

            .replace(

                " ",

                "_"

            )

        )



        existing = (

            db.query(

                MetadataField

            )

            .filter(

                MetadataField.module_id == module_id,

                MetadataField.field_name == field_name,

            )

            .first()

        )



        if existing:


            raise Exception(

                f"Metadata field '{field_name}' already exists."

            )



        metadata_field = MetadataField(


            module_id=module_id,


            field_name=field_name,


            display_name=

                field_definition.get(

                    "label",

                    field_name,

                ),


            data_type=

                field_definition.get(

                    "data_type",

                    "string",

                ),


            control_type=

                field_definition.get(

                    "control_type",

                    "TEXTBOX",

                ),


            length=

                field_definition.get(

                    "length",

                    150,

                ),


            is_required=

                field_definition.get(

                    "required",

                    False,

                ),


            is_unique=

                field_definition.get(

                    "unique",

                    False,

                ),


            show_in_grid=

                field_definition.get(

                    "show_in_grid",

                    True,

                ),


            is_searchable=

                field_definition.get(

                    "searchable",

                    True,

                ),


            is_filterable=

                field_definition.get(

                    "filterable",

                    True,

                ),


        )



        db.add(

            metadata_field

        )


        db.commit()


        db.refresh(

            metadata_field

        )



        return metadata_field





    # =====================================================
    # SYNC MIGRATION ACTIONS
    # =====================================================

    def sync_changes(

        self,

        db: Session,

        module_id: int,

        changes: list,

    ):


        synced = []



        for change in changes:


            if change.get(

                "type"

            ) == "ADD_FIELD":


                field = self.sync_add_field(

                    db,

                    module_id,

                    change["new_definition"],

                )


                synced.append(

                    {

                        "field":

                            field.field_name,

                        "status":

                            "SYNCED",

                    }

                )



        return {


            "success":

                True,


            "synced_count":

                len(synced),


            "fields":

                synced,

        }





metadata_sync_service = MetadataSyncService()