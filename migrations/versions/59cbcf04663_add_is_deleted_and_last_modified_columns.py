"""add is_deleted and last_modified columns

Revision ID: 59cbcf04663
Revises: 59935c933ab
Create Date: 2015-04-20 13:32:09.792703

"""

# revision identifiers, used by Alembic.
revision = '59cbcf04663'
down_revision = '59935c933ab'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('title_register_data', sa.Column('is_deleted', sa.Boolean(), nullable=True))
    title_register_data = table('title_register_data', column('is_deleted'))
    op.execute(title_register_data.update().values(is_deleted=False))
    op.alter_column('title_register_data', 'is_deleted', nullable=False)

    op.add_column('title_register_data', sa.Column('last_modified',
                                                   sa.types.DateTime(timezone=True),
                                                   nullable=True))
    title_register_data = table('title_register_data', column('last_modified'))
    op.execute(title_register_data.update().values(last_modified=sa.func.now()))
    op.alter_column('title_register_data', 'last_modified', nullable=False)

    op.create_index('idx_title_number_and_last_modified', 'title_register_data',
                    ['title_number', 'last_modified'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('idx_title_number_and_last_modified', table_name='title_register_data')
    op.drop_column('title_register_data', 'last_modified')
    op.drop_column('title_register_data', 'is_deleted')
    ### end Alembic commands ###
