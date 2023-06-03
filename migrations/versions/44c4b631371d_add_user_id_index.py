"""add user id index

Revision ID: 44c4b631371d
Revises: 11a32e15d289
Create Date: 2023-04-25 17:56:20.881808

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '44c4b631371d'
down_revision = '11a32e15d289'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('profiles', schema=None) as batch_op:
        batch_op.create_index('idx_profiles_user_id', ['user_id'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('profiles', schema=None) as batch_op:
        batch_op.drop_index('idx_profiles_user_id')

    # ### end Alembic commands ###