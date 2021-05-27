"""Initial migration

Revision ID: 3536f4ac076b
Revises: 
Create Date: 2021-05-26 22:27:20.939625

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3536f4ac076b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('public_id', sa.String(length=128), nullable=True),
    sa.Column('body', sa.Text(), nullable=True),
    sa.Column('created_datetime', sa.DateTime(), nullable=True),
    sa.Column('modified_datetime', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('public_id')
    )
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('public_id', sa.String(length=128), nullable=True),
    sa.Column('body', sa.Text(), nullable=True),
    sa.Column('created_datetime', sa.DateTime(), nullable=True),
    sa.Column('modified_datetime', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('public_id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('public_id', sa.String(length=128), nullable=True),
    sa.Column('profile_picture_path', sa.String(length=128), nullable=True),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('phone_nbr', sa.String(length=15), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=False),
    sa.Column('created_datetime', sa.DateTime(), nullable=True),
    sa.Column('modified_datetime', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('phone_nbr'),
    sa.UniqueConstraint('public_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('post')
    op.drop_table('comment')
    # ### end Alembic commands ###
