import os
import shutil
from uuid import uuid4

from fastapi import APIRouter, UploadFile, File

from app.utils.excel_parser import read_excel

router = APIRouter(
    prefix="/templates",
    tags=["Template Engine"],
)

UPLOAD_FOLDER = "uploads/templates"

os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True,
)


@router.post("/upload")
async def upload_template(
    file: UploadFile = File(...)
):
    extension = file.filename.split(".")[-1]

    filename = f"{uuid4()}.{extension}"

    filepath = os.path.join(
        UPLOAD_FOLDER,
        filename,
    )

    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(
            file.file,
            buffer,
        )

    excel = read_excel(filepath)

    return {
        "message": "Template uploaded successfully",
        "file_name": filename,
        "original_name": file.filename,
        "structure": excel,
    }