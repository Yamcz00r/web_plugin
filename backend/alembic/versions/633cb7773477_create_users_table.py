
"""create_users_table

Revision ID: 40b49780
Revises: 
Create Date: 2023-11-28 22:13:53

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '40b49780'
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
