from app.platform.designer.runtime_sync.runtime_validation_sync import (
    runtime_validation_sync,
)


from app.database.session import SessionLocal



db = SessionLocal()



module_id = 12



# =====================================================
# TEST 1 — VALID DATA
# =====================================================

valid_data = {


    "location_code":

        "LOC001",


    "location_name":

        "Main Plant",


    "warehouse_code":

        "WH01",


}



valid_result = runtime_validation_sync.validate(

    db,

    module_id,

    valid_data,

)



print()

print("VALID DATA RESULT")

print("-----------------")

print(valid_result)





# =====================================================
# TEST 2 — INVALID DATA
# =====================================================

invalid_data = {


    "location_name":

        "Main Plant",


    "abc_test":

        "123",


}



invalid_result = runtime_validation_sync.validate(

    db,

    module_id,

    invalid_data,

)



print()

print("INVALID DATA RESULT")

print("-------------------")

print(invalid_result)



db.close()