from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select
from app.config.db import engine
from app.models.enrollment import Enrollment
from app.schemas.enrollment import EnrollmentCreate, EnrollmentRead
from typing import List

router = APIRouter()

@router.post("/", response_model=EnrollmentRead)
def create_enrollment(enrollment: EnrollmentCreate):
    """Enroll a student in a course if not already enrolled."""

    with Session(engine) as session:
        exists = session.exec(
            select(Enrollment).where(
                Enrollment.student_id == enrollment.student_id,
                Enrollment.course_id == enrollment.course_id
            )
        ).first()
        if exists:
            raise HTTPException(status_code=400, detail="Student already enrolled in this course.")
        db_enroll = Enrollment(**enrollment.dict())
        session.add(db_enroll)
        session.commit()
        session.refresh(db_enroll)
        return db_enroll
    
@router.get("/", response_model=List[EnrollmentRead])
def get_enrollments():
    """Retrieve all student-course enrollment records."""

    with Session(engine) as session:
        return session.exec(select(Enrollment)).all()