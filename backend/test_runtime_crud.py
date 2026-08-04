from app.platform.designer.runtime_sync.runtime_crud_service import (
    runtime_crud_service,
)

from app.database.session import SessionLocal



db = SessionLocal()



module_id = 12



# =====================================================
# CREATE TEST RECORD
# =====================================================

data = {

    "location_code":
        "LOC001",

    "location_name":
        "Main Plant",

    "warehouse_code":
        "WH01",

    "storage_location":
        "Rack-A",

    "is_active":
        True,

}



result = runtime_crud_service.create(

    db,

    module_id,

    data,

)



print()

print("CREATE RESULT")

print("-------------")

print(result)



# =====================================================
# READ LIST
# =====================================================

records = runtime_crud_service.list(

    db,

    module_id,

)



print()

print("LIST RESULT")

print("-----------")

print(records)



db.close()