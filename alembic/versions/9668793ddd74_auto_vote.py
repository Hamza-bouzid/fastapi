"""auto-vote

Revision ID: 9668793ddd74
Revises: 806510d61080
Create Date: 2024-03-24 16:03:54.394643

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '9668793ddd74'
down_revision: Union[str, None] = '806510d61080'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('votes',
                    sa.Column('user_id', sa.Integer(), nullable=False),
                    sa.Column('post_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ondelete='CASCADE'),
                    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('user_id', 'post_id')
                    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('votes')
    # ### end Alembic commands ###
