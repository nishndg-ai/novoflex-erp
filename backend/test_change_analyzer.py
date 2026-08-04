from app.platform.designer.change_engine.change_analyzer import (
    change_analyzer,
)



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



result = change_analyzer.analyze(

    version_1,

    version_2,

)



print(result)