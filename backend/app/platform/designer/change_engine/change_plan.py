from __future__ import annotations

from typing import Any



class ChangePlanGenerator:
    """
    BLUISH Change Plan Generator

    Converts detected object changes into
    executable ERP migration actions.

    Flow:

        Change Analyzer
              |
              ↓
        Change Plan
              |
              ↓
        Migration Executor
    """



    # =====================================================
    # PUBLIC METHOD
    # =====================================================

    def generate(

        self,

        analysis_result: dict[str, Any],

        table_name: str,

    ) -> dict[str, Any]:


        plans = []


        for change in analysis_result.get(

            "changes",

            []

        ):


            change_type = change.get(

                "type"

            )


            if change_type == "ADD_FIELD":


                plans.append(

                    self.create_add_field_plan(

                        change,

                        table_name,

                    )

                )



            elif change_type == "MODIFY_FIELD":


                plans.append(

                    self.create_modify_field_plan(

                        change,

                        table_name,

                    )

                )



            elif change_type == "REMOVE_FIELD":


                plans.append(

                    self.create_remove_field_plan(

                        change,

                        table_name,

                    )

                )



        return {


            "success":

                True,


            "table":

                table_name,


            "action_count":

                len(plans),


            "actions":

                plans,

        }





    # =====================================================
    # ADD FIELD
    # =====================================================

    def create_add_field_plan(

        self,

        change: dict,

        table_name: str,

    ) -> dict:


        field = change["new_definition"]


        return {


            "action":

                "ADD_COLUMN",


            "table":

                table_name,


            "field":

                change["field"],


            "data_type":

                self.map_database_type(

                    field

                ),


        }





    # =====================================================
    # MODIFY FIELD
    # =====================================================

    def create_modify_field_plan(

        self,

        change: dict,

        table_name: str,

    ) -> dict:


        field = change["new_definition"]


        return {


            "action":

                "MODIFY_COLUMN",


            "table":

                table_name,


            "field":

                change["field"],


            "data_type":

                self.map_database_type(

                    field

                ),


        }





    # =====================================================
    # REMOVE FIELD
    # =====================================================

    def create_remove_field_plan(

        self,

        change: dict,

        table_name: str,

    ) -> dict:


        return {


            "action":

                "REMOVE_COLUMN",


            "table":

                table_name,


            "field":

                change["field"],

        }





    # =====================================================
    # DATA TYPE MAPPING
    # =====================================================

    def map_database_type(

        self,

        field: dict,

    ) -> str:


        data_type = field.get(

            "data_type"

        )


        length = field.get(

            "length",

            150,

        )


        mapping = {


            "string":

                f"VARCHAR({length})",


            "integer":

                "INTEGER",


            "decimal":

                "DECIMAL",


            "boolean":

                "BOOLEAN",


            "date":

                "DATE",

        }


        return mapping.get(

            data_type,

            "VARCHAR(150)",

        )





change_plan_generator = ChangePlanGenerator()