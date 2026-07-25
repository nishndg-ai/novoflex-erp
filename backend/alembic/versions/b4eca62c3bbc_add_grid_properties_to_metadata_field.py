"""add grid properties to metadata_field

Revision ID: b4eca62c3bbc
Revises: ceabfa5236d7
Create Date: 2026-07-25 11:09:17.604609

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "b4eca62c3bbc"
down_revision: Union[str, Sequence[str], None] = "ceabfa5236d7"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    op.add_column(
        "metadata_fields",
        sa.Column(
            "show_in_grid",
            sa.Boolean(),
            nullable=False,
            server_default=sa.text("false"),
        ),
    )

    op.add_column(
        "metadata_fields",
        sa.Column(
            "grid_order",
            sa.Integer(),
            nullable=False,
            server_default=sa.text("0"),
        ),
    )

    op.add_column(
        "metadata_fields",
        sa.Column(
            "grid_width",
            sa.Integer(),
            nullable=False,
            server_default=sa.text("150"),
        ),
    )

    op.add_column(
        "metadata_fields",
        sa.Column(
            "is_sortable",
            sa.Boolean(),
            nullable=False,
            server_default=sa.text("true"),
        ),
    )

    op.add_column(
        "metadata_fields",
        sa.Column(
            "is_filterable",
            sa.Boolean(),
            nullable=False,
            server_default=sa.text("true"),
        ),
    )

    op.add_column(
        "metadata_fields",
        sa.Column(
            "is_searchable",
            sa.Boolean(),
            nullable=False,
            server_default=sa.text("true"),
        ),
    )

    # Remove server defaults after populating existing rows
    op.alter_column("metadata_fields", "show_in_grid", server_default=None)
    op.alter_column("metadata_fields", "grid_order", server_default=None)
    op.alter_column("metadata_fields", "grid_width", server_default=None)
    op.alter_column("metadata_fields", "is_sortable", server_default=None)
    op.alter_column("metadata_fields", "is_filterable", server_default=None)
    op.alter_column("metadata_fields", "is_searchable", server_default=None)


def downgrade() -> None:
    """Downgrade schema."""

    op.drop_column("metadata_fields", "is_searchable")
    op.drop_column("metadata_fields", "is_filterable")
    op.drop_column("metadata_fields", "is_sortable")
    op.drop_column("metadata_fields", "grid_width")
    op.drop_column("metadata_fields", "grid_order")
    op.drop_column("metadata_fields", "show_in_grid")