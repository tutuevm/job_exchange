"""remove tables job status and job type

Revision ID: d4f28b6e0a95
Revises: 7928962fd780
Create Date: 2024-07-29 21:15:17.821485

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd4f28b6e0a95'
down_revision: Union[str, None] = '7928962fd780'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('job_status')
    op.drop_table('job_types')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('job_types',
    sa.Column('id', sa.UUID(), autoincrement=False, nullable=False),
    sa.Column('title', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='job_types_pkey')
    )
    op.create_table('job_status',
    sa.Column('id', sa.UUID(), autoincrement=False, nullable=False),
    sa.Column('title', sa.VARCHAR(length=20), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='job_status_pkey')
    )
    # ### end Alembic commands ###
