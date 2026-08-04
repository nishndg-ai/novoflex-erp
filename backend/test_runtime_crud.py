from app.platform.designer.runtime_sync.runtime_crud_service import (
    runtime_crud_service,
)

from app.database.session import SessionLocal



db = SessionLocal()



data = {

    "location_code":
        "LOC003",

    "location_name":
        "Third Plant",

    "warehouse_code":
        "WH01",

    "storage_location":
        "Rack-C",

    "is_active":
        True,

}



result = runtime_crud_service.create(

    db,

    12,

    data,

    user="nishant",

)



print()

print("CREATE RESULT")

print("-------------")

print(result)



records = runtime_crud_service.list(

    db,

    12,

)



print()

print("LIST RESULT")

print("-----------")

print(records)



db.close()