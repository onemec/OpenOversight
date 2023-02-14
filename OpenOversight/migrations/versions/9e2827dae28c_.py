"""Add cascading foreign key constraint to assignments

Revision ID: 9e2827dae28c
Revises: 0acbb0f0b1ef
Create Date: 2018-08-13 13:18:15.381300

"""
from alembic import op

# revision identifiers, used by Alembic.
revision = "9e2827dae28c"
down_revision = "0acbb0f0b1ef"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint("assignments_officer_id_fkey", "assignments", type_="foreignkey")
    op.create_foreign_key(
        None, "assignments", "officers", ["officer_id"], ["id"], ondelete="CASCADE"
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "assignments", type_="foreignkey")
    op.create_foreign_key(
        "assignments_officer_id_fkey", "assignments", "officers", ["officer_id"], ["id"]
    )
    # ### end Alembic commands ###
