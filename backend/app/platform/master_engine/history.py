from datetime import datetime, UTC

from sqlalchemy.orm import Session

from app.platform.master_engine.models.master_history import (
    MasterHistory,
)



class HistoryEngine:


    def add(
        self,
        db: Session,
        module: str,
        record_id: int,
        action: str,
        user: str,
        changes=None,
        reason: str | None = None,
    ):


        history = MasterHistory(

            module=module,

            record_id=record_id,

            action=action,

            old_data=(
                changes.get("old")
                if changes
                else None
            ),

            new_data=(
                changes.get("new")
                if changes
                else None
            ),

            reason=reason,

            changed_by=user,

            changed_at=datetime.now(UTC),

        )


        db.add(history)

        db.commit()

        db.refresh(history)


        return history



    def get(

        self,

        db: Session,

        module: str,

        record_id: int,

    ):


        return (

            db.query(MasterHistory)

            .filter(

                MasterHistory.module == module,

                MasterHistory.record_id == record_id,

            )

            .order_by(

                MasterHistory.changed_at.desc()

            )

            .all()

        )