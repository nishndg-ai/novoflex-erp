from app.platform.runtime.runtime_engine import RuntimeEngine


class GridBuilder:

    def __init__(self, runtime: RuntimeEngine):
        self.runtime = runtime

    def build(self, module_code: str):

        runtime = self.runtime.build_runtime(module_code)

        if runtime is None:
            return None

        columns = []

        for field in runtime["fields"]:

            if getattr(field, "show_in_grid", False):

                columns.append(
                    {
                        "field": field.field_name,
                        "title": field.display_name,
                        "type": field.data_type,
                    }
                )

        return {
            "module": runtime["module"],
            "columns": columns,
        }