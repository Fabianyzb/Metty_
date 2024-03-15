"""empty message

Revision ID: b282ea605d84
Revises: 
Create Date: 2023-12-12 05:44:58.467742

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b282ea605d84'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('alumnos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=120), nullable=False),
    sa.Column('apellidos', sa.String(length=120), nullable=False),
    sa.Column('correo_electronico', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=120), nullable=False),
    sa.Column('tipo_de_cuenta', sa.Boolean(), nullable=False),
    sa.Column('conectado', sa.Boolean(), nullable=False),
    sa.Column('estado', sa.Boolean(), nullable=False),
    sa.Column('solicitud_saliente', sa.Boolean(), nullable=False),
    sa.Column('alumno_en_sala', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('correo_electronico')
    )
    op.create_table('area',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('tutores',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=120), nullable=False),
    sa.Column('apellidos', sa.String(length=120), nullable=False),
    sa.Column('correo_electronico', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=120), nullable=False),
    sa.Column('tipo_de_cuenta', sa.Boolean(), nullable=False),
    sa.Column('conectado', sa.Boolean(), nullable=False),
    sa.Column('estado', sa.Boolean(), nullable=False),
    sa.Column('solicitud_entrante', sa.Boolean(), nullable=False),
    sa.Column('tutor_en_sala', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('correo_electronico')
    )
    op.create_table('categorias',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre_materia', sa.String(), nullable=False),
    sa.Column('alumno_id', sa.Integer(), nullable=False),
    sa.Column('tutor_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['alumno_id'], ['alumnos.id'], ),
    sa.ForeignKeyConstraint(['tutor_id'], ['tutores.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nombre_materia')
    )
    op.create_table('cuentas_bancarias',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tipo_de_cuenta', sa.Boolean(), nullable=False),
    sa.Column('numero_cuenta', sa.Integer(), nullable=False),
    sa.Column('banco', sa.ARRAY(sa.String()), nullable=True),
    sa.Column('tutor_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['tutor_id'], ['tutores.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('numero_cuenta')
    )
    op.create_table('metodos_de_pago',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre_titular', sa.String(), nullable=False),
    sa.Column('numero_tarjeta', sa.Integer(), nullable=False),
    sa.Column('fecha_vencimiento', sa.Integer(), nullable=False),
    sa.Column('cvv', sa.Integer(), nullable=False),
    sa.Column('alumno_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['alumno_id'], ['alumnos.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cvv'),
    sa.UniqueConstraint('numero_tarjeta')
    )
    op.create_table('perfiles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('profile_img', sa.String(length=240), nullable=True),
    sa.Column('alumno_id', sa.Integer(), nullable=False),
    sa.Column('tutor_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['alumno_id'], ['alumnos.id'], ),
    sa.ForeignKeyConstraint(['tutor_id'], ['tutores.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('solicitud_sala',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('confirmacion_tutor', sa.Boolean(), nullable=True),
    sa.Column('estado', sa.Boolean(), nullable=True),
    sa.Column('alumno_id', sa.Integer(), nullable=False),
    sa.Column('tutor_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['alumno_id'], ['alumnos.id'], ),
    sa.ForeignKeyConstraint(['tutor_id'], ['tutores.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tema',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('area_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['area_id'], ['area.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('materia',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('tema_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['tema_id'], ['tema.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('salas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('solicitud_sala_id', sa.Integer(), nullable=False),
    sa.Column('alumno_id', sa.Integer(), nullable=False),
    sa.Column('tutor_id', sa.Integer(), nullable=False),
    sa.Column('estado_sala', sa.Boolean(), nullable=False),
    sa.Column('finalizar_alumno', sa.Boolean(), nullable=False),
    sa.Column('finalizar_tutor', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['alumno_id'], ['alumnos.id'], ),
    sa.ForeignKeyConstraint(['solicitud_sala_id'], ['solicitud_sala.id'], ),
    sa.ForeignKeyConstraint(['tutor_id'], ['tutores.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('solicitud_sala_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('salas')
    op.drop_table('materia')
    op.drop_table('tema')
    op.drop_table('solicitud_sala')
    op.drop_table('perfiles')
    op.drop_table('metodos_de_pago')
    op.drop_table('cuentas_bancarias')
    op.drop_table('categorias')
    op.drop_table('tutores')
    op.drop_table('area')
    op.drop_table('alumnos')
    # ### end Alembic commands ###
