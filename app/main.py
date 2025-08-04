from fastapi import FastAPI
from app.config.db import init_db
from app.routers import student, course, enrollment, grade,attendance

app = FastAPI(title="Student Management System")

# Initialize the database
init_db()

# Include routers
app.include_router(student.router, prefix="/students", tags=["Students"])
app.include_router(course.router, prefix="/courses", tags=["Courses"])
app.include_router(enrollment.router, prefix="/enrollments", tags=["Enrollments"])
app.include_router(grade.router, prefix="/grades", tags=["Grades"])
app.include_router(attendance.router, prefix="/attendance", tags=["Attendance"])





      

