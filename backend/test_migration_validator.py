from app.platform.designer.change_engine.migration.validator import (
    migration_validator,
)


from app.database.session import SessionLocal



# =====================================================
# DATABASE SESSION
# =====================================================

db = SessionLocal()



# =====================================================
# TEST VALID MIGRATION PLAN
# =====================================================

migration_plan = {


    "success":

        True,


    "table":

        "test_location",


    "action_count":

        1,


    "actions":

        [

            {

                "action":

                    "ADD_COLUMN",


                "table":

                    "test_location",


                "field":

                    "warehouse_code",


                "data_type":

                    "VARCHAR(50)",

            }

        ]

}




# =====================================================
# VALIDATE MIGRATION
# =====================================================

result = migration_validator.validate(

    db,

    migration_plan,

)



print()

print("VALIDATION RESULT")

print("-----------------")

print(result)



# =====================================================
# CLOSE DATABASE
# =====================================================

db.close()