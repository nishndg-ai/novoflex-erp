"""add master history and audit tables

Revision ID: f823db017ad9
Revises: 35f804ff5d40
Create Date: 2026-07-27 16:48:54.470841

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "f823db017ad9"

down_revision: Union[str, Sequence[str], None] = "35f804ff5d40"

branch_labels: Union[str, Sequence[str], None] = None

depends_on: Union[str, Sequence[str], None] = None



def upgrade() -> None:
    """Upgrade schema."""

    # ===============================
    # Master History Table
    # ===============================

    op.create_table(
        "master_history",

        sa.Column(
            "id",
            sa.Integer(),
            nullable=False,
        ),

        sa.Column(
            "module",
            sa.String(length=100),
            nullable=False,
        ),

        sa.Column(
            "record_id",
            sa.Integer(),
            nullable=False,
        ),

        sa.Column(
            "action",
            sa.String(length=50),
            nullable=False,
        ),

        sa.Column(
            "old_data",
            sa.JSON(),
            nullable=True,
        ),

        sa.Column(
            "new_data",
            sa.JSON(),
            nullable=True,
        ),

        sa.Column(
            "reason",
            sa.Text(),
            nullable=True,
        ),

        sa.Column(
            "changed_by",
            sa.String(length=100),
            nullable=True,
        ),

        sa.Column(
            "changed_at",
            sa.DateTime(),
            nullable=True,
        ),

        sa.PrimaryKeyConstraint(
            "id"
        ),
    )


    # ===============================
    # Audit Log Table
    # ===============================

    op.create_table(
        "audit_log",

        sa.Column(
            "id",
            sa.Integer(),
            nullable=False,
        ),

        sa.Column(
            "module",
            sa.String(length=100),
            nullable=False,
        ),

        sa.Column(
            "action",
            sa.String(length=50),
            nullable=False,
        ),

        sa.Column(
            "record_id",
            sa.Integer(),
            nullable=True,
        ),

        sa.Column(
            "user",
            sa.String(length=100),
            nullable=True,
        ),

        sa.Column(
            "old_data",
            sa.JSON(),
            nullable=True,
        ),

        sa.Column(
            "new_data",
            sa.JSON(),
            nullable=True,
        ),

        sa.Column(
            "created_at",
            sa.DateTime(),
            nullable=True,
        ),

        sa.PrimaryKeyConstraint(
            "id"
        ),
    )



def downgrade() -> None:
    """Downgrade schema."""

    op.drop_table(
        "audit_log"
    )


    op.drop_table(
        "master_history"
    )