from typing import Generic, Type, TypeVar

from sqlalchemy.orm import Session

ModelType = TypeVar("ModelType")


class BaseRepository(Generic[ModelType]):
    """
    Generic repository for all ERP modules.

    Supports:
    - Get All
    - Get By ID
    - Create
    - Update
    - Soft Delete
    - Restore
    - Exists
    - Pagination
    """

    def __init__(self, model: Type[ModelType]):
        self.model = model

    def get_all(self, db: Session):
        return (
            db.query(self.model)
            .filter(self.model.is_active.is_(True))
            .order_by(self.model.id)
            .all()
        )

    def get_paginated(
        self,
        db: Session,
        skip: int = 0,
        limit: int = 50,
    ):
        return (
            db.query(self.model)
            .filter(self.model.is_active.is_(True))
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_by_id(
        self,
        db: Session,
        record_id: int,
    ):
        return (
            db.query(self.model)
            .filter(
                self.model.id == record_id,
                self.model.is_active.is_(True),
            )
            .first()
        )

    def exists(
        self,
        db: Session,
        **filters,
    ):
        return (
            db.query(self.model)
            .filter_by(**filters)
            .first()
            is not None
        )

    def create(
        self,
        db: Session,
        obj: ModelType,
    ):
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj

    def update(
        self,
        db: Session,
        db_obj: ModelType,
    ):
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def soft_delete(
        self,
        db: Session,
        record_id: int,
    ):
        obj = self.get_by_id(db, record_id)

        if obj is None:
            return None

        obj.is_active = False

        db.commit()
        db.refresh(obj)

        return obj

    def restore(
        self,
        db: Session,
        record_id: int,
    ):
        obj = (
            db.query(self.model)
            .filter(self.model.id == record_id)
            .first()
        )

        if obj is None:
            return None

        obj.is_active = True

        db.commit()
        db.refresh(obj)

        return obj