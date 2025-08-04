from sqlmodel import SQLModel, Field
from typing import Optional

class Enrollment(SQLModel, table=True):
    """Database model for a enrollment entry."""
    id: Optional[int] = Field(default=None, primary_key=True)
    student_id: int
    course_id: int