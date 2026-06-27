"""initial enterprise foundation

Revision ID: 0001_initial_foundation
Revises:
Create Date: 2026-06-27
"""
from alembic import op
from app.infrastructure.database.base import Base
from app.domain import models  # noqa: F401

revision = "0001_initial_foundation"
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    bind = op.get_bind()
    Base.metadata.create_all(bind=bind)

def downgrade() -> None:
    bind = op.get_bind()
    Base.metadata.drop_all(bind=bind)
