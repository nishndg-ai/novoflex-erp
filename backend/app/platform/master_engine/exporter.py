import pandas as pd


class ExportEngine:

    def export_excel(
        self,
        data: list[dict],
        file_path: str,
    ):
        """
        Export data to Excel.
        """

        df = pd.DataFrame(data)

        df.to_excel(
            file_path,
            index=False,
        )

        return file_path

    def export_csv(
        self,
        data: list[dict],
        file_path: str,
    ):
        """
        Export data to CSV.
        """

        df = pd.DataFrame(data)

        df.to_csv(
            file_path,
            index=False,
        )

        return file_path