from __future__ import annotations

from sqlalchemy.orm import Session

from sqlalchemy import text



class MigrationExecutor:
    """
    BLUISH Migration Executor

    Executes validated migration plans.

    Supported actions:

        ADD_COLUMN
        MODIFY_COLUMN
        REMOVE_COLUMN


    Flow:

        Validated Migration Plan

                |
                ↓

        Migration Executor

                |
                ↓

        Database Transaction

                |
                ↓

        Runtime Object Updated
    """



    # =====================================================
    # EXECUTE MIGRATION PLAN
    # =====================================================

    def execute(

        self,

        db: Session,

        migration_plan: dict,

    ) -> dict:


        executed_actions = []



        try:


            for action in migration_plan.get(

                "actions",

                []

            ):


                result = self.execute_action(

                    db,

                    action,

                )


                executed_actions.append(

                    result

                )



            db.commit()



            return {


                "success":

                    True,


                "executed_count":

                    len(executed_actions),


                "actions":

                    executed_actions,

            }




        except Exception as e:


            db.rollback()



            return {


                "success":

                    False,


                "error":

                    str(e),


            }





    # =====================================================
    # EXECUTE SINGLE ACTION
    # =====================================================

    def execute_action(

        self,

        db: Session,

        action: dict,

    ) -> dict:


        action_type = action.get(

            "action"

        )


        if action_type == "ADD_COLUMN":


            return self.add_column(

                db,

                action,

            )



        elif action_type == "MODIFY_COLUMN":


            return self.modify_column(

                db,

                action,

            )



        elif action_type == "REMOVE_COLUMN":


            return self.remove_column(

                db,

                action,

            )



        else:


            raise Exception(

                f"Unsupported action {action_type}"

            )





    # =====================================================
    # ADD COLUMN
    # =====================================================

    def add_column(

        self,

        db: Session,

        action: dict,

    ) -> dict:


        sql = f"""

        ALTER TABLE {action['table']}

        ADD COLUMN {action['field']}

        {action['data_type']}

        """



        db.execute(

            text(sql)

        )



        return {


            "action":

                "ADD_COLUMN",


            "table":

                action["table"],


            "field":

                action["field"],


            "status":

                "EXECUTED",

        }





    # =====================================================
    # MODIFY COLUMN
    # =====================================================

    def modify_column(

        self,

        db: Session,

        action: dict,

    ) -> dict:


        sql = f"""

        ALTER TABLE {action['table']}

        ALTER COLUMN {action['field']}

        TYPE {action['data_type']}

        """



        db.execute(

            text(sql)

        )



        return {


            "action":

                "MODIFY_COLUMN",


            "table":

                action["table"],


            "field":

                action["field"],


            "status":

                "EXECUTED",

        }





    # =====================================================
    # REMOVE COLUMN
    # =====================================================

    def remove_column(

        self,

        db: Session,

        action: dict,

    ) -> dict:


        sql = f"""

        ALTER TABLE {action['table']}

        DROP COLUMN {action['field']}

        """



        db.execute(

            text(sql)

        )



        return {


            "action":

                "REMOVE_COLUMN",


            "table":

                action["table"],


            "field":

                action["field"],


            "status":

                "EXECUTED",

        }





migration_executor = MigrationExecutor()