"""Add Validation model

Revision ID: 9486941ad9cd
Revises: 73b223519cdb
Create Date: 2016-03-03 11:38:14.372962

"""
# This line added manually!
import config

# revision identifiers, used by Alembic.
revision = '9486941ad9cd'
down_revision = '73b223519cdb'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    # This line added manually! [Original: op.create_table('validation',]
    validation_table = op.create_table('validation',
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('product', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('price')
    )
    ### end Alembic commands ###

    # This line added manually!
    price = int(config.CONFIG_DICT['NOMINAL_PRICE'])
    op.bulk_insert(validation_table, [{'price': price, 'product': 'drvSummary'}])

def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('validation')
    ### end Alembic commands ###
