from datetime import datetime

from sqlalchemy.orm import Session

from app.platform.master_engine.import_log import ImportLog



class ImportLogService:


    def generate_batch_no(
        self,
        db: Session,
    ):

        today = datetime.utcnow().strftime(
            "%Y%m%d"
        )


        count = (
            db.query(ImportLog)
            .count()
        )


        sequence = str(
            count + 1
        ).zfill(6)


        return (
            f"IMP-{today}-{sequence}"
        )



    def create(
        self,
        db: Session,
        module: str,
        file_name: str,
        total_rows: int,
        user: str = "admin",
    ):


        log = ImportLog(

            batch_no=self.generate_batch_no(
                db
            ),

            module=module,

            file_name=file_name,

            total_rows=total_rows,

            status="STARTED",

            user=user,

            started_at=datetime.utcnow(),

        )


        db.add(log)

        db.commit()

        db.refresh(log)


        return log



    def complete(
        self,
        db: Session,
        log: ImportLog,
        success_rows: int,
        failed_rows: int,
        error_summary: str | None = None,
    ):


        log.success_rows = success_rows

        log.failed_rows = failed_rows

        log.status = "COMPLETED"

        log.completed_at = datetime.utcnow()


        if error_summary:

            log.error_summary = error_summary



        if log.started_at:

            duration = (
                log.completed_at
                -
                log.started_at
            )


            log.duration_seconds = int(
                duration.total_seconds()
            )



        db.commit()

        db.refresh(log)


        return log



    def fail(
        self,
        db: Session,
        log: ImportLog,
        error: str,
    ):


        log.status = "FAILED"

        log.error_summary = error

        log.completed_at = datetime.utcnow()


        if log.started_at:

            duration = (
                log.completed_at
                -
                log.started_at
            )


            log.duration_seconds = int(
                duration.total_seconds()
            )


        db.commit()

        db.refresh(log)


        return log