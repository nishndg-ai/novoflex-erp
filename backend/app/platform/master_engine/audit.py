from datetime import datetime, UTC

from sqlalchemy.orm import Session

from app.platform.master_engine.models.audit_log import (
    AuditLog,
)



class AuditEngine:


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

            old_data=old_data,

            new_data=new_data,

            created_at=datetime.now(UTC),

        )


        db.add(audit)

        db.commit()

        db.refresh(audit)


        return audit