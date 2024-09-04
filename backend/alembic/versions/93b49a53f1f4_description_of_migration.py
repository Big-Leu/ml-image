"""Description of migration

Revision ID: 93b49a53f1f4
Revises: b8cb965784a1
Create Date: 2024-05-15 18:47:04.835384

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '93b49a53f1f4'
down_revision: Union[str, None] = 'b8cb965784a1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('mymodel',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('contact_number', sa.String(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('mymodel')
    # ### end Alembic commands ###
