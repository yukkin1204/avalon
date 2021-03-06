"""empty message

Revision ID: 57bd7eeb2fa9
Revises: 
Create Date: 2020-06-12 23:17:57.779051

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '57bd7eeb2fa9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('divination',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('round', sa.Integer(), nullable=False),
    sa.Column('maiden_id', sa.Integer(), nullable=False),
    sa.Column('target_id', sa.Integer(), nullable=False),
    sa.Column('is_spy', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('game',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=32), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('progress', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=16), nullable=False),
    sa.Column('is_spy', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.String(length=16), nullable=False),
    sa.Column('password', sa.String(length=16), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('vote',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('round', sa.Integer(), nullable=False),
    sa.Column('phase', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('is_approve', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vote')
    op.drop_table('user')
    op.drop_table('role')
    op.drop_table('game')
    op.drop_table('divination')
    # ### end Alembic commands ###
