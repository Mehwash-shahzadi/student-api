from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select
from app.config.db import engine
from app.models.grade import Grade
from app.schemas.grade import GradeCreate, GradeRead
from typing import List

router = APIRouter()
@router.post("/", response_model=GradeRead)
def create_grade(grade: GradeCreate):

    """Create a new grade for an existing enrollment."""

    with Session(engine) as session:
        from app.models.enrollment import Enrollment
        enrollment = session.exec(select(Enrollment).where(Enrollment.id == grade.enrollment_id)).first()
        if not enrollment:
            raise HTTPException(status_code=404, detail="Enrollment not found.")
        db_grade = Grade(**grade.dict())
        session.add(db_grade)
        session.commit()
        session.refresh(db_grade)
        return db_grade

@router.get("/", response_model=List[GradeRead])
def get_grades():
    """Retrieve a list of all grade records."""

    with Session(engine) as session:
        return session.exec(select(Grade)).all()