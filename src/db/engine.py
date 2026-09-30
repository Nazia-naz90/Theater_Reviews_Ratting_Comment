# engine.py

from sqlmodel import create_engine, SQLModel , Session
import src.models.model as model

# Database ko create krnay ka engine
database_url = "sqlite:///database.db"
engine = create_engine(database_url, echo = True)


def create_tables():
    SQLModel.metadata.create_all(engine) # Create Table


def get_session():
   with Session(engine) as session:
       yield session
