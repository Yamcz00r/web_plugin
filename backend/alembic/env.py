# alembic/env.py
from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context


# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name, disable_existing_loggers=False)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = None

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.

# here we call on the engine configuration we set up in engineio.py
# from myapp import engineio
# connectable = engineio.get_engine()
# or
# from myapp import db
# connectable = db.engine

# ensure your target database is set here
# if not 'my_database' in target_metadata.tables:
#     target_metadata.reflect(only=['my_table'], views=True)

config.set_main_option('sqlalchemy.url', 'postgresql+psycopg2://root:secret@postgres:5432/mydatabase')
