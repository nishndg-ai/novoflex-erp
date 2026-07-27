from app.database.database import SessionLocal

from app.platform.master_engine.history import HistoryEngine
from app.platform.master_engine.audit import AuditEngine



db = SessionLocal()


try:

    history = HistoryEngine()

    result = history.add(

        db=db,

        module="PRODUCT",

        record_id=1,

        action="CREATE",

        user="admin",

        changes={

            "new": {

                "product_code": "TEST001",

                "product_name": "Test Product"

            }

        },

        reason="Initial creation"

    )


    print(
        "HISTORY CREATED:",
        result.id
    )



    audit = AuditEngine()


    result2 = audit.create_log(

        db=db,

        action="CREATE",

        module="PRODUCT",

        user="admin",

        record_id=1,

        new_data={

            "product_code": "TEST001"

        }

    )


    print(
        "AUDIT CREATED:",
        result2.id
    )


finally:

    db.close()