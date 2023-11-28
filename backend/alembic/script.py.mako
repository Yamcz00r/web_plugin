<%
    import time
    import uuid
    from alembic import op
    from sqlalchemy import String, Column

    # Set your model and table name here
    model = 'users'
    table = 'users'
    # Generate short UUID
    short_uuid = str(uuid.uuid4())[:8]
%>
"""create_users_table

Revision ID: ${short_uuid}
Revises: 
Create Date: ${time.strftime('%Y-%m-%d %H:%M:%S')}

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '${short_uuid}'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        '${table}',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_name', sa.String(50), nullable=False),
        sa.Column('email', sa.String(255), nullable=False),
        sa.Column('hashed_password', sa.String(255), nullable=False),
    )


def downgrade():
    op.drop_table('${table}')
