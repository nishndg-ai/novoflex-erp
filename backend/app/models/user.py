from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
    ForeignKey,
)

from sqlalchemy.orm import relationship

from app.database.base import Base



class User(Base):

    __tablename__ = "users"


    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )


    username = Column(
        String(50),
        unique=True,
        nullable=False,
    )


    password_hash = Column(
        String(255),
        nullable=False,
    )


    full_name = Column(
        String(150),
        nullable=False,
    )


    email = Column(
        String(150),
        nullable=True,
    )


    role_id = Column(
        Integer,
        ForeignKey(
            "role.id"
        ),
        nullable=False,
    )


    company_id = Column(
        Integer,
        ForeignKey(
            "company.id"
        ),
        nullable=False,
    )


    plant_id = Column(
        Integer,
        ForeignKey(
            "plants.id"
        ),
        nullable=True,
    )


    is_active = Column(
        Boolean,
        default=True,
    )


    created_at = Column(
        DateTime,
        default=datetime.utcnow,
    )


    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )


    role = relationship(
        "Role"
    )


    company = relationship(
        "Company"
    )


    plant = relationship(
        "Plant"
    )