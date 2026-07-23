from datetime import datetime, UTC


class AuditEngine:

    def create_log(
        self,
        action: str,
        module: str,
        user: str,
        record_id: int,
        old_data=None,
        new_data=None,
    ):
        """
        Create audit log entry.
        """

        return {
            "timestamp": datetime.now(UTC),
            "module": module,
            "action": action,
            "user": user,
            "record_id": record_id,
            "old_data": old_data,
            "new_data": new_data,
        }