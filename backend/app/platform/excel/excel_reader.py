from pathlib import Path

import pandas as pd



class ExcelReader:
    """
    BLUISH Common Excel Reader

    Shared by:

    - Master Import Engine
    - Object Analyzer
    - Future:
        - PDF converter
        - OCR importer
        - AI extraction layer

    Supported:
        .xlsx
        .xls
        .csv
    """



    def read(
        self,
        file_path: str,
    ) -> pd.DataFrame:


        file = Path(file_path)


        if not file.exists():

            raise FileNotFoundError(
                f"File not found: {file_path}"
            )


        extension = (
            file.suffix
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



    def get_columns(
        self,
        file_path: str,
    ) -> list[str]:


        df = self.read(
            file_path
        )


        return (
            df.columns
            .tolist()
        )



    def get_preview(
        self,
        file_path: str,
        rows: int = 10,
    ) -> dict:


        df = self.read(
            file_path
        )


        return {

            "columns":
                df.columns.tolist(),

            "rows":
                df.head(rows)
                .fillna("")
                .to_dict(
                    orient="records"
                ),

            "total_rows":
                len(df),

        }



excel_reader = ExcelReader()