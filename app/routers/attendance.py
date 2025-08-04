from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select
from app.config.db import engine
from app.models.attendance import Attendance
from app.schemas.attendance import AttendanceCreate, AttendanceRead
from typing import List

router = APIRouter()
@router.post("/", response_model=AttendanceRead)
def create_attendance(attendance: AttendanceCreate):
    """Mark attendance for a student in a course on a specific date."""

    with Session(engine) as session:
        exists = session.exec(
            select(Attendance).where(
                Attendance.student_id == attendance.student_id,
                Attendance.course_id == attendance.course_id,
                Attendance.date == attendance.date
            )
        ).first()
        if exists:
            raise HTTPException(status_code=400, detail="Attendance already marked for this date.")
        db_attendance = Attendance(**attendance.dict())
        session.add(db_attendance)
        session.commit()
        session.refresh(db_attendance)
        return db_attendance
@router.get("/", response_model=List[AttendanceRead])
def get_attendance():
    """Retrieve all attendance records."""

    with Session(engine) as session:
        return session.exec(select(Attendance)).all()