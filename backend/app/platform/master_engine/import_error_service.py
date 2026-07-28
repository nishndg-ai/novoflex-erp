from sqlalchemy.orm import Session

from app.platform.master_engine.import_error import (
    ImportErrorDetail,
)



class ImportErrorService:


    def create(
        self,
        db: Session,
        batch_no: str,
        row_number: int,
        error_message: str,
        column_name: str | None = None,
        invalid_value: str | None = None,
    ):


        error = ImportErrorDetail(

            batch_no=batch_no,

            row_number=row_number,

            column_name=column_name,

            invalid_value=invalid_value,

            error_message=error_message,

        )


        db.add(error)

        db.commit()

        db.refresh(error)


        return error