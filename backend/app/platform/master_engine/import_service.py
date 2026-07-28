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
    ):

        runtime = self.runtime_engine.build_runtime(
            module_code
        )

        if runtime is None:
            raise ValueError(
                f"Module '{module_code}' not found"
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
                self.importer.preview(
                    file_path
                ),
        }



    # ---------------------------------------------------------
    # Column Mapping
    # ---------------------------------------------------------

    def map_columns(
        self,
        runtime,
        row: dict[str, Any],
    ):

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
    # Column Validation
    # ---------------------------------------------------------

    def validate_columns(
        self,
        runtime,
        row_columns: list[str],
    ):

        required_columns = {

            field.field_name.upper()

            for field in runtime.fields

            if field.is_required

        }


        received_columns = {

            column.upper()

            for column in row_columns

        }


        missing = list(
            required_columns - received_columns
        )


        extra = list(
            received_columns -
            {
                field.field_name.upper()
                for field in runtime.fields
            }
        )


        if missing or extra:

            raise ValueError(
                {
                    "error": "Invalid columns",
                    "missing": missing,
                    "extra": extra,
                }
            )



    # ---------------------------------------------------------
    # Clean Values
    # ---------------------------------------------------------

    def clean_values(
        self,
        values: dict[str, Any],
    ):

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
    # Apply Runtime Defaults
    # ---------------------------------------------------------

    def apply_defaults(
        self,
        runtime,
        values: dict[str, Any],
    ):

        for field in runtime.fields:

            current_value = values.get(
                field.field_name
            )


            if current_value in (
                None,
                "",
            ):

                if field.default_value not in (
                    None,
                    "",
                ):

                    default = field.default_value


                    if str(default).lower() == "true":
                        default = True

                    elif str(default).lower() == "false":
                        default = False


                    values[field.field_name] = default


        return values



    # ---------------------------------------------------------
    # Import Records
    # ---------------------------------------------------------

    def import_records(
        self,
        module_code: str,
        file_path: str,
        user: str = "admin",
    ):


        runtime = self.runtime_engine.build_runtime(
            module_code
        )


        if runtime is None:
            raise ValueError(
                f"Module '{module_code}' not found"
            )


        rows = self.importer.import_data(
            file_path
        )


        if rows:

            self.validate_columns(
                runtime,
                list(rows[0].keys()),
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


                mapped_row = self.apply_defaults(
                    runtime,
                    mapped_row,
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