"""empty message

Revision ID: 514633d38f49
Revises: 44c4b631371d
Create Date: 2023-04-28 10:57:49.881987

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '514633d38f49'
down_revision = '44c4b631371d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('profiles', schema=None) as batch_op:
        batch_op.add_column(sa.Column('linkedin_url', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('facebook_url', sa.String(), nullable=True))
        batch_op.drop_column('bio')

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('linkedin_url', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('facebook_url', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('facebook_url')
        batch_op.drop_column('linkedin_url')

    with op.batch_alter_table('profiles', schema=None) as batch_op:
        batch_op.add_column(sa.Column('bio', sa.VARCHAR(), autoincrement=False, nullable=True))
        batch_op.drop_column('facebook_url')
        batch_op.drop_column('linkedin_url')

    # ### end Alembic commands ###
