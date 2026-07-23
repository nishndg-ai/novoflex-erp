from sqlalchemy import Column, Integer, String, Boolean, DateTime, func

from app.database.base import Base


class UOM(Base):
    __tablename__ = "uom"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), unique=True, nullable=False)
    code = Column(String(50), unique=True, nullable=False)
    description = Column(String(255), nullable=True)

    is_active = Column(Boolean, default=True)

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())