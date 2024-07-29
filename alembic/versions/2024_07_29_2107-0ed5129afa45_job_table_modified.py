"""job table modified

Revision ID: 0ed5129afa45
Revises: 63f36a90c868
Create Date: 2024-07-29 21:07:19.470975

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0ed5129afa45'
down_revision: Union[str, None] = '63f36a90c868'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('jobs', sa.Column('status_value', sa.Enum('DRAFT', 'CRATED', 'ANDER_REVIEW', 'COMPLETED', 'CLOSED', name='jobstatusschema'), nullable=False))
    op.add_column('jobs', sa.Column('type_value', sa.Enum('HOURLY_PAY', 'SALARY', name='jobtypeschema'), nullable=False))
    op.create_index(op.f('ix_jobs_status_value'), 'jobs', ['status_value'], unique=False)
    op.create_index(op.f('ix_jobs_type_value'), 'jobs', ['type_value'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_jobs_type_value'), table_name='jobs')
    op.drop_index(op.f('ix_jobs_status_value'), table_name='jobs')
    op.drop_column('jobs', 'type_value')
    op.drop_column('jobs', 'status_value')
    # ### end Alembic commands ###
