from pathlib import Path
from typing import Any

import pandas as pd

from app.platform.excel.excel_reader import (
    excel_reader,
)



class ObjectAnalyzerService:
    """
    BLUISH Object Analyzer

    Converts uploaded Excel structure
    into Business Object Designer definition.

    Version:
        v0.2 ERP Rule Based

    Future:
        - AI suggestions
        - PDF extraction
        - OCR image extraction
    """



    # =====================================================
    # PUBLIC METHOD
    # =====================================================

    def analyze_excel(
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


        fields = []


        for column in df.columns:

            fields.append(

                self.analyze_column(
                    df,
                    column,
                )

            )



        object_name = self.detect_object_name(
            file.stem,
            df.columns.tolist(),
        )



        return {

            "object_name":
                object_name,

            "description":
                f"Created from {file.name}",

            "application":
                "MASTER",

            "category":
                "MASTER",

            "features":
            {
                "excel_import": True,

                "workflow": False,

                "dashboard": False,

                "ai": False,
            },

            "fields":
                fields,

        }



    # =====================================================
    # COLUMN ANALYSIS
    # =====================================================

    def analyze_column(
        self,
        df,
        column_name: str,
    ) -> dict[str, Any]:


        values = (
            df[column_name]
            .dropna()
        )


        data_type = self.detect_data_type(
            values
        )


        normalized_name = (

            column_name
            .strip()
            .lower()
            .replace(
                " ",
                "_",
            )

        )


        required = (

            len(values)
            ==
            len(df)

        )


        unique = self.detect_unique(
            normalized_name,
            values,
        )



        return {

            "name":
                normalized_name,

            "label":
                column_name,

            "data_type":
                data_type,

            "control_type":
                self.detect_control_type(
                    data_type
                ),

            "length":
                self.detect_length(
                    values
                ),

            "required":
                required,

            "unique":
                unique,

            "show_in_grid":
                True,

            "searchable":
                True,

            "filterable":
                True,

        }



    # =====================================================
    # ERP UNIQUE DETECTION
    # =====================================================

    def detect_unique(
        self,
        field_name: str,
        values,
    ) -> bool:


        unique_keywords = [

            "code",

            "id",

            "number",

            "no",

            "gst",

            "email",

            "mobile",

            "phone",

            "registration",

        ]



        non_unique_keywords = [

            "name",

            "description",

            "address",

            "city",

            "state",

            "country",

            "type",

            "category",

            "remarks",

        ]



        for keyword in non_unique_keywords:

            if keyword in field_name:

                return False



        for keyword in unique_keywords:

            if keyword in field_name:

                return True



        # fallback statistical check

        return (

            values.nunique()
            ==
            len(values)

        )



    # =====================================================
    # DATA TYPE DETECTION
    # =====================================================

    def detect_data_type(
        self,
        values,
    ) -> str:


        dtype = values.dtype


        if pd.api.types.is_bool_dtype(dtype):

            return "boolean"


        if pd.api.types.is_integer_dtype(dtype):

            return "integer"


        if pd.api.types.is_float_dtype(dtype):

            return "decimal"


        if pd.api.types.is_datetime64_any_dtype(dtype):

            return "date"


        return "string"



    # =====================================================
    # CONTROL DETECTION
    # =====================================================

    def detect_control_type(
        self,
        data_type: str,
    ) -> str:


        mapping = {

            "string":
                "TEXTBOX",

            "integer":
                "NUMBER",

            "decimal":
                "DECIMAL",

            "boolean":
                "CHECKBOX",

            "date":
                "DATE",

        }


        return mapping.get(
            data_type,
            "TEXTBOX",
        )



    # =====================================================
    # FIELD LENGTH
    # =====================================================

    def detect_length(
        self,
        values,
    ) -> int:


        if len(values) == 0:

            return 150


        max_length = max(

            values.astype(str)
            .map(len)

        )


        if max_length <= 50:

            return 50


        if max_length <= 150:

            return 150


        return 500



    # =====================================================
    # OBJECT NAME
    # =====================================================

    def detect_object_name(
        self,
        filename: str,
        columns: list[str],
    ) -> str:


        text = " ".join(
            columns
        ).lower()



        keyword_map = {

            "customer":
                [
                    "customer",
                    "client",
                    "buyer",
                ],

            "supplier":
                [
                    "supplier",
                    "vendor",
                ],

            "employee":
                [
                    "employee",
                    "staff",
                ],

            "item":
                [
                    "item",
                    "product",
                    "material",
                ],

            "machine":
                [
                    "machine",
                    "equipment",
                ],

        }



        for object_name, keywords in keyword_map.items():

            for keyword in keywords:

                if keyword in text:

                    return object_name.title()



        filename_text = (

            filename
            .replace("_", " ")
            .replace("-", " ")
            .lower()

        )



        if not filename_text.startswith(
            "tmp"
        ):

            return filename_text.title()



        return "Business Object"




object_analyzer_service = ObjectAnalyzerService()