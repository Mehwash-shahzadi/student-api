from pydantic import BaseModel

"""Schemas for course creation and retrieval."""

class CourseCreate(BaseModel):
    """Schema for creating a course."""
    title: str
    description: str

class CourseRead(CourseCreate):
    """Schema for reading a course with ID."""
    id: int