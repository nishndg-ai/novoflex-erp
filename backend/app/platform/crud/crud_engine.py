from __future__ import annotations

from typing import Any

from app.platform.crud.service import CrudService

from app.platform.runtime.runtime_data_engine import (
    RuntimeDataEngine,
)

from app.platform.runtime.runtime_engine import (
    RuntimeEngine,
)



class CrudEngine:
    """
    Generic metadata-driven CRUD engine.

    Carries user security context
    for company / plant level data isolation.
    """



    def __init__(
        self,
        runtime_engine: RuntimeEngine,
        data_engine: RuntimeDataEngine,
        user_context: dict | None = None,
    ):

        self.runtime_engine = runtime_engine

        self.user_context = user_context or {}

        self.service = CrudService(
            data_engine
        )



    # ---------------------------------------------------------
    # LIST
    # ---------------------------------------------------------

    def list(
        self,
        module_code: str,
        *,
        filters: dict[str, Any] | None = None,
        search: str | None = None,
        limit: int = 100,
        offset: int = 0,
        order_by: str | None = None,
        descending: bool = False,
        include_deleted: bool = False,
    ):

        runtime = self.runtime_engine.build_runtime(
            module_code
        )


        return self.service.list(

            runtime,

            filters=filters,

            search=search,

            limit=limit,

            offset=offset,

            order_by=order_by,

            descending=descending,

            include_deleted=include_deleted,

            user_context=self.user_context,

        )



    # ---------------------------------------------------------
    # GET
    # ---------------------------------------------------------

    def get(
        self,
        module_code: str,
        record_id: int,
    ):

        runtime = self.runtime_engine.build_runtime(
            module_code
        )


        return self.service.get(

            runtime,

            record_id,

            user_context=self.user_context,

        )



    # ---------------------------------------------------------
    # CREATE
    # ---------------------------------------------------------

    def create(
        self,
        module_code: str,
        values: dict[str, Any],
    ):

        runtime = self.runtime_engine.build_runtime(
            module_code
        )


        return self.service.create(

            runtime,

            values,

            user_context=self.user_context,

        )



    # ---------------------------------------------------------
    # UPDATE
    # ---------------------------------------------------------

    def update(
        self,
        module_code: str,
        record_id: int,
        values: dict[str, Any],
    ):

        runtime = self.runtime_engine.build_runtime(
            module_code
        )


        self.service.update(

            runtime,

            record_id,

            values,

            user_context=self.user_context,

        )



    # ---------------------------------------------------------
    # DELETE
    # ---------------------------------------------------------

    def delete(
        self,
        module_code: str,
        record_id: int,
    ):

        runtime = self.runtime_engine.build_runtime(
            module_code
        )


        self.service.delete(

            runtime,

            record_id,

            user_context=self.user_context,

        )



    # ---------------------------------------------------------
    # RESTORE
    # ---------------------------------------------------------

    def restore(
        self,
        module_code: str,
        record_id: int,
    ):

        runtime = self.runtime_engine.build_runtime(
            module_code
        )


        self.service.restore(

            runtime,

            record_id,

            user_context=self.user_context,

        )