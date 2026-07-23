from datetime import datetime, UTC


class HistoryEngine:

    def __init__(self):
        self._history = []

    def add(
        self,
        module: str,
        record_id: int,
        action: str,
        user: str,
        changes=None,
    ):
        entry = {
            "timestamp": datetime.now(UTC),
            "module": module,
            "record_id": record_id,
            "action": action,
            "user": user,
            "changes": changes or {},
        }

        self._history.append(entry)

        return entry

    def get(
        self,
        module: str,
        record_id: int,
    ):
        return [
            item
            for item in self._history
            if item["module"] == module
            and item["record_id"] == record_id
        ]