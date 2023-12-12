"""create_user_table

Revision ID: a02f5605865a
Revises: 
Create Date: 2023-12-10 20:59:21.114194

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a02f5605865a'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
"users",
sa.Column('id', sa.Integer, primary_key=True, index=True),
         sa.Column('user_name', sa.String, index=True),
         sa.Column('email', sa.String, index=True, unique=True),
         sa.Column('hashed_password', sa.String)
    )


def downgrade() -> None:
    op.drop_table('users')
