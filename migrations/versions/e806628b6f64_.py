"""empty message

Revision ID: e806628b6f64
Revises: 
Create Date: 2024-05-06 20:06:35.427270

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e806628b6f64'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('curso',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nome', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('unidadecompetencia', schema=None) as batch_op:
        batch_op.alter_column('numero',
               existing_type=mysql.INTEGER(),
               nullable=True)
        batch_op.alter_column('nome',
               existing_type=mysql.VARCHAR(length=250),
               type_=sa.String(length=200),
               nullable=True)
        batch_op.alter_column('carga_horaria',
               existing_type=mysql.INTEGER(),
               nullable=True)
        batch_op.alter_column('competencia_geral',
               existing_type=mysql.VARCHAR(length=250),
               type_=sa.String(length=255),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('unidadecompetencia', schema=None) as batch_op:
        batch_op.alter_column('competencia_geral',
               existing_type=sa.String(length=255),
               type_=mysql.VARCHAR(length=250),
               nullable=False)
        batch_op.alter_column('carga_horaria',
               existing_type=mysql.INTEGER(),
               nullable=False)
        batch_op.alter_column('nome',
               existing_type=sa.String(length=200),
               type_=mysql.VARCHAR(length=250),
               nullable=False)
        batch_op.alter_column('numero',
               existing_type=mysql.INTEGER(),
               nullable=False)

    op.drop_table('curso')
    # ### end Alembic commands ###