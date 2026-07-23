from enum import Enum


class EventType(str, Enum):
    # CRUD
    BEFORE_CREATE = "before_create"
    AFTER_CREATE = "after_create"

    BEFORE_UPDATE = "before_update"
    AFTER_UPDATE = "after_update"

    BEFORE_DELETE = "before_delete"
    AFTER_DELETE = "after_delete"

    # Validation
    BEFORE_VALIDATE = "before_validate"
    AFTER_VALIDATE = "after_validate"

    # Query
    BEFORE_QUERY = "before_query"
    AFTER_QUERY = "after_query"

    # Lookup
    BEFORE_LOOKUP = "before_lookup"
    AFTER_LOOKUP = "after_lookup"

    # Workflow
    BEFORE_WORKFLOW = "before_workflow"
    AFTER_WORKFLOW = "after_workflow"

    BEFORE_STATE_CHANGE = "before_state_change"
    AFTER_STATE_CHANGE = "after_state_change"