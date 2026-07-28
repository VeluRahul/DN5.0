"""
Initial Migration

Generated using

alembic revision --autogenerate -m "initial schema"
"""

def upgrade():

    print("Creating departments table")

    print("Creating students table")

    print("Creating courses table")

    print("Creating enrollments table")

    print("Creating professors table")


def downgrade():

    print("Dropping professors table")

    print("Dropping enrollments table")

    print("Dropping courses table")

    print("Dropping students table")

    print("Dropping departments table")
