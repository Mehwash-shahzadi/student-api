from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select
from app.config.db import engine
from app.models.course import Course
from app.schemas.course import CourseCreate, CourseRead
from typing import List

router = APIRouter()

@router.post("/", response_model=CourseRead)
def create_course(course: CourseCreate):
    """Create a new course if the title is unique."""

    with Session(engine) as session:
        existing_course = session.exec(select(Course).where(Course.title == course.title)).first()
        if existing_course:
            raise HTTPException(status_code=400, detail="Course with this title already exists.")
        db_course = Course(**course.dict())
        session.add(db_course)
        session.commit()
        session.refresh(db_course)
        return db_course
    
@router.get("/", response_model=List[CourseRead])
def get_courses():
    """Retrieve a list of all available courses."""

    with Session(engine) as session:
        return session.exec(select(Course)).all()