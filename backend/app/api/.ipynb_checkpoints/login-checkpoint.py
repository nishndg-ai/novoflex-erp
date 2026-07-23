from fastapi import APIRouter

router = APIRouter()

@router.post("/login")
def login(user: dict):

    if (
        user["username"] == "admin"
        and user["password"] == "admin"
    ):
        return {
            "success": True,
            "token": "NOVOFLEX_DEMO_TOKEN",
            "name": "Administrator",
        }

    return {
        "success": False,
        "message": "Invalid Username or Password",
    }