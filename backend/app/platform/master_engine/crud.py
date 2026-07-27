from datetime import datetime

from sqlalchemy.orm import Session

from app.platform.master_engine.history import (
    HistoryEngine,
)

from app.platform.master_engine.audit import (
    AuditEngine,
)



class CrudEngine:


    def __init__(self):

        self.history = HistoryEngine()

        self.audit = AuditEngine()



    def create(

        self,

        db: Session,

        obj,

        module: str | None = None,

        user: str = "system",

    ):

        db.add(obj)

        db.commit()

        db.refresh(obj)


        if module:

            record_id = getattr(
                obj,
                "id",
                None
            )


            data = self._object_to_dict(
                obj
            )


            self.history.add(

                db=db,

                module=module,

                record_id=record_id,

                action="CREATE",

                user=user,

                changes={

                    "new": data

                }

            )


            self.audit.create_log(

                db=db,

                action="CREATE",

                module=module,

                user=user,

                record_id=record_id,

                new_data=data

            )


        return obj





    def update(

        self,

        db: Session,

        obj,

        module: str | None = None,

        user: str = "system",

        old_data: dict | None = None,

    ):


        db.commit()

        db.refresh(obj)



        if module:


            record_id = getattr(

                obj,

                "id",

                None

            )


            new_data = self._object_to_dict(

                obj

            )


            self.history.add(

                db=db,

                module=module,

                record_id=record_id,

                action="UPDATE",

                user=user,

                changes={

                    "old": old_data,

                    "new": new_data,

                }

            )


            self.audit.create_log(

                db=db,

                action="UPDATE",

                module=module,

                user=user,

                record_id=record_id,

                old_data=old_data,

                new_data=new_data,

            )


        return obj





    def delete(

        self,

        db: Session,

        obj,

        module: str | None = None,

        user: str = "system",

    ):


        old_data = self._object_to_dict(

            obj

        )


        obj.is_active = False


        db.commit()

        db.refresh(obj)



        if module:


            record_id = getattr(

                obj,

                "id",

                None

            )


            new_data = self._object_to_dict(

                obj

            )


            self.history.add(

                db=db,

                module=module,

                record_id=record_id,

                action="DELETE",

                user=user,

                changes={

                    "old": old_data,

                    "new": new_data,

                }

            )


            self.audit.create_log(

                db=db,

                action="DELETE",

                module=module,

                user=user,

                record_id=record_id,

                old_data=old_data,

                new_data=new_data,

            )


        return obj





    def restore(

        self,

        db: Session,

        obj,

        module: str | None = None,

        user: str = "system",

    ):


        obj.is_active = True


        db.commit()

        db.refresh(obj)



        if module:


            record_id = getattr(

                obj,

                "id",

                None

            )


            new_data = self._object_to_dict(

                obj

            )


            self.history.add(

                db=db,

                module=module,

                record_id=record_id,

                action="RESTORE",

                user=user,

                changes={

                    "new": new_data

                }

            )


            self.audit.create_log(

                db=db,

                action="RESTORE",

                module=module,

                user=user,

                record_id=record_id,

                new_data=new_data,

            )


        return obj





    def _object_to_dict(

        self,

        obj

    ):

        data = {}


        for column in obj.__table__.columns:


            value = getattr(

                obj,

                column.name

            )


            if isinstance(

                value,

                datetime

            ):

                value = value.isoformat()


            data[column.name] = value


        return data