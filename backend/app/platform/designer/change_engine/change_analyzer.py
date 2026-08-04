from __future__ import annotations

from typing import Any



class ChangeAnalyzer:
    """
    BLUISH Designer Change Analyzer

    Compares two object definitions and identifies
    structural changes.

    Supported changes:

        ADD_FIELD
        REMOVE_FIELD
        MODIFY_FIELD

    Flow:

        Version 1 Definition
                |
                ↓
          Change Analyzer
                |
                ↓
        Change Detection Result
                |
                ↓
          Change Plan Engine
    """



    # =====================================================
    # PUBLIC METHOD
    # =====================================================

    def analyze(

        self,

        old_definition: dict[str, Any],

        new_definition: dict[str, Any],

    ) -> dict[str, Any]:


        old_fields = self.extract_fields(

            old_definition

        )


        new_fields = self.extract_fields(

            new_definition

        )


        changes = []


        # =====================================================
        # DETECT ADDED AND MODIFIED FIELDS
        # =====================================================

        for field_name, new_field in new_fields.items():


            if field_name not in old_fields:


                changes.append(

                    {

                        "type":
                            "ADD_FIELD",

                        "field":
                            field_name,

                        "new_definition":
                            new_field,

                    }

                )


            else:


                old_field = old_fields[field_name]


                if self.field_changed(

                    old_field,

                    new_field,

                ):


                    changes.append(

                        {

                            "type":
                                "MODIFY_FIELD",

                            "field":
                                field_name,

                            "old_definition":
                                old_field,

                            "new_definition":
                                new_field,

                        }

                    )



        # =====================================================
        # DETECT REMOVED FIELDS
        # =====================================================

        for field_name, old_field in old_fields.items():


            if field_name not in new_fields:


                changes.append(

                    {

                        "type":
                            "REMOVE_FIELD",

                        "field":
                            field_name,

                        "old_definition":
                            old_field,

                    }

                )



        return {


            "success":
                True,


            "change_count":
                len(changes),


            "changes":
                changes,

        }




    # =====================================================
    # FIELD EXTRACTION
    # =====================================================

    def extract_fields(

        self,

        definition: dict[str, Any],

    ) -> dict[str, dict]:


        fields = {}


        for field in definition.get(

            "fields",

            [],

        ):


            name = field.get(

                "name"

            )


            if name:

                fields[name] = field



        return fields




    # =====================================================
    # FIELD COMPARISON
    # =====================================================

    def field_changed(

        self,

        old_field: dict,

        new_field: dict,

    ) -> bool:


        compare_keys = [

            "label",

            "data_type",

            "control_type",

            "length",

            "required",

            "unique",

        ]



        for key in compare_keys:


            if old_field.get(key) != new_field.get(key):

                return True



        return False





change_analyzer = ChangeAnalyzer()