"""add users table

Revision ID: aefcecb43453
Revises: 8af436ed2cdc
Create Date: 2024-03-24 15:50:24.749972

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'aefcecb43453'
down_revision: Union[str, None] = '8af436ed2cdc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'),
                              nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )


def downgrade() -> None:
    op.drop_table('users')
