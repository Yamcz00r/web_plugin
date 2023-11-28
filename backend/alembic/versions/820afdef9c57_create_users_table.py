
"""create_users_table

Revision ID: 972e1345
Revises: 
Create Date: 2023-11-28 22:08:47

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '972e1345'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_name', sa.String(50), nullable=False),
        sa.Column('email', sa.String(255), nullable=False),
        sa.Column('hashed_password', sa.String(255), nullable=False),
    )


def downgrade():
    op.drop_table('users')
