from sqlalchemy import Column, Integer, String, Boolean, DateTime, func

from app.database.base import Base


class Company(Base):
    __tablename__ = "company"

    id = Column(Integer, primary_key=True, index=True)

    code = Column(String(20), unique=True, nullable=False)
    name = Column(String(200), nullable=False)

    gstin = Column(String(20), nullable=True)
    pan = Column(String(20), nullable=True)
    cin = Column(String(30), nullable=True)

    email = Column(String(100), nullable=True)
    phone = Column(String(20), nullable=True)

    address = Column(String(500), nullable=True)

    is_active = Column(Boolean, default=True)

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now(),
    )