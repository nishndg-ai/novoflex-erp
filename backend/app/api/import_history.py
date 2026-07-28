from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.platform.master_engine.import_log import ImportLog


router = APIRouter(
    prefix="/import",
    tags=["Import History"],
)


@router.get("/history")
def import_history(
    db: Session = Depends(get_db),
):

    logs = (
        db.query(ImportLog)
        .order_by(
            ImportLog.id.desc()
        )
        .all()
    )


    return [

        {
            "batch_no": log.batch_no,

            "module": log.module,

            "file_name": log.file_name,

            "total_rows": log.total_rows,

            "success_rows": log.success_rows,

            "failed_rows": log.failed_rows,

            "status": log.status,

            "user": log.user,

            "started_at": log.started_at,

            "completed_at": log.completed_at,

            "duration_seconds": log.duration_seconds,

        }

        for log in logs

    ]