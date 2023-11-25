import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

RUNNING_INSIDE_GITHUB_ACTIONS = os.getenv("RUNNING_INSIDE_GITHUB_ACTIONS", False)

if not RUNNING_INSIDE_GITHUB_ACTIONS:
    engine = create_engine(os.environ["DB_CONNECTION_URL"])
else:
    engine = create_engine(
        os.environ["DB_CONNECTION_URL"],
        connect_args={"check_same_thread": False}
    )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()