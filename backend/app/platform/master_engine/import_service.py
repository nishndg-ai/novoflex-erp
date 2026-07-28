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

from app.platform.master_engine.import_validator import (
    ImportValidator,
)

from app.platform.master_engine.import_log_service import (
    ImportLogService,
)



class ImportService:
    """
    Runtime based Master Data Import Service.

    Flow:

    Excel
      ↓
    Import Engine
      ↓
    Import Log
      ↓
    Column Mapping
      ↓
    Default Values
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

        self.import_validator = ImportValidator()

        self.import_log_service = ImportLogService()


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
    # Apply Defaults
    # ---------------------------------------------------------

    def apply_defaults(
        self,
        runtime,
        values: dict[str, Any],
    ):

        for field in runtime.fields:

            value = values.get(
                field.field_name
            )


            if value in (
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
    # Prepare Rows
    # ---------------------------------------------------------

    def prepare_rows(
        self,
        runtime,
        rows,
    ):

        prepared = []


        for row in rows:

            mapped = self.map_columns(
                runtime,
                row,
            )


            mapped = self.clean_values(
                mapped
            )


            mapped = self.apply_defaults(
                runtime,
                mapped,
            )


            prepared.append(
                mapped
            )


        return prepared



    # ---------------------------------------------------------
    # Validate Import
    # ---------------------------------------------------------

    def validate_import(
        self,
        module_code: str,
        file_path: str,
    ):


        runtime = self.runtime_engine.build_runtime(
            module_code
        )


        rows = self.importer.import_data(
            file_path
        )


        self.validate_columns(
            runtime,
            list(rows[0].keys()),
        )


        prepared_rows = self.prepare_rows(
            runtime,
            rows,
        )


        return self.import_validator.validate(
            runtime,
            prepared_rows,
        )



    # ---------------------------------------------------------
    # Execute Import
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


        import_log = self.import_log_service.create(
            self.db,
            module=module_code,
            file_name=file_path,
            total_rows=len(rows),
            user=user,
        )



        try:

            self.validate_columns(
                runtime,
                list(rows[0].keys()),
            )


            prepared_rows = self.prepare_rows(
                runtime,
                rows,
            )


            validation = self.import_validator.validate(
                runtime,
                prepared_rows,
            )


            inserted = 0

            failed = validation["failed_rows"]

            errors = validation["errors"]



            for row in validation["valid_data"]:

                try:

                    self.crud.create(
                        runtime,
                        row,
                        user=user,
                    )


                    inserted += 1


                except Exception as e:

                    failed += 1


                    errors.append(
                        {
                            "error": str(e),
                            "data": row,
                        }
                    )



            self.import_log_service.complete(
                self.db,
                import_log,
                success_rows=inserted,
                failed_rows=failed,
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


        except Exception:


            import_log.status = "FAILED"

            self.db.commit()


            raise