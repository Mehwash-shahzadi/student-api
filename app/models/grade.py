from sqlmodel import SQLModel, Field
from typing import Optional

class Grade(SQLModel, table=True):
    """Database model for a grade entry."""
    id: Optional[int] = Field(default=None, primary_key=True)
    enrollment_id: int
    grade: str