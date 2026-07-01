from fastapi import APIRouter

router = APIRouter()

@router.post("/login")
def login(username: str, password: str):

    if username == "admin" and password == "admin123":

        return {
            "success": True,
            "user": {
                "name": "Administrator",
                "role": "Corporate Admin",
                "company": "NovoFlex Industries Pvt Ltd",
                "plant": "Head Office"
            }
        }

    return {
        "success": False,
        "message": "Invalid Username or Password"
    }