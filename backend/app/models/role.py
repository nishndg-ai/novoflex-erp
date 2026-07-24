from sqlalchemy import Column, Integer, String, Boolean, DateTime, func

from app.database.base import Base


class Role(Base):
    __tablename__ = "role"

    id = Column(Integer, primary_key=True, index=True)

    code = Column(String(20), unique=True, nullable=False)
    name = Column(String(100), nullable=False)

    description = Column(String(500), nullable=True)

    is_active = Column(Boolean, default=True)

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now(),
    )