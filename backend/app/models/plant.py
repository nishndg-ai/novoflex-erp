from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base_model import BaseModel


class Plant(BaseModel):
    __tablename__ = "plants"

    company_id: Mapped[int] = mapped_column(
        ForeignKey("company.id"),
        nullable=False,
    )

    company = relationship("Company")

    code: Mapped[str] = mapped_column(
        String(20),
        unique=True,
        nullable=False,
    )

    name: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    address: Mapped[str] = mapped_column(
        String(255),
        default="",
    )

    city: Mapped[str] = mapped_column(
        String(100),
        default="",
    )

    state: Mapped[str] = mapped_column(
        String(100),
        default="",
    )

    country: Mapped[str] = mapped_column(
        String(100),
        default="India",
    )

    pincode: Mapped[str] = mapped_column(
        String(20),
        default="",
    )

    phone: Mapped[str] = mapped_column(
        String(20),
        default="",
    )

    email: Mapped[str] = mapped_column(
        String(120),
        default="",
    )