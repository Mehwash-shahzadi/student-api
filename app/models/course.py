from sqlmodel import SQLModel, Field
from typing import Optional

class Course(SQLModel, table=True):
    """Database model for a course."""
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: str