"""
Task 94

Configure Alembic Environment
"""

from models import Base

# Alembic will compare ORM models
# against the existing database.

target_metadata = Base.metadata

"""
Offline Migration

Alembic can generate SQL scripts
without connecting to the database.
"""

def run_migrations_offline():

    pass


"""
Online Migration

Alembic connects to the database
and applies migrations.
"""

def run_migrations_online():

    pass


"""
Run the appropriate migration mode.
"""

if __name__ == "__main__":

    run_migrations_online()
