from app.platform.designer.sync_engine.metadata_sync_service import (
    metadata_sync_service,
)


from app.database.session import SessionLocal



db = SessionLocal()



# =====================================================
# TEST MODULE
# =====================================================

module_id = 12



# =====================================================
# TEST ADD FIELD CHANGE
# =====================================================

changes = [

    {

        "type": "ADD_FIELD",

        "field": "warehouse_code",

        "new_definition": {

            "name": "warehouse_code",

            "label": "Warehouse Code",

            "data_type": "string",

            "control_type": "TEXTBOX",

            "length": 50,

            "required": False,

            "unique": False,

            "show_in_grid": True,

            "searchable": True,

            "filterable": True,

        }

    }

]



# =====================================================
# SYNC METADATA
# =====================================================

result = metadata_sync_service.sync_changes(

    db,

    module_id,

    changes,

)



print()

print("METADATA SYNC RESULT")

print("--------------------")

print(result)



db.close()