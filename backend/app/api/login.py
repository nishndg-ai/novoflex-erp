from fastapi import APIRouter

router = APIRouter()

@router.post("/login")
def login(user: dict):

    print("Login Request:", user)

    username = user.get("username")
    password = user.get("password")

    if username == "admin" and password == "admin":
        return {
            "success": True,
            "token": "NOVOFLEX_DEMO_TOKEN",
            "name": "Administrator",
        }

    return {
        "success": False,
        "message": "Invalid Username or Password",
    }