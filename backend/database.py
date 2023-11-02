from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



url = "postgresql://postgres:zaq12wsx@localhost:5432/postgres"

engine = create_engine(
    url
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False,  bind=engine)

Base = declarative_base()
