def detect_template(structure):

    result = {
        "type": "UNKNOWN",
        "sheet": None,
        "columns": [],
    }

    if len(structure["sheets"]) == 0:
        return result

    sheet = structure["sheets"][0]

    result["sheet"] = sheet["sheet"]

    columns = []

    for col in sheet["columns"]:
        columns.append(col["column"])

    result["columns"] = columns

    text = " ".join(columns).lower()

    if (
        "code" in text
        and "name" in text
    ):
        result["type"] = "MASTER"

    elif (
        "parameter" in text
        or "characteristic" in text
    ):
        result["type"] = "CHECKSHEET"

    elif (
        "qty" in text
        or "quantity" in text
    ):
        result["type"] = "TRANSACTION"

    return result