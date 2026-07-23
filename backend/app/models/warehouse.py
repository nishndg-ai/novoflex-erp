from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database.base import Base


class Warehouse(Base):
    __tablename__ = "warehouses"

    id = Column(Integer, primary_key=True, index=True)

    plant_id = Column(
        Integer,
        ForeignKey("plants.id"),
        nullable=False,
    )

    code = Column(String(20), nullable=False)

    name = Column(String(100), nullable=False)

    warehouse_type = Column(String(20), nullable=False)

    default_store = Column(Boolean, default=False)

    is_active = Column(Boolean, default=True)

    plant = relationship("Plant")