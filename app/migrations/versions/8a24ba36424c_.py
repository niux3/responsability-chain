"""empty message

Revision ID: 8a24ba36424c
Revises: 
Create Date: 2025-01-24 14:13:30.515749

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8a24ba36424c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('website', sa.String(), nullable=True),
    sa.Column('phone', sa.String(), nullable=True),
    sa.Column('sex', sa.String(), nullable=True),
    sa.Column('ssn', sa.String(), nullable=True),
    sa.Column('birthday', sa.Date(), nullable=True),
    sa.Column('address_city', sa.String(), nullable=True),
    sa.Column('address_street', sa.String(), nullable=True),
    sa.Column('address_zipcode', sa.String(), nullable=True),
    sa.Column('address_lat', sa.Numeric(precision=9, scale=7), nullable=True),
    sa.Column('address_long', sa.Numeric(precision=9, scale=7), nullable=True),
    sa.Column('company', sa.String(), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('updated', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('ssn')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
