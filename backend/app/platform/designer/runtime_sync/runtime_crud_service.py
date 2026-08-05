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

from app.platform.master_engine.history import (
    HistoryEngine,
)



class RuntimeCrudService:


    def __init__(self):

        self.audit = AuditEngine()

        self.history = HistoryEngine()



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



        columns = ", ".join(
            insert_data.keys()
        )


        params = ", ".join(

            [

                f":{key}"

                for key in insert_data.keys()

            ]

        )



        result = db.execute(

            text(

                f"""

                INSERT INTO {module.table_name}

                ({columns})

                VALUES

                ({params})

                RETURNING id

                """

            ),

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



        self.history.add(

            db=db,

            module=module_name,

            record_id=record_id,

            action="CREATE",

            user=user,

            changes={

                "new": insert_data

            },

        )



        return {

            "id": record_id,

            "status": "CREATED",

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


        result = db.execute(

            text(

                f"""

                SELECT *

                FROM {module.table_name}

                ORDER BY id

                """

            )

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


        result = db.execute(

            text(

                f"""

                SELECT *

                FROM {module.table_name}

                WHERE id=:id

                """

            ),

            {

                "id": record_id

            }

        )


        row = result.fetchone()



        if row is None:

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

                "status": "NOT_FOUND"

            }



        # Preserve original database state

        old_data = old_data.copy()



        # Separate update payload

        update_data = data.copy()


        update_data["id"] = record_id



        set_clause = ", ".join(

            [

                f"{key}=:{key}"

                for key in data.keys()

            ]

        )



        db.execute(

            text(

                f"""

                UPDATE {module.table_name}

                SET {set_clause}

                WHERE id=:id

                """

            ),

            update_data,

        )


        db.commit()



        module_name = module.table_name.upper()



        # -----------------------------
        # AUDIT
        # -----------------------------

        self.audit.create_log(

            db=db,

            action="UPDATE",

            module=module_name,

            user=user,

            record_id=record_id,

            old_data=old_data,

            new_data=data,

        )



        # -----------------------------
        # HISTORY
        # -----------------------------

        self.history.add(

            db=db,

            module=module_name,

            record_id=record_id,

            action="UPDATE",

            user=user,

            changes={

                "old": old_data,

                "new": data,

            },

        )



        return {

            "id": record_id,

            "status": "UPDATED",

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

                "status": "NOT_FOUND"

            }



        # Preserve original snapshot

        old_data = old_data.copy()



        db.execute(

            text(

                f"""

                UPDATE {module.table_name}

                SET is_active=false

                WHERE id=:id

                """

            ),

            {

                "id": record_id

            }

        )


        db.commit()



        module_name = module.table_name.upper()



        # -----------------------------
        # AUDIT
        # -----------------------------

        self.audit.create_log(

            db=db,

            action="DELETE",

            module=module_name,

            user=user,

            record_id=record_id,

            old_data=old_data,

            new_data={

                "is_active": False

            },

        )



        # -----------------------------
        # HISTORY
        # -----------------------------

        self.history.add(

            db=db,

            module=module_name,

            record_id=record_id,

            action="DELETE",

            user=user,

            changes={

                "old": old_data,

                "new": {

                    "is_active": False

                },

            },

        )



        return {

            "id": record_id,

            "status": "DEACTIVATED"

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

                "Module not found"

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