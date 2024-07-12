"""renamed place and action_type; places id changed from int to uuid

Revision ID: b48ef407144f
Revises: 99f698b5d263
Create Date: 2024-07-12 16:42:11.739895

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b48ef407144f'
down_revision: Union[str, None] = '99f698b5d263'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('action_types',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('title', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('places',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    op.drop_table('action_type')
    op.drop_table('place')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('place',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('title', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='place_pkey'),
    sa.UniqueConstraint('title', name='place_title_key')
    )
    op.create_table('action_type',
    sa.Column('id', sa.UUID(), autoincrement=False, nullable=False),
    sa.Column('title', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='action_type_pkey')
    )
    op.drop_table('places')
    op.drop_table('action_types')
    # ### end Alembic commands ###
