from __future__ import annotations

from sqlalchemy.orm import Session


from sqlalchemy import inspect



class MigrationValidator:
    """
    BLUISH Migration Validator

    Validates migration actions before execution.

    Checks:

        - Supported action
        - Table existence
        - Column existence
        - Duplicate column creation

    Flow:

        Change Plan

             |
             ↓

        Migration Validator

             |
             ↓

        Migration Executor
    """



    # =====================================================
    # PUBLIC VALIDATION METHOD
    # =====================================================

    def validate(

        self,

        db: Session,

        migration_plan: dict,

    ) -> dict:


        errors = []

        actions = migration_plan.get(

            "actions",

            []

        )


        for action in actions:


            result = self.validate_action(

                db,

                action,

            )


            if not result["valid"]:


                errors.extend(

                    result["errors"]

                )



        return {


            "success":

                len(errors) == 0,


            "valid":

                len(errors) == 0,


            "errors":

                errors,

        }




    # =====================================================
    # ACTION VALIDATION
    # =====================================================

    def validate_action(

        self,

        db: Session,

        action: dict,

    ) -> dict:


        errors = []


        action_type = action.get(

            "action"

        )


        table = action.get(

            "table"

        )


        field = action.get(

            "field"

        )



        supported_actions = [

            "ADD_COLUMN",

            "MODIFY_COLUMN",

            "REMOVE_COLUMN",

        ]



        if action_type not in supported_actions:


            errors.append(

                f"Unsupported migration action: {action_type}"

            )



            return {


                "valid":

                    False,


                "errors":

                    errors,

            }




        inspector = inspect(

            db.bind

        )


        tables = inspector.get_table_names()



        if table not in tables:


            errors.append(

                f"Table '{table}' does not exist."

            )


            return {


                "valid":

                    False,


                "errors":

                    errors,

            }



        columns = [

            column["name"]

            for column in inspector.get_columns(

                table

            )

        ]



        # =====================================================
        # ADD COLUMN VALIDATION
        # =====================================================

        if action_type == "ADD_COLUMN":


            if field in columns:


                errors.append(

                    f"Column '{field}' already exists."

                )



        # =====================================================
        # MODIFY COLUMN VALIDATION
        # =====================================================

        if action_type == "MODIFY_COLUMN":


            if field not in columns:


                errors.append(

                    f"Column '{field}' does not exist."

                )



        # =====================================================
        # REMOVE COLUMN VALIDATION
        # =====================================================

        if action_type == "REMOVE_COLUMN":


            if field not in columns:


                errors.append(

                    f"Column '{field}' does not exist."

                )



        return {


            "valid":

                len(errors) == 0,


            "errors":

                errors,

        }





migration_validator = MigrationValidator()