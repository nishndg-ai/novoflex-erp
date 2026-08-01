from __future__ import annotations

from app.platform.designer.schemas.designer_schema import (
    BusinessObjectCreateRequest,
    DesignerFeatures,
    DesignerFieldRequest,
)




class ProposalConversionService:
    """
    BLUISH Proposal Conversion Service.

    Converts stored approved proposal JSON
    into BusinessObjectCreateRequest.

    Flow:

        Designer Proposal
              |
              ↓
        JSON Definition
              |
              ↓
        Pydantic Request
              |
              ↓
        Business Object Designer
    """



    def convert(
        self,
        definition: dict,
    ) -> BusinessObjectCreateRequest:



        fields = []



        for field in definition.get(
            "fields",
            [],
        ):


            fields.append(

                DesignerFieldRequest(

                    name=field.get(
                        "name"
                    ),

                    label=field.get(
                        "label"
                    ),

                    data_type=field.get(
                        "data_type",
                        "string",
                    ),

                    control_type=field.get(
                        "control_type",
                        "TEXTBOX",
                    ),

                    length=field.get(
                        "length",
                        150,
                    ),

                    required=field.get(
                        "required",
                        False,
                    ),

                    unique=field.get(
                        "unique",
                        False,
                    ),

                    show_in_grid=field.get(
                        "show_in_grid",
                        True,
                    ),

                    searchable=field.get(
                        "searchable",
                        True,
                    ),

                    filterable=field.get(
                        "filterable",
                        True,
                    ),

                )

            )



        features_data = definition.get(
            "features",
            {},
        )



        features = DesignerFeatures(

            excel_import=features_data.get(
                "excel_import",
                False,
            ),

            workflow=features_data.get(
                "workflow",
                False,
            ),

            dashboard=features_data.get(
                "dashboard",
                False,
            ),

            ai=features_data.get(
                "ai",
                False,
            ),

        )



        return BusinessObjectCreateRequest(

            object_name=definition.get(
                "object_name"
            ),

            description=definition.get(
                "description"
            ),

            application=definition.get(
                "application",
                "MASTER",
            ),

            category=definition.get(
                "category",
                "MASTER",
            ),

            features=features,

            fields=fields,

        )




proposal_conversion_service = ProposalConversionService()