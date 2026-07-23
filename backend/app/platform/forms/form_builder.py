from app.platform.runtime.runtime_engine import RuntimeEngine


class FormBuilder:

    def __init__(self, runtime: RuntimeEngine):
        self.runtime = runtime

    def build(self, module_code: str):

        runtime = self.runtime.build_runtime(module_code)

        if runtime is None:
            return None

        return {
            "module": runtime["module"],
            "layout": runtime["layout"],
            "fields": runtime["fields"],
        }