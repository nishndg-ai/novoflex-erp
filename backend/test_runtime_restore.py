from app.database.session import SessionLocal

from app.platform.designer.runtime_sync.runtime_crud_service import (
    runtime_crud_service,
)



db = SessionLocal()


try:


    result = runtime_crud_service.restore(

        db=db,

        module_id=12,

        record_id=4,

        user="nishant",

    )


    print()

    print("RESTORE RESULT")

    print("----------------")

    print(result)



    print()

    print("AFTER RESTORE")

    print("----------------")


    record = runtime_crud_service.get(

        db=db,

        module_id=12,

        record_id=4,

    )


    print(record)



finally:

    db.close()