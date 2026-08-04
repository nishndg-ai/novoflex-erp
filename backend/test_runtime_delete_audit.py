from app.platform.designer.runtime_sync.runtime_crud_service import (
    runtime_crud_service,
)

from app.database.session import SessionLocal



db = SessionLocal()



result = runtime_crud_service.soft_delete(

    db,

    12,

    6,

    user="nishant",

)



print()

print("DELETE RESULT")

print("-------------")

print(result)



record = runtime_crud_service.get(

    db,

    12,

    6,

)



print()

print("AFTER DELETE")

print("------------")

print(record)



db.close()