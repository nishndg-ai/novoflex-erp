from __future__ import annotations

from datetime import datetime, date
from decimal import Decimal
from typing import Any

from sqlalchemy.orm import Session

from app.platform.master_engine.models.master_history import (
    MasterHistory,
)



class HistoryEngine:
    """
    BLUISH History Engine

    Stores record change history.

    Converts non JSON serializable
    Python objects into safe values.
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

                key: self.serialize(item)

                for key, item in value.items()

            }



        if isinstance(

            value,

            list,

        ):

            return [

                self.serialize(item)

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





    def add(

        self,

        db: Session,

        module: str,

        record_id: int,

        action: str,

        user: str,

        changes: dict,

    ):



        serialized_changes = self.serialize(

            changes

        )



        old_data = serialized_changes.get(

            "old"

        )


        new_data = serialized_changes.get(

            "new"

        )



        history = MasterHistory(

            module=module,

            record_id=record_id,

            action=action,

            old_data=old_data,

            new_data=new_data,

            changed_by=user,

            changed_at=datetime.now(),

        )



        db.add(history)

        db.commit()

        db.refresh(history)



        return history