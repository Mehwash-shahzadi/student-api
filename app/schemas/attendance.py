from pydantic import BaseModel

"""Schemas for attendance creation and retrieval."""
class AttendanceCreate(BaseModel):
    """Schema for creating an attendance record."""
    student_id: int
    course_id: int
    date: str
    status: str

class AttendanceRead(AttendanceCreate):
    """Schema for reading an attendance record with ID."""
    id: int