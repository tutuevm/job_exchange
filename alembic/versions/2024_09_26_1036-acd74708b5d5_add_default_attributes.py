"""add default attributes

Revision ID: acd74708b5d5
Revises: 605906ef0850
Create Date: 2024-09-26 10:36:29.618007

"""

from typing import Sequence, Union
from uuid import uuid4

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "acd74708b5d5"
down_revision: Union[str, None] = "605906ef0850"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        f"""
    INSERT INTO user_attributes VALUES
    ('{uuid4()}', 'role', 'manager'),
    ('{uuid4()}', 'role', 'user'),
    ('{uuid4()}', 'role', 'admin');
    """
    )


def downgrade() -> None:
    op.execute(
        "DELETE FROM user_attributes WHERE value IN ('user', 'manager', 'admin')"
    )
