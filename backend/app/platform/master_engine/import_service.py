from __future__ import annotations

import math

from typing import Any

from sqlalchemy.orm import Session

from app.platform.runtime.runtime_engine import RuntimeEngine
from app.platform.runtime.runtime_data_engine import (
    RuntimeDataEngine,
)

from app.platform.crud.service import CrudService

from app.platform.master_engine.importer import (
    ImportEngine,
)



class ImportService:
    """
    Runtime based Master Data Import Service.

    Flow:

    File
      ↓
    ImportEngine
      ↓
    Runtime Metadata
      ↓
    Column Mapping
      ↓
    Data Cleaning
      ↓
    Validation
      ↓
    Runtime CRUD
      ↓
    Audit + History
    """



    def __init__(
        self,
        db: Session,
    ):

        self.db = db

        self.importer = ImportEngine()

        self.runtime_engine = RuntimeEngine(
            db
        )

        self.data_engine = RuntimeDataEngine(
            db
        )

        self.crud = CrudService(
            self.data_engine
        )



    # ---------------------------------------------------------
    # Preview
    # ---------------------------------------------------------

    def preview(
        self,
        module_code: str,
        file_path: str,
    ) -> dict[str, Any]:


        runtime = (
            self.runtime_engine
            .build_runtime(module_code)
        )


        if runtime is None:

            raise ValueError(
                f"Module '{module_code}' not found"
            )


        file_data = self.importer.preview(
            file_path
        )


        return {

            "module":
                runtime.module.module_code,

            "table":
                runtime.module.table_name,

            "fields":
                [
                    field.field_name
                    for field in runtime.fields
                ],

            "file":
                file_data,

        }



    # ---------------------------------------------------------
    # Column Mapping
    # ---------------------------------------------------------

    def map_columns(
        self,
        runtime,
        row: dict[str, Any],
    ):

        """
        Convert Excel headers into
        database field names.
        """


        field_map = {

            field.field_name.upper():
                field.field_name

            for field in runtime.fields

        }


        mapped = {}


        for key, value in row.items():

            db_field = field_map.get(
                key.upper()
            )


            if db_field:

                mapped[db_field] = value


        return mapped



    # ---------------------------------------------------------
    # Clean Imported Values
    # ---------------------------------------------------------

    def clean_values(
        self,
        values: dict[str, Any],
    ):

        """
        Convert Excel empty values.

        NaN  → None
        """

        cleaned = {}


        for key, value in values.items():


            if (
                isinstance(value, float)
                and math.isnan(value)
            ):

                cleaned[key] = None


            else:

                cleaned[key] = value


        return cleaned



    # ---------------------------------------------------------
    # Import Records
    # ---------------------------------------------------------

    def import_records(
        self,
        module_code: str,
        file_path: str,
        user: str = "admin",
    ) -> dict[str, Any]:


        runtime = (
            self.runtime_engine
            .build_runtime(module_code)
        )


        if runtime is None:

            raise ValueError(
                f"Module '{module_code}' not found"
            )


        rows = self.importer.import_data(
            file_path
        )


        inserted = 0

        failed = 0

        errors = []



        for index, row in enumerate(
            rows,
            start=1
        ):


            try:


                mapped_row = self.map_columns(
                    runtime,
                    row,
                )


                mapped_row = self.clean_values(
                    mapped_row
                )


                self.crud.create(
                    runtime,
                    mapped_row,
                    user=user,
                )


                inserted += 1



            except Exception as e:


                failed += 1


                errors.append(
                    {
                        "row": index,
                        "error": str(e),
                    }
                )



        return {

            "module":
                module_code,

            "inserted":
                inserted,

            "failed":
                failed,

            "errors":
                errors,

        }