"""add message id to telemetry readings

Revision ID: 0002_message_id
Revises: 0001_devices_telemetry
Create Date: 2026-07-15
"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "0002_message_id"
down_revision: str | None = "0001_devices_telemetry"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.add_column("telemetry_readings", sa.Column("message_id", sa.String(length=120), nullable=True))
    op.execute("UPDATE telemetry_readings SET message_id = 'legacy-' || id WHERE message_id IS NULL")
    op.alter_column("telemetry_readings", "message_id", nullable=False)
    op.create_unique_constraint(
        "uq_telemetry_readings_message_id",
        "telemetry_readings",
        ["message_id"],
    )


def downgrade() -> None:
    op.drop_constraint("uq_telemetry_readings_message_id", "telemetry_readings", type_="unique")
    op.drop_column("telemetry_readings", "message_id")
