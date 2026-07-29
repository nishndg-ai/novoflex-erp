from datetime import datetime, timedelta, timezone

from jose import jwt



SECRET_KEY = "NOVOFLEX_SECRET_KEY_CHANGE_LATER"

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 60



class TokenService:


    def create_access_token(
        self,
        data: dict,
    ):


        to_encode = data.copy()


        expire = datetime.now(
            timezone.utc
        ) + timedelta(
            minutes=ACCESS_TOKEN_EXPIRE_MINUTES
        )


        to_encode.update(
            {
                "exp": expire
            }
        )


        return jwt.encode(
            to_encode,
            SECRET_KEY,
            algorithm=ALGORITHM,
        )



    def decode_token(
        self,
        token: str,
    ):


        return jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[
                ALGORITHM
            ],
        )