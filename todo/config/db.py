from sqlmodel import SQLModel, create_engine
import os

DATABASE_URL =os.getenv('DB_SECRET_STRING')
engine = create_engine(DATABASE_URL, echo=True)

def create_tables():
    SQLModel.metadata.create_all(engine)