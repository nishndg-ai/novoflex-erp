from app.platform.designer.runtime_sync.runtime_schema_service import (
    runtime_schema_service,
)


from app.database.session import SessionLocal



# =====================================================
# DATABASE SESSION
# =====================================================

db = SessionLocal()



# =====================================================
# TEST MODULE
# =====================================================

module_id = 12



# =====================================================
# GET RUNTIME SCHEMA
# =====================================================

result = runtime_schema_service.get_runtime_schema(

    db,

    module_id,

)



print()

print("RUNTIME SCHEMA RESULT")

print("---------------------")

print(result)



# =====================================================
# FIELD MAP TEST
# =====================================================

field_map = runtime_schema_service.get_field_map(

    db,

    module_id,

)



print()

print("FIELD MAP")

print("---------------------")

print(field_map)



db.close()