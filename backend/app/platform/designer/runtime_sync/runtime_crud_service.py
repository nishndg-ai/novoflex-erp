from __future__ import annotations

from sqlalchemy.orm import Session
from sqlalchemy import text


from app.platform.metadata.models.metadata_module import (
    MetadataModule,
)


from app.platform.metadata.models.metadata_field import (
    MetadataField,
)



class RuntimeCrudService:
    """
    BLUISH Dynamic Runtime CRUD Engine

    Metadata driven database operations.

    Supported:

        CREATE
        READ LIST
        READ SINGLE
        UPDATE
        SOFT DELETE

    """



    # =====================================================
    # CREATE RECORD
    # =====================================================

    def create(

        self,

        db: Session,

        module_id: int,

        data: dict,

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

                "id":

                    record_id

            },

        )


        row = result.fetchone()



        if not row:

            return None



        return dict(

            row._mapping

        )





    # =====================================================
    # UPDATE RECORD
    # =====================================================

    def update(

        self,

        db: Session,

        module_id: int,

        record_id: int,

        data: dict,

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



        update_data = {

            key: value

            for key, value in data.items()

            if key in allowed_fields

        }



        if not update_data:

            raise Exception(

                "No valid fields provided."

            )



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



        return {

            "id":

                record_id,

            "status":

                "UPDATED",

        }





    # =====================================================
    # SOFT DELETE RECORD
    # =====================================================

    def soft_delete(

        self,

        db: Session,

        module_id: int,

        record_id: int,

    ):


        module = self.get_module(

            db,

            module_id,

        )


        fields = self.get_fields(

            db,

            module_id,

        )


        field_names = [

            field.field_name

            for field in fields

        ]



        if "is_active" not in field_names:


            raise Exception(

                "Soft delete requires is_active field."

            )



        sql = f"""

        UPDATE {module.table_name}

        SET is_active = false

        WHERE id=:id

        """



        result = db.execute(

            text(sql),

            {

                "id":

                    record_id

            },

        )


        db.commit()



        if result.rowcount == 0:

            return {

                "status":

                    "NOT_FOUND"

            }



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