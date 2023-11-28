"""create_users_table

Revision ID: 877c5db4bbfb
Revises: 
Create Date: 2023-11-23 12:34:56.789012

"""
from alembic import op
import sqlalchemy as sa

revision = '877c5db4bbfb'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String(50), nullable=False),
        sa.Column('password', sa.String(255), nullable=False),
        sa.Column('email', sa.String(255), nullable=False),
    )

def downgrade():
    op.drop_table('users')
    # Dodaj inne instrukcje SQL degradacji, jeśli są potrzebne
