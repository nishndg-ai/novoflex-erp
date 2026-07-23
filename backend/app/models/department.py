from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base_model import BaseModel


class Department(BaseModel):
    __tablename__ = "departments"

    code: Mapped[str] = mapped_column(
        String(10),
        unique=True,
        nullable=False,
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )