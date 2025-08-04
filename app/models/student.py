from sqlmodel import SQLModel, Field
from typing import Optional

class Student(SQLModel, table=True):
    """Database model for a student."""
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str
    age: int
