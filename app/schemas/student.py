from pydantic import BaseModel

"""Schemas for student creation and retrieval."""

class StudentCreate(BaseModel):
    """Schema for creating a student."""
    name: str
    email: str
    age: int

class StudentRead(StudentCreate):
    """Schema for reading a student with ID."""
    id: int
