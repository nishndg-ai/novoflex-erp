from sqlalchemy.orm import Session

from app.platform.metadata.models.metadata_field import MetadataField
from app.platform.metadata.models.metadata_module import MetadataModule


def seed_company_fields(db: Session):

    module = (
        db.query(MetadataModule)
        .filter(MetadataModule.module_code == "company")
        .first()
    )

    if module is None:
        print("Company module not found. Seed company module first.")
        return

    fields = [
        {
            "field_name": "code",
            "display_name": "Company Code",
            "data_type": "string",
            "length": 20,
            "control_type": "textbox",
            "is_required": True,
            "is_unique": True,
        },
        {
            "field_name": "name",
            "display_name": "Company Name",
            "data_type": "string",
            "length": 200,
            "control_type": "textbox",
            "is_required": True,
            "is_unique": False,
        },
        {
            "field_name": "is_active",
            "display_name": "Active",
            "data_type": "boolean",
            "length": 0,
            "control_type": "checkbox",
            "is_required": False,
            "is_unique": False,
        },
    ]

    order = 1

    for item in fields:

        existing = (
            db.query(MetadataField)
            .filter(
                MetadataField.module_id == module.id,
                MetadataField.field_name == item["field_name"],
            )
            .first()
        )

        if existing:
            continue

        field = MetadataField(
            module_id=module.id,
            field_name=item["field_name"],
            display_name=item["display_name"],
            data_type=item["data_type"],
            control_type=item["control_type"],
            length=item["length"],
            decimal_places=0,
            default_value=None,
            is_primary=False,
            is_required=item["is_required"],
            is_unique=item["is_unique"],
            is_visible=True,
            is_editable=True,
            display_order=order,
        )

        db.add(field)
        order += 1

    db.commit()

    print("✅ Company fields seeded successfully.")