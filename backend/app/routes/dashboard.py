from fastapi import APIRouter

router = APIRouter()

@router.get("/dashboard")
def dashboard():

    return {

        "company": "NovoFlex Group",

        "plants": [
            "Head Office",
            "Unit 1",
            "Unit 2",
            "Novoflex Marketing Pvt Ltd"
        ],

        "today":{

            "production":125000,

            "dispatch":83000,

            "rejection":1.2,

            "pending_orders":18,

            "quality_alerts":2,

            "employees_present":146

        }

    }