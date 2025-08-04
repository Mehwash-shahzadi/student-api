from pydantic import BaseModel

"""Schemas enrollment creation and retrieval."""

class EnrollmentCreate(BaseModel):
    """Schema for creating an enrollment."""
    student_id: int
    course_id: int

class EnrollmentRead(EnrollmentCreate):
    """Schema for reading an enrollment with ID."""
    id: int