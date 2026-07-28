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

from app.platform.master_engine.import_error_service import (
    ImportErrorService,
)



class ImportService:
    """
    Runtime based Master Import Service
    """



    def __init__(
        self,
        db: Session,
    ):

        self.db = db

        self.importer = ImportEngine()

        self.import_validator = ImportValidator()

        self.import_log_service = ImportLogService()

        self.import_error_service = ImportErrorService()


        self.runtime_engine = RuntimeEngine(
            db
        )

        self.data_engine = RuntimeDataEngine(
            db
        )

        self.crud = CrudService(
            self.data_engine
        )



    # -----------------------------------------------------
    # Preview
    # -----------------------------------------------------

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



    # -----------------------------------------------------
    # Mapping
    # -----------------------------------------------------

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

            field = field_map.get(
                key.upper()
            )


            if field:

                mapped[field] = value


        return mapped



    # -----------------------------------------------------
    # Clean
    # -----------------------------------------------------

    def clean_values(
        self,
        values,
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



    # -----------------------------------------------------
    # Defaults
    # -----------------------------------------------------

    def apply_defaults(
        self,
        runtime,
        values,
    ):

        for field in runtime.fields:


            current = values.get(
                field.field_name
            )


            if current in (
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



    # -----------------------------------------------------
    # Prepare Rows
    # -----------------------------------------------------

    def prepare_rows(
        self,
        runtime,
        rows,
    ):

        result = []


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
                mapped
            )


            result.append(
                mapped
            )


        return result



    # -----------------------------------------------------
    # Column Validation
    # -----------------------------------------------------

    def validate_columns(
        self,
        runtime,
        columns,
    ):

        required = {

            field.field_name.upper()

            for field in runtime.fields

            if field.is_required

        }


        received = {

            c.upper()

            for c in columns

        }


        missing = list(
            required - received
        )


        if missing:

            raise ValueError(
                {
                    "missing": missing
                }
            )



    # -----------------------------------------------------
    # Execute Import
    # -----------------------------------------------------

    def import_records(
        self,
        module_code,
        file_path,
        user="admin",
    ):


        runtime = self.runtime_engine.build_runtime(
            module_code
        )


        if runtime is None:

            raise ValueError(
                "Module not found"
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



            # ---------------------------------------------
            # Save detailed validation errors
            # ---------------------------------------------

            for error in errors:


                row_number = error.get(
                    "row",
                    0
                )


                error_list = error.get(
                    "errors",
                    []
                )


                for item in error_list:


                    self.import_error_service.create(

                        self.db,

                        batch_no=import_log.batch_no,

                        row_number=row_number,

                        column_name=item.get(
                            "column"
                        ),

                        invalid_value=str(
                            item.get(
                                "value"
                            )
                        ),

                        error_message=item.get(
                            "message"
                        ),

                    )



            # ---------------------------------------------
            # Insert valid records
            # ---------------------------------------------

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


                    self.import_error_service.create(

                        self.db,

                        batch_no=import_log.batch_no,

                        row_number=0,

                        error_message=str(e),

                    )



            self.import_log_service.complete(

                self.db,

                import_log,

                success_rows=inserted,

                failed_rows=failed,

            )



            return {

                "module": module_code,

                "inserted": inserted,

                "failed": failed,

                "errors": errors,

            }



        except Exception as e:


            self.import_log_service.fail(

                self.db,

                import_log,

                str(e),

            )


            raise