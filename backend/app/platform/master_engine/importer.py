from __future__ import annotations

from pathlib import Path
from typing import Any


from app.platform.excel.excel_reader import (
    excel_reader,
)



class ImportEngine:
    """
    Master Data Import Engine.

    Responsibilities:

    - Excel preview
    - Excel import preparation

    Excel reading is handled by:
        ExcelReader

    Future:
    - Mapping
    - Revision import
    - Validation rules
    - AI assisted mapping
    """



    # ---------------------------------------------------------
    # Preview File
    # ---------------------------------------------------------

    def preview(
        self,
        file_path: str,
    ) -> dict[str, Any]:


        file = Path(
            file_path
        )


        if not file.exists():

            raise FileNotFoundError(
                f"File not found: {file_path}"
            )


        df = excel_reader.read(
            file_path
        )


        return {

            "file_name":
                file.name,


            "columns":
                df.columns.tolist(),


            "rows":
                (
                    df.fillna("")
                    .to_dict(
                        orient="records"
                    )
                ),


            "total_rows":
                len(df),

        }



    # ---------------------------------------------------------
    # Import Data
    # ---------------------------------------------------------

    def import_data(
        self,
        file_path: str,
    ) -> list[dict[str, Any]]:


        df = excel_reader.read(
            file_path
        )


        return (

            df.fillna("")
            .to_dict(
                orient="records"
            )

        )