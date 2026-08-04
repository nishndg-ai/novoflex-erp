from __future__ import annotations

from sqlalchemy.orm import Session
from sqlalchemy import text


from app.platform.metadata.models.metadata_module import (
    MetadataModule,
)

from app.platform.metadata.models.metadata_field import (
    MetadataField,
)

from app.platform.master_engine.audit import (
    AuditEngine,
)



class RuntimeCrudService:
    """
    BLUISH Dynamic Runtime CRUD Engine

    Metadata driven CRUD.

    Supported:

        CREATE
        READ LIST
        READ SINGLE
        UPDATE
        SOFT DELETE

    """



    def __init__(self):

        self.audit = AuditEngine()



    # =====================================================
    # CREATE
    # =====================================================

    def create(

        self,

        db: Session,

        module_id: int,

        data: dict,

        user: str = "system",

    ):


        module = self.get_module(

            db,

            module_id,

        )


        fields = self.get_fields(

            db,

            module_id,

        )


        allowed_fields = [

            field.field_name

            for field in fields

        ]



        insert_data = {

            key: value

            for key, value in data.items()

            if key in allowed_fields

        }



        if not insert_data:

            raise Exception(

                "No valid fields provided."

            )



        columns = ", ".join(

            insert_data.keys()

        )


        params = ", ".join(

            [

                f":{key}"

                for key in insert_data.keys()

            ]

        )



        sql = f"""

        INSERT INTO {module.table_name}

        ({columns})

        VALUES

        ({params})

        RETURNING id

        """



        result = db.execute(

            text(sql),

            insert_data,

        )


        db.commit()



        record_id = result.fetchone()[0]



        module_name = module.table_name.upper()



        self.audit.create_log(

            db=db,

            action="CREATE",

            module=module_name,

            user=user,

            record_id=record_id,

            new_data=insert_data,

        )



        return {

            "id":

                record_id,

            "status":

                "CREATED",

        }





    # =====================================================
    # READ LIST
    # =====================================================

    def list(

        self,

        db: Session,

        module_id: int,

    ):


        module = self.get_module(

            db,

            module_id,

        )


        sql = f"""

        SELECT *

        FROM {module.table_name}

        ORDER BY id

        """



        result = db.execute(

            text(sql)

        )


        return [

            dict(row._mapping)

            for row in result

        ]





    # =====================================================
    # READ SINGLE
    # =====================================================

    def get(

        self,

        db: Session,

        module_id: int,

        record_id: int,

    ):


        module = self.get_module(

            db,

            module_id,

        )


        sql = f"""

        SELECT *

        FROM {module.table_name}

        WHERE id=:id

        """



        result = db.execute(

            text(sql),

            {

                "id": record_id

            },

        )


        row = result.fetchone()



        if not row:

            return None



        return dict(row._mapping)





    # =====================================================
    # UPDATE
    # =====================================================

    def update(

        self,

        db: Session,

        module_id: int,

        record_id: int,

        data: dict,

        user: str = "system",

    ):


        module = self.get_module(

            db,

            module_id,

        )


        old_data = self.get(

            db,

            module_id,

            record_id,

        )


        if old_data is None:

            return {

                "status":

                    "NOT_FOUND"

            }



        fields = self.get_fields(

            db,

            module_id,

        )


        allowed_fields = [

            field.field_name

            for field in fields

        ]



        update_data = {

            key: value

            for key, value in data.items()

            if key in allowed_fields

        }



        set_clause = ", ".join(

            [

                f"{key}=:{key}"

                for key in update_data.keys()

            ]

        )



        update_data["id"] = record_id



        sql = f"""

        UPDATE {module.table_name}

        SET {set_clause}

        WHERE id=:id

        """



        result = db.execute(

            text(sql),

            update_data,

        )


        db.commit()



        if result.rowcount == 0:

            return {

                "status":

                    "NOT_FOUND"

            }



        self.audit.create_log(

            db=db,

            action="UPDATE",

            module=module.table_name.upper(),

            user=user,

            record_id=record_id,

            old_data=old_data,

            new_data=data,

        )



        return {

            "id":

                record_id,

            "status":

                "UPDATED",

        }





    # =====================================================
    # SOFT DELETE
    # =====================================================

    def soft_delete(

        self,

        db: Session,

        module_id: int,

        record_id: int,

        user: str = "system",

    ):


        module = self.get_module(

            db,

            module_id,

        )


        old_data = self.get(

            db,

            module_id,

            record_id,

        )


        if old_data is None:

            return {

                "status":

                    "NOT_FOUND"

            }



        sql = f"""

        UPDATE {module.table_name}

        SET is_active=false

        WHERE id=:id

        """



        result = db.execute(

            text(sql),

            {

                "id": record_id

            },

        )


        db.commit()



        if result.rowcount == 0:

            return {

                "status":

                    "NOT_FOUND"

            }



        self.audit.create_log(

            db=db,

            action="DELETE",

            module=module.table_name.upper(),

            user=user,

            record_id=record_id,

            old_data=old_data,

            new_data={

                "is_active": False

            },

        )



        return {

            "id":

                record_id,

            "status":

                "DEACTIVATED",

        }





    # =====================================================
    # HELPERS
    # =====================================================

    def get_module(

        self,

        db: Session,

        module_id: int,

    ):


        module = (

            db.query(

                MetadataModule

            )

            .filter(

                MetadataModule.id == module_id

            )

            .first()

        )


        if not module:

            raise Exception(

                "Module not found."

            )


        return module





    def get_fields(

        self,

        db: Session,

        module_id: int,

    ):


        return (

            db.query(

                MetadataField

            )

            .filter(

                MetadataField.module_id == module_id

            )

            .order_by(

                MetadataField.display_order

            )

            .all()

        )





runtime_crud_service = RuntimeCrudService()