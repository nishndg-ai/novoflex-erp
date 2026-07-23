import pandas as pd


class ImportEngine:

    def preview(
        self,
        file_path: str,
    ):
        """
        Preview imported Excel file.
        """

        df = pd.read_excel(file_path)

        return {
            "columns": df.columns.tolist(),
            "rows": df.fillna("").to_dict(
                orient="records"
            ),
            "total_rows": len(df),
        }

    def import_data(
        self,
        file_path: str,
    ):
        """
        Import Excel file.
        """

        df = pd.read_excel(file_path)

        return df.to_dict(
            orient="records"
        )