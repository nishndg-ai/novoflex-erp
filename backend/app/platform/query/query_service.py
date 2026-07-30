from __future__ import annotations

from typing import Any

from sqlalchemy import and_

from sqlalchemy.orm import Session

from .count_builder import CountBuilder
from .query_engine import QueryEngine
from .query_result import QueryResult



class QueryService:
    """
    Generic runtime query service.

    Default behavior:
    - Returns only active records.
    - Hides soft deleted records.

    Deleted records can be included
    using include_deleted=True.
    """



    def __init__(
        self,
        db: Session,
    ):

        self.db = db



    def execute(
        self,
        *,
        table,
        filters: dict[str, Any] | None = None,
        search: str | None = None,
        limit: int = 100,
        offset: int = 0,
        order_by: str | None = None,
        descending: bool = False,
        include_deleted: bool = False,
    ) -> dict[str, Any]:

        runtime_filters = {}

        if filters:
            runtime_filters.update(
                filters
            )


        # -------------------------------------------------
        # BLUISH Soft Delete Filter
        # -------------------------------------------------

        if (
            not include_deleted
            and hasattr(
                table.c,
                "is_active",
            )
        ):

            runtime_filters[
                "is_active"
            ] = True



        stmt = QueryEngine.build_select(

            table,

            filters=runtime_filters,

            search=search,

            limit=limit,

            offset=offset,

            order_by=order_by,

            descending=descending,

        )



        rows = [

            dict(row._mapping)

            for row in self.db.execute(stmt).fetchall()

        ]



        total_stmt = CountBuilder.build(

            table,

            filters=runtime_filters,

            search=search,

        )



        total = self.db.execute(
            total_stmt
        ).scalar_one()



        return QueryResult.build(

            rows=rows,

            total=total,

            limit=limit,

            offset=offset,

        )