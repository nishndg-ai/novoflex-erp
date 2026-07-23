from sqlalchemy.orm import Session


class CrudEngine:

    def create(
        self,
        db: Session,
        obj,
    ):
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj

    def update(
        self,
        db: Session,
        obj,
    ):
        db.commit()
        db.refresh(obj)
        return obj

    def delete(
        self,
        db: Session,
        obj,
    ):
        obj.is_active = False

        db.commit()

        return obj

    def restore(
        self,
        db: Session,
        obj,
    ):
        obj.is_active = True

        db.commit()

        return obj