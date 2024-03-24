"""create posts table

Revision ID: 8af436ed2cdc
Revises: 
Create Date: 2024-03-24 15:41:19.443111

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '8af436ed2cdc'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('title', sa.String(), nullable=False),
                    sa.Column('content', sa.String(), nullable=False),
                    sa.Column('published', sa.Boolean(), server_default='TRUE', nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False,
                              server_default=sa.text('now()')),
                    )


def downgrade() -> None:
    op.drop_table('posts')
