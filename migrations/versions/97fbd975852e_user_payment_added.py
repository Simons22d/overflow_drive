"""user/payment/added

Revision ID: 97fbd975852e
Revises: f21ede423cc2
Create Date: 2020-07-31 20:08:06.411536

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '97fbd975852e'
down_revision = 'f21ede423cc2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('mpesa', sa.Column('user', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'mpesa', 'user', ['user'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'mpesa', type_='foreignkey')
    op.drop_column('mpesa', 'user')
    # ### end Alembic commands ###
