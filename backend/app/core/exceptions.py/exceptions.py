from fastapi import HTTPException


class RecordNotFoundException(HTTPException):

    def __init__(self):
        super().__init__(
            status_code=404,
            detail="Record not found",
        )


class DuplicateRecordException(HTTPException):

    def __init__(self):
        super().__init__(
            status_code=400,
            detail="Duplicate record",
        )