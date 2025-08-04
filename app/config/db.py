from sqlmodel import SQLModel, create_engine
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DB_SECRET_STRING")
engine = create_engine(DATABASE_URL, echo=True)

def init_db():
    from app.models import student, course, enrollment, grade, attendance
    SQLModel.metadata.create_all(engine)
