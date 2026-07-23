from app.platform.master_engine import master_engine


def test_master_engine_creation():
    assert master_engine is not None


def test_validation_engine():

    data = {
        "code": "COMP001",
        "name": "Novoflex"
    }

    rules = {
        "required": [
            "code",
            "name",
        ]
    }

    assert master_engine.validate(
        data,
        rules,
    ) is True


def test_permission_engine():

    permissions = [
        "VIEW",
        "CREATE",
        "EDIT",
        "DELETE",
        "IMPORT",
        "EXPORT",
    ]

    assert master_engine.permissions.can_view(permissions)
    assert master_engine.permissions.can_create(permissions)
    assert master_engine.permissions.can_edit(permissions)
    assert master_engine.permissions.can_delete(permissions)
    assert master_engine.permissions.can_import(permissions)
    assert master_engine.permissions.can_export(permissions)


def test_history_engine():

    master_engine.add_history(
        module="Company",
        record_id=1,
        action="CREATE",
        user="Admin",
    )

    history = master_engine.get_history(
        "Company",
        1,
    )

    assert len(history) == 1


def test_audit_engine():

    log = master_engine.audit_log(
        action="CREATE",
        module="Company",
        user="Admin",
        record_id=1,
    )

    assert log["action"] == "CREATE"
    assert log["module"] == "Company"