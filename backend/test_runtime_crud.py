from app.platform.designer.runtime_sync.runtime_crud_service import (
    runtime_crud_service,
)

from app.database.session import SessionLocal



db = SessionLocal()



data = {

    "location_code":
        "LOC002",

    "location_name":
        "Second Plant",

    "warehouse_code":
        "WH01",

    "storage_location":
        "Rack-B",

    "is_active":
        True,

}



result = runtime_crud_service.create(

    db,

    12,

    data,

    user="system",

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