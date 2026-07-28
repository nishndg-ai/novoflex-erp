from typing import Any

from pydantic import BaseModel, Field


class ImportPreview(BaseModel):
    """
    Response model for uploaded file preview.
    """

    module_code: str

    file_name: str

    columns: list[str] = Field(
        default_factory=list
    )

    rows: list[dict[str, Any]] = Field(
        default_factory=list
    )

    total_rows: int = 0



class ImportValidationResult(BaseModel):
    """
    Validation result before commit.
    """

    module_code: str

    total_rows: int = 0

    valid_rows: int = 0

    invalid_rows: int = 0

    errors: list[dict[str, Any]] = Field(
        default_factory=list
    )



class ImportRequest(BaseModel):
    """
    Import execution request.
    """

    module_code: str

    mode: str = "ADD"
    """
    Supported modes:

    ADD
    REVISE_DATA
    REVISE_FORMAT
    """

    user: str = "admin"



class ImportResult(BaseModel):
    """
    Final import result.
    """

    module_code: str

    mode: str

    inserted: int = 0

    updated: int = 0

    failed: int = 0

    errors: list[dict[str, Any]] = Field(
        default_factory=list
    )