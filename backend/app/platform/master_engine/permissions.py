class PermissionEngine:

    def can_view(
        self,
        user_permissions: list[str],
    ):
        return "VIEW" in user_permissions

    def can_create(
        self,
        user_permissions: list[str],
    ):
        return "CREATE" in user_permissions

    def can_edit(
        self,
        user_permissions: list[str],
    ):
        return "EDIT" in user_permissions

    def can_delete(
        self,
        user_permissions: list[str],
    ):
        return "DELETE" in user_permissions

    def can_import(
        self,
        user_permissions: list[str],
    ):
        return "IMPORT" in user_permissions

    def can_export(
        self,
        user_permissions: list[str],
    ):
        return "EXPORT" in user_permissions