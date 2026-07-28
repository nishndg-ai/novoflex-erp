from sqlalchemy.orm import Session

from app.platform.master_engine.import_log import ImportLog



class ImportLogService:


    def create(
        self,
        db: Session,
        module: str,
        file_name: str,
        total_rows: int,
        user: str = "admin",
    ):

        log = ImportLog(
            module=module,
            file_name=file_name,
            total_rows=total_rows,
            status="STARTED",
            user=user,
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
    ):

        log.success_rows = success_rows

        log.failed_rows = failed_rows

        log.status = "COMPLETED"


        db.commit()

        db.refresh(log)

        return log