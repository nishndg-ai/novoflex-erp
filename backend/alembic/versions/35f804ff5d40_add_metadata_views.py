"""add metadata views

Revision ID: 35f804ff5d40
Revises: b4eca62c3bbc
Create Date: 2026-07-25 11:53:13.609937

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "35f804ff5d40"
down_revision: Union[str, Sequence[str], None] = "b4eca62c3bbc"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    op.create_table(
        "metadata_views",
        sa.Column("module_id", sa.Integer(), nullable=False),
        sa.Column("view_code", sa.String(length=100), nullable=False),
        sa.Column("display_name", sa.String(length=200), nullable=False),
        sa.Column("description", sa.String(length=500), nullable=True),
        sa.Column(
            "view_type",
            sa.Enum(
                "FORM",
                "GRID",
                "DETAIL",
                "DASHBOARD",
                "REPORT",
                "KANBAN",
                "CALENDAR",
                "GANTT",
                "TREE",
                "TIMELINE",
                "CARD",
                "PIVOT",
                "CHART",
                "MOBILE",
                name="viewtype",
            ),
            nullable=False,
        ),
        sa.Column("page_size", sa.Integer(), nullable=False),
        sa.Column("default_sort_field", sa.String(length=100), nullable=True),
        sa.Column("default_sort_order", sa.String(length=4), nullable=True),
        sa.Column("is_default", sa.Boolean(), nullable=False),
        sa.Column("allow_search", sa.Boolean(), nullable=False),
        sa.Column("allow_filter", sa.Boolean(), nullable=False),
        sa.Column("allow_sort", sa.Boolean(), nullable=False),
        sa.Column("allow_export", sa.Boolean(), nullable=False),
        sa.Column("allow_grouping", sa.Boolean(), nullable=False),
        sa.Column("allow_column_resize", sa.Boolean(), nullable=False),
        sa.Column("allow_column_reorder", sa.Boolean(), nullable=False),
        sa.Column("allow_pivot", sa.Boolean(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column("created_by", sa.String(length=100), nullable=True),
        sa.Column("updated_by", sa.String(length=100), nullable=True),
        sa.Column("version", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["module_id"],
            ["metadata_modules.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint(
            "module_id",
            "view_code",
            name="uq_metadata_view_module_code",
        ),
    )

    op.create_index(
        op.f("ix_metadata_views_created_at"),
        "metadata_views",
        ["created_at"],
        unique=False,
    )
    op.create_index(
        op.f("ix_metadata_views_id"),
        "metadata_views",
        ["id"],
        unique=False,
    )
    op.create_index(
        op.f("ix_metadata_views_is_active"),
        "metadata_views",
        ["is_active"],
        unique=False,
    )
    op.create_index(
        op.f("ix_metadata_views_module_id"),
        "metadata_views",
        ["module_id"],
        unique=False,
    )
    op.create_index(
        op.f("ix_metadata_views_view_code"),
        "metadata_views",
        ["view_code"],
        unique=False,
    )
    op.create_index(
        op.f("ix_metadata_views_view_type"),
        "metadata_views",
        ["view_type"],
        unique=False,
    )

    op.create_table(
        "metadata_view_components",
        sa.Column("view_id", sa.Integer(), nullable=False),
        sa.Column("field_id", sa.Integer(), nullable=True),
        sa.Column(
            "component_type",
            sa.Enum(
                "FIELD",
                "LABEL",
                "BUTTON",
                "TAB",
                "GROUP",
                "SECTION",
                "SEPARATOR",
                "SPACER",
                "IMAGE",
                "HTML",
                "CUSTOM",
                name="viewcomponenttype",
            ),
            nullable=False,
        ),
        sa.Column("component_name", sa.String(length=100), nullable=False),
        sa.Column("display_name", sa.String(length=200), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("display_order", sa.Integer(), nullable=False),
        sa.Column("row_no", sa.Integer(), nullable=False),
        sa.Column("column_no", sa.Integer(), nullable=False),
        sa.Column("column_span", sa.Integer(), nullable=False),
        sa.Column("is_visible", sa.Boolean(), nullable=False),
        sa.Column("is_readonly", sa.Boolean(), nullable=False),
        sa.Column("css_class", sa.String(length=200), nullable=True),
        sa.Column("style", sa.Text(), nullable=True),
        sa.Column("properties", sa.JSON(), nullable=True),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column("created_by", sa.String(length=100), nullable=True),
        sa.Column("updated_by", sa.String(length=100), nullable=True),
        sa.Column("version", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["field_id"],
            ["metadata_fields.id"],
        ),
        sa.ForeignKeyConstraint(
            ["view_id"],
            ["metadata_views.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint(
            "view_id",
            "component_name",
            name="uq_metadata_view_component_name",
        ),
    )

    op.create_index(
        op.f("ix_metadata_view_components_component_type"),
        "metadata_view_components",
        ["component_type"],
        unique=False,
    )
    op.create_index(
        op.f("ix_metadata_view_components_created_at"),
        "metadata_view_components",
        ["created_at"],
        unique=False,
    )
    op.create_index(
        op.f("ix_metadata_view_components_field_id"),
        "metadata_view_components",
        ["field_id"],
        unique=False,
    )
    op.create_index(
        op.f("ix_metadata_view_components_id"),
        "metadata_view_components",
        ["id"],
        unique=False,
    )
    op.create_index(
        op.f("ix_metadata_view_components_is_active"),
        "metadata_view_components",
        ["is_active"],
        unique=False,
    )
    op.create_index(
        op.f("ix_metadata_view_components_view_id"),
        "metadata_view_components",
        ["view_id"],
        unique=False,
    )


def downgrade() -> None:
    """Downgrade schema."""

    op.drop_index(
        op.f("ix_metadata_view_components_view_id"),
        table_name="metadata_view_components",
    )
    op.drop_index(
        op.f("ix_metadata_view_components_is_active"),
        table_name="metadata_view_components",
    )
    op.drop_index(
        op.f("ix_metadata_view_components_id"),
        table_name="metadata_view_components",
    )
    op.drop_index(
        op.f("ix_metadata_view_components_field_id"),
        table_name="metadata_view_components",
    )
    op.drop_index(
        op.f("ix_metadata_view_components_created_at"),
        table_name="metadata_view_components",
    )
    op.drop_index(
        op.f("ix_metadata_view_components_component_type"),
        table_name="metadata_view_components",
    )
    op.drop_table("metadata_view_components")

    op.drop_index(
        op.f("ix_metadata_views_view_type"),
        table_name="metadata_views",
    )
    op.drop_index(
        op.f("ix_metadata_views_view_code"),
        table_name="metadata_views",
    )
    op.drop_index(
        op.f("ix_metadata_views_module_id"),
        table_name="metadata_views",
    )
    op.drop_index(
        op.f("ix_metadata_views_is_active"),
        table_name="metadata_views",
    )
    op.drop_index(
        op.f("ix_metadata_views_id"),
        table_name="metadata_views",
    )
    op.drop_index(
        op.f("ix_metadata_views_created_at"),
        table_name="metadata_views",
    )
    op.drop_table("metadata_views")