from app.platform.designer.runtime_sync.runtime_crud_service import (
    runtime_crud_service,
)

from app.database.session import SessionLocal


db = SessionLocal()


result = runtime_crud_service.update(

    db,

    12,

    8,

    {
        "warehouse_code": "WH02"
    },

    user="nishant",

)


print()

print("UPDATE RESULT")

print("-------------")

print(result)



record = runtime_crud_service.get(

    db,

    12,

    8

)


print()

print("UPDATED RECORD")

print("----------------")

print(record)



db.close()