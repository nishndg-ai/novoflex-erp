from enum import Enum


class ViewType(str, Enum):
    """
    Supported runtime view types.
    """

    FORM = "FORM"
    GRID = "GRID"
    DETAIL = "DETAIL"

    DASHBOARD = "DASHBOARD"
    REPORT = "REPORT"

    KANBAN = "KANBAN"
    CALENDAR = "CALENDAR"
    GANTT = "GANTT"

    TREE = "TREE"
    TIMELINE = "TIMELINE"
    CARD = "CARD"

    PIVOT = "PIVOT"
    CHART = "CHART"

    MOBILE = "MOBILE"