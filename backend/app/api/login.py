from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.services.auth_service import AuthService

from app.services.permission_service import PermissionService



router = APIRouter()


auth_service = AuthService()

permission_service = PermissionService()



@router.post("/login")
def login(
    user: dict,
    db: Session = Depends(get_db),
):


    username = user.get(
        "username"
    )


    password = user.get(
        "password"
    )


    authenticated_user = auth_service.authenticate(

        db,

        username,

        password,

    )


    if not authenticated_user:


        return {

            "success": False,

            "message":
                "Invalid Username or Password",

        }



    role_name = (
        authenticated_user.role.code
        if authenticated_user.role
        else None
    )


    permissions = (
        permission_service.get_role_permissions(
            db,
            role_name,
        )
        if role_name
        else []
    )



    return {


        "success": True,


        "token":
            "NOVOFLEX_TOKEN",


        "user": {


            "id":
                authenticated_user.id,


            "username":
                authenticated_user.username,


            "name":
                authenticated_user.full_name,


            "role":
                role_name,


            "company_id":
                authenticated_user.company_id,


            "plant_id":
                authenticated_user.plant_id,


        },


        "permissions":
            permissions,

    }