from sqlmodel import SQLModel, Field
from typing import Optional

class Attendance(SQLModel, table=True):
    """Database model for a attendance entry."""
    id: Optional[int] = Field(default=None, primary_key=True)
    student_id: int
    course_id: int
    date: str
    status: str