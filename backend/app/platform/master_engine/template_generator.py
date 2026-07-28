from __future__ import annotations

from pathlib import Path
from typing import Any

import pandas as pd


class TemplateGenerator:
    """
    Runtime metadata based Excel template generator.
    """

    def generate(
        self,
        runtime,
        file_path: str,
    ) -> str:
        """
        Generate Excel import template
        from runtime fields.
        """

        columns = []

        sample_row = {}

        for field in runtime.fields:

            columns.append(
                field.field_name
            )

            if field.is_required:
                sample_row[field.field_name] = (
                    f"<{field.display_name}>"
                )
            else:
                sample_row[field.field_name] = ""


        df = pd.DataFrame(
            [sample_row],
            columns=columns,
        )


        path = Path(file_path)

        df.to_excel(
            path,
            index=False,
        )


        return str(path)