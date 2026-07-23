from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Integer,
    String,
    event,
    func,
)

from app.database.base import Base


class BaseEntity(Base):
    __abstract__ = True

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    is_active = Column(
        Boolean,
        nullable=False,
        default=True,
        index=True,
    )

    created_at = Column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        index=True,
    )

    updated_at = Column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    )

    created_by = Column(
        String(100),
        nullable=True,
    )

    updated_by = Column(
        String(100),
        nullable=True,
    )

    version = Column(
        Integer,
        nullable=False,
        default=1,
    )

    def to_dict(self):
        return {
            column.name: getattr(self, column.name)
            for column in self.__table__.columns
        }


@event.listens_for(BaseEntity, "before_update", propagate=True)
def increment_version(mapper, connection, target):
    target.version += 1