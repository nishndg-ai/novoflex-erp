from fastapi import Depends, HTTPException, status

from app.core.security import get_current_user



def require_permission(
    module_code: str,
    action: str,
):


    def permission_checker(

        current_user: dict = Depends(
            get_current_user
        ),

    ):


        permissions = current_user.get(
            "permissions",
            []
        )


        for permission in permissions:


            if (

                permission.get("module_code")
                == module_code

            ):


                allowed = permission.get(
                    f"can_{action}",
                    False,
                )


                if allowed:

                    return current_user



        raise HTTPException(

            status_code=status.HTTP_403_FORBIDDEN,

            detail="Permission denied",

        )


    return permission_checker