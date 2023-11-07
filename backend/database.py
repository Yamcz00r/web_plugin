from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os 
from dotenv import load_dotenv


url = "postgresql://postgres:zaq12wsx@localhost:5432/postgres"
load_dotenv()


engine = create_engine(
    os.getenv("DATABASE_URL")
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False,  bind=engine)

Base = declarative_base()
