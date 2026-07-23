from sqlalchemy.orm import Session

from app.platform.metadata.models.metadata_module import MetadataModule


def seed_company_module(db: Session):

    existing = (
        db.query(MetadataModule)
        .filter(MetadataModule.module_code == "company")
        .first()
    )

    if existing:
        return existing

    module = MetadataModule(
        module_code="company",
        module_name="Company",
        display_name="Company",
        description="Company Master",

        application="ERP",
        category="Masters",

        route="/company",
        icon="building",

        menu_order=1,

        table_name="company",

        api_endpoint="/runtime/company",

        page_size=20,
    )

    db.add(module)
    db.commit()
    db.refresh(module)

    return module