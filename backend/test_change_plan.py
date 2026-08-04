from app.platform.designer.change_engine.change_analyzer import (
    change_analyzer,
)


from app.platform.designer.change_engine.change_plan import (
    change_plan_generator,
)



# =====================================================
# VERSION 1
# =====================================================

version_1 = {

    "object_name": "Test Location",

    "fields": [

        {
            "name": "location_code",
            "label": "Location Code",
            "data_type": "string",
            "control_type": "TEXTBOX",
            "length": 50,
            "required": True,
            "unique": True,
        },

        {
            "name": "location_name",
            "label": "Location Name",
            "data_type": "string",
            "control_type": "TEXTBOX",
            "length": 150,
            "required": True,
            "unique": False,
        },

    ]

}



# =====================================================
# VERSION 2
# =====================================================

version_2 = {

    "object_name": "Test Location",

    "fields": [

        {
            "name": "location_code",
            "label": "Location Code",
            "data_type": "string",
            "control_type": "TEXTBOX",
            "length": 50,
            "required": True,
            "unique": True,
        },

        {
            "name": "location_name",
            "label": "Location Name",
            "data_type": "string",
            "control_type": "TEXTBOX",
            "length": 150,
            "required": True,
            "unique": False,
        },

        {
            "name": "storage_location",
            "label": "Storage Location",
            "data_type": "string",
            "control_type": "TEXTBOX",
            "length": 100,
            "required": False,
            "unique": False,
        },

    ]

}




# =====================================================
# ANALYZE CHANGE
# =====================================================

analysis = change_analyzer.analyze(

    version_1,

    version_2,

)


print("\nCHANGE ANALYSIS")
print("----------------")

print(

    analysis

)




# =====================================================
# GENERATE PLAN
# =====================================================

plan = change_plan_generator.generate(

    analysis,

    table_name="test_location",

)


print("\nCHANGE PLAN")
print("----------------")

print(

    plan

)