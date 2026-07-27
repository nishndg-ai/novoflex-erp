from app.database.database import SessionLocal

from app.platform.master_engine.crud import CrudEngine

from app.models.company import Company



db = SessionLocal()


try:

    crud = CrudEngine()


    company = Company(

        code="TEST-AUDIT-002",

        name="Audit Test Company 002",

        is_active=True

    )


    result = crud.create(

        db=db,

        obj=company,

        module="COMPANY",

        user="admin"

    )


    print(
        "CREATED COMPANY ID:",
        result.id
    )


finally:

    db.close()