Alembic Migration Folder

This folder stores all migration files.

Contents

1. env.py
2. versions/

Migration files are automatically generated using

alembic revision --autogenerate

Each migration contains

upgrade()

downgrade()

functions.

Alembic tracks migration history using

alembic_version table.
