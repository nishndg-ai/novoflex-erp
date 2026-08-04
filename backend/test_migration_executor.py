from app.platform.designer.change_engine.migration.executor import (
    migration_executor,
)

from app.database.session import SessionLocal



db = SessionLocal()



migration_plan = {

    "success": True,

    "table": "test_location",

    "action_count": 1,

    "actions": [

        {

            "action": "ADD_COLUMN",

            "table": "test_location",

            "field": "warehouse_code",

            "data_type": "VARCHAR(50)",

        }

    ]

}



result = migration_executor.execute(

    db,

    migration_plan,

)



print()

print("EXECUTION RESULT")

print("----------------")

print(result)



db.close()