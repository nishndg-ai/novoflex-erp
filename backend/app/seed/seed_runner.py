from app.database.database import SessionLocal

from app.seed.company_seed import seed_company_module
from app.seed.field_company_seed import seed_company_fields


def run():

    db = SessionLocal()

    try:

        seed_company_module(db)
        seed_company_fields(db)

        print("✅ Company metadata seeded successfully.")

    finally:
        db.close()


if __name__ == "__main__":
    run()