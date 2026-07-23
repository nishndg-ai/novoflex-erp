import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()

engine = create_engine(os.getenv("DATABASE_URL"))

with engine.connect() as conn:

    result = conn.execute(text("""
        SELECT
            column_name,
            data_type
        FROM information_schema.columns
        WHERE table_name = 'metadata_layouts'
        ORDER BY ordinal_position;
    """))

    print("\nmetadata_layouts columns\n")
    print("=" * 60)

    for row in result:
        print(f"{row.column_name:30} {row.data_type}")