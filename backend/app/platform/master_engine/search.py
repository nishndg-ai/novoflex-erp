from sqlalchemy import or_


class SearchEngine:

    def search(
        self,
        query,
        model,
        keyword: str,
        fields: list[str],
    ):
        """
        Generic keyword search
        """

        if not keyword:
            return query

        conditions = []

        for field in fields:
            conditions.append(
                getattr(model, field).ilike(f"%{keyword}%")
            )

        return query.filter(
            or_(*conditions)
        )

    def sort(
        self,
        query,
        model,
        field: str = "id",
        direction: str = "asc",
    ):

        column = getattr(model, field)

        if direction.lower() == "desc":
            return query.order_by(column.desc())

        return query.order_by(column.asc())