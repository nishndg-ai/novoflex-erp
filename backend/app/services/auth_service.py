from sqlalchemy.orm import Session

from passlib.context import CryptContext

from app.models.user import User



pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto",
)



class AuthService:


    def verify_password(
        self,
        plain_password,
        hashed_password,
    ):

        return pwd_context.verify(
            plain_password,
            hashed_password,
        )



    def get_user_by_username(
        self,
        db: Session,
        username: str,
    ):


        return (

            db.query(User)

            .filter(
                User.username == username
            )

            .first()

        )



    def authenticate(
        self,
        db: Session,
        username: str,
        password: str,
    ):


        user = self.get_user_by_username(
            db,
            username,
        )


        if not user:

            return None


        if not user.is_active:

            return None


        if not self.verify_password(
            password,
            user.password_hash,
        ):

            return None


        return user