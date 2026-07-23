import pandas as pd


def read_excel(filepath: str):

    excel = pd.ExcelFile(filepath)

    result = {
        "sheets": []
    }

    for sheet in excel.sheet_names:

        df = pd.read_excel(
            filepath,
            sheet_name=sheet,
        )

        columns = []

        for col in df.columns:

            columns.append({
                "column": str(col),
                "datatype": str(df[col].dtype),
                "blank": bool(df[col].isnull().all()),
            })

        result["sheets"].append({
            "sheet": sheet,
            "rows": len(df),
            "columns": columns,
        })

    return result