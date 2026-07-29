from fastapi import Depends, HTTPException, status

from fastapi.security import OAuth2PasswordBearer

from app.services.token_service import TokenService



oauth2_scheme = OAuth2PasswordBearer(

    tokenUrl="/token"

)



token_service = TokenService()



def get_current_user(

    token: str = Depends(
        oauth2_scheme
    ),

):


    try:


        payload = token_service.decode_token(

            token

        )


        return payload



    except Exception:


        raise HTTPException(

            status_code=status.HTTP_401_UNAUTHORIZED,

            detail="Invalid or expired token",

            headers={

                "WWW-Authenticate":
                    "Bearer"

            },

        )