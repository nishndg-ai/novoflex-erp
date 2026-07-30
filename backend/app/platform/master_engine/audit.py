from __future__ import annotations

from datetime import datetime, date
from decimal import Decimal
from typing import Any

from sqlalchemy.orm import Session

from app.platform.master_engine.models.audit_log import (
    AuditLog,
)



class AuditEngine:
    """
    BLUISH Audit Engine

    Stores audit logs.

    Converts non JSON serializable
    values before storing.
    """



    def serialize(
        self,
        value: Any,
    ) -> Any:


        if isinstance(
            value,
            dict,
        ):

            return {

                key: self.serialize(
                    item
                )

                for key, item in value.items()

            }



        if isinstance(
            value,
            list,
        ):

            return [

                self.serialize(
                    item
                )

                for item in value

            ]



        if isinstance(
            value,
            (
                datetime,
                date,
            ),
        ):

            return value.isoformat()



        if isinstance(
            value,
            Decimal,
        ):

            return float(value)



        return value





    def create_log(

        self,

        db: Session,

        action: str,

        module: str,

        user: str,

        record_id: int,

        old_data=None,

        new_data=None,

    ):


        audit = AuditLog(

            module=module,

            action=action,

            user=user,

            record_id=record_id,


            old_data=self.serialize(
                old_data
            ),


            new_data=self.serialize(
                new_data
            ),


            created_at=datetime.now(),

        )


        db.add(audit)

        db.commit()

        db.refresh(audit)


        return audit