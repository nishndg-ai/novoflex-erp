from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.platform.master_engine.import_error import (
    ImportErrorDetail,
)



router = APIRouter(
    prefix="/import",
    tags=["Import Errors"],
)



@router.get(
    "/{batch_no}/errors"
)
def get_import_errors(
    batch_no: str,
    db: Session = Depends(get_db),
):


    errors = (
        db.query(ImportErrorDetail)
        .filter(
            ImportErrorDetail.batch_no == batch_no
        )
        .order_by(
            ImportErrorDetail.id.asc()
        )
        .all()
    )


    if not errors:

        raise HTTPException(
            status_code=404,
            detail="No errors found for this batch"
        )



    return {

        "batch_no":
            batch_no,


        "total_errors":
            len(errors),


        "errors":
            [

                {

                    "row":
                        error.row_number,


                    "column":
                        error.column_name,


                    "value":
                        error.invalid_value,


                    "message":
                        error.error_message,

                }

                for error in errors

            ]

    }