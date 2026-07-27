from sqlalchemy.orm import Session

from .crud import CrudEngine
from .validator import ValidationEngine
from .search import SearchEngine
from .importer import ImportEngine
from .exporter import ExportEngine
from .audit import AuditEngine
from .history import HistoryEngine
from .permissions import PermissionEngine



class MasterEngine:


    def __init__(self):

        self.crud = CrudEngine()

        self.validator = ValidationEngine()

        self.search = SearchEngine()

        self.importer = ImportEngine()

        self.exporter = ExportEngine()

        self.audit = AuditEngine()

        self.history = HistoryEngine()

        self.permissions = PermissionEngine()



    # ==========================
    # CRUD
    # ==========================


    def create(

        self,

        db: Session,

        obj,

        module: str | None = None,

        user: str = "system",

    ):

        return self.crud.create(

            db=db,

            obj=obj,

            module=module,

            user=user,

        )





    def update(

        self,

        db: Session,

        obj,

        module: str | None = None,

        user: str = "system",

        old_data: dict | None = None,

    ):

        return self.crud.update(

            db=db,

            obj=obj,

            module=module,

            user=user,

            old_data=old_data,

        )





    def delete(

        self,

        db: Session,

        obj,

        module: str | None = None,

        user: str = "system",

    ):

        return self.crud.delete(

            db=db,

            obj=obj,

            module=module,

            user=user,

        )





    def restore(

        self,

        db: Session,

        obj,

        module: str | None = None,

        user: str = "system",

    ):

        return self.crud.restore(

            db=db,

            obj=obj,

            module=module,

            user=user,

        )





    # ==========================
    # VALIDATION
    # ==========================


    def validate(

        self,

        data: dict,

        rules=None,

    ):

        return self.validator.validate(

            data,

            rules

        )





    # ==========================
    # SEARCH
    # ==========================


    def search_records(

        self,

        query,

        model,

        keyword: str,

        fields: list[str],

    ):

        return self.search.search(

            query,

            model,

            keyword,

            fields,

        )





    def sort_records(

        self,

        query,

        model,

        field="id",

        direction="asc",

    ):

        return self.search.sort(

            query,

            model,

            field,

            direction,

        )





    # ==========================
    # IMPORT / EXPORT
    # ==========================


    def preview_import(

        self,

        file_path: str,

    ):

        return self.importer.preview(

            file_path

        )





    def import_data(

        self,

        file_path: str,

    ):

        return self.importer.import_data(

            file_path

        )





    def export_excel(

        self,

        data,

        file_path,

    ):

        return self.exporter.export_excel(

            data,

            file_path,

        )





    def export_csv(

        self,

        data,

        file_path,

    ):

        return self.exporter.export_csv(

            data,

            file_path,

        )





    # ==========================
    # AUDIT / HISTORY
    # ==========================


    def audit_log(

        self,

        **kwargs

    ):

        return self.audit.create_log(

            **kwargs

        )





    def add_history(

        self,

        **kwargs

    ):

        return self.history.add(

            **kwargs

        )





    def get_history(

        self,

        db: Session,

        module,

        record_id,

    ):

        return self.history.get(

            db,

            module,

            record_id,

        )