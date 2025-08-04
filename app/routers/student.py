from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select
from app.config.db import engine
from app.models.student import Student
from app.schemas.student import StudentCreate, StudentRead
from typing import List

router = APIRouter()
@router.post("/", response_model=StudentRead)
def create_student(student: StudentCreate):
    """Create a new student record if the email is not already registered."""
    with Session(engine) as session:
        existing_student = session.exec(select(Student).where(Student.email == student.email)).first()
        if existing_student:
            raise HTTPException(status_code=400, detail="Student with this email already exists.")
        db_student = Student(**student.dict())
        session.add(db_student)
        session.commit()
        session.refresh(db_student)
        return db_student
    
@router.get("/", response_model=List[StudentRead])
def get_students():
    """Retrieve a list of all student records from the database."""

    with Session(engine) as session:
        students = session.exec(select(Student)).all()
        return students
    
@router.put("/{id}", response_model=StudentRead)
def update_student(id: int, updated_student: StudentCreate):
    """Update an existing student's information using their ID."""

    with Session(engine) as session:
        student = session.get(Student, id)
        if not student:
            raise HTTPException(status_code=404, detail="Student not found")

        for key, value in updated_student.dict().items():
            setattr(student, key, value)

        session.add(student)
        session.commit()
        session.refresh(student)
        return student


@router.delete("/{id}")
def delete_student(id: int):
    """Delete a student from the database using their ID."""

    with Session(engine) as session:
        student = session.get(Student, id)
        if not student:
            raise HTTPException(status_code=404, detail="Student not found")

        session.delete(student)
        session.commit()
        return {"message": "Student deleted successfully"}
