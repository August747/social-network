"""empty message

Revision ID: 4c53bd9890a2
Revises: 731aec227b45
Create Date: 2023-04-06 17:46:51.389490

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4c53bd9890a2'
down_revision = '731aec227b45'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password', sa.String(), nullable=True))
        batch_op.create_index(batch_op.f('ix_user_password'), ['password'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_password'))
        batch_op.drop_column('password')

    # ### end Alembic commands ###
