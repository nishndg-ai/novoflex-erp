from sqlalchemy import (
    MetaData,
    Table,
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
    func,
    inspect,
)

from sqlalchemy.orm import Session


from app.platform.metadata.models.metadata_module import (
    MetadataModule,
)

from app.platform.metadata.models.metadata_field import (
    MetadataField,
)



class SchemaGenerator:
    """
    BLUISH Dynamic Schema Generator

    Converts metadata definitions into
    physical database tables.

    Supports:
    - GLOBAL data
    - COMPANY data
    - PLANT data
    """



    def __init__(
        self,
        db: Session,
    ):

        self.db = db

        self.engine = db.get_bind()

        self.metadata = MetaData()



    def generate_table(
        self,
        module_id: int,
    ):

        module = (
            self.db.query(MetadataModule)
            .filter(
                MetadataModule.id == module_id
            )
            .first()
        )


        if module is None:

            raise ValueError(
                "Module not found"
            )



        table_name = module.table_name



        inspector = inspect(
            self.engine
        )


        if inspector.has_table(
            table_name
        ):

            return {

                "message":
                    "Table already exists",

                "table":
                    table_name,

            }





        fields = (

            self.db.query(MetadataField)

            .filter(

                MetadataField.module_id == module_id,

                MetadataField.is_active.is_(True),

            )

            .order_by(

                MetadataField.display_order

            )

            .all()

        )





        columns = []



        # =====================================================
        # PRIMARY KEY
        # =====================================================

        columns.append(

            Column(

                "id",

                Integer,

                primary_key=True,

                autoincrement=True,

            )

        )





        # =====================================================
        # METADATA FIELDS
        # =====================================================

        for field in fields:


            column_type = self.resolve_type(

                field.data_type,

                field.length,

            )



            columns.append(

                Column(

                    field.field_name,

                    column_type,

                    nullable=not field.is_required,

                    unique=field.is_unique,

                )

            )





        # =====================================================
        # DATA SCOPE FIELDS
        # =====================================================

        if module.data_scope == "COMPANY":


            columns.append(

                Column(

                    "company_id",

                    Integer,

                    nullable=True,

                )

            )



        elif module.data_scope == "PLANT":


            columns.append(

                Column(

                    "plant_id",

                    Integer,

                    nullable=True,

                )

            )





        # =====================================================
        # COMMON BLUISH SYSTEM FIELDS
        # =====================================================

        columns.extend(

            [

                Column(

                    "is_active",

                    Boolean,

                    nullable=False,

                    default=True,

                ),


                Column(

                    "created_at",

                    DateTime,

                    server_default=func.now(),

                ),


                Column(

                    "updated_at",

                    DateTime,

                    server_default=func.now(),

                    onupdate=func.now(),

                ),


                Column(

                    "version",

                    Integer,

                    default=1,

                ),

            ]

        )





        table = Table(

            table_name,

            self.metadata,

            *columns,

        )





        self.metadata.create_all(

            self.engine,

            tables=[table],

        )





        return {


            "message":

                "Table created successfully",



            "table":

                table_name,



            "columns":

                [

                    column.name

                    for column in columns

                ],

        }





    def resolve_type(

        self,

        data_type: str,

        length: int | None = None,

    ):



        if data_type.lower() == "string":


            return String(

                length or 255

            )



        if data_type.lower() == "integer":


            return Integer



        if data_type.lower() == "boolean":


            return Boolean



        if data_type.lower() == "datetime":


            return DateTime



        return String(255)





schema_generator = SchemaGenerator