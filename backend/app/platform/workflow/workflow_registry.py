from __future__ import annotations

from .workflow_definition import WorkflowDefinition


class WorkflowRegistry:
    """
    Global workflow registry.

    Initially stores workflow definitions in memory.
    Later this will load definitions from metadata/database.
    """

    _definitions: dict[str, WorkflowDefinition] = {}

    @classmethod
    def register(
        cls,
        definition: WorkflowDefinition,
    ) -> None:
        cls._definitions[
            definition.module_code
        ] = definition

    @classmethod
    def get(
        cls,
        module_code: str,
    ) -> WorkflowDefinition | None:
        return cls._definitions.get(module_code)

    @classmethod
    def exists(
        cls,
        module_code: str,
    ) -> bool:
        return module_code in cls._definitions

    @classmethod
    def all(
        cls,
    ) -> list[WorkflowDefinition]:
        return list(
            cls._definitions.values()
        )

    @classmethod
    def clear(
        cls,
    ) -> None:
        cls._definitions.clear()