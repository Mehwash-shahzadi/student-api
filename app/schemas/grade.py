from pydantic import BaseModel

"""Schemas for grades creation and retrieval."""

class GradeCreate(BaseModel):
    """Schema for creating a grade entry."""
    enrollment_id: int
    grade: str

class GradeRead(GradeCreate):
    """Schema for reading a grade entry with ID."""
    id: int