from __future__ import annotations

from pathlib import Path
from typing import Any

import pandas as pd


class ImportEngine:
    """
    Master Data Import Engine.

    Current support:
    - Excel preview
    - Excel import preparation

    Future:
    - CSV
    - PDF
    - Word
    - OCR
    - Mapping
    - Revision import
    """

    # ---------------------------------------------------------
    # Preview File
    # ---------------------------------------------------------

    def preview(
        self,
        file_path: str,
    ) -> dict[str, Any]:

        file = Path(file_path)

        if not file.exists():
            raise FileNotFoundError(
                f"File not found: {file_path}"
            )

        df = self._read_file(
            file_path
        )

        return {
            "file_name": file.name,

            "columns":
                df.columns.tolist(),

            "rows":
                df.fillna("")
                .to_dict(
                    orient="records"
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

        df = self._read_file(
            file_path
        )

        return (
            df.fillna("")
            .to_dict(
                orient="records"
            )
        )


    # ---------------------------------------------------------
    # File Reader
    # ---------------------------------------------------------

    def _read_file(
        self,
        file_path: str,
    ) -> pd.DataFrame:

        extension = (
            Path(file_path)
            .suffix
            .lower()
        )


        if extension in [
            ".xlsx",
            ".xls",
        ]:

            return pd.read_excel(
                file_path
            )


        if extension == ".csv":

            return pd.read_csv(
                file_path
            )


        raise ValueError(
            f"Unsupported file format: {extension}"
        )