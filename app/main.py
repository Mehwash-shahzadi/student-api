from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    """Data model for a student."""
    name: str
    rollno: int

students=[
    {
        "name":"mishi",
        "rollno":23
    },
    {
        "name":"muteem",
        "rollno":26
    }
]

@app.get("/students")
def getTodo():
    """Retrieve the list of all students."""
    return students

@app.post("/addStudent")
def addStudent(student:Student): # its a type hint . Accepts and validates JSON input using Pydantic
    """Add a new student to the list.Raises 400 if the roll number already exists."""
    for s in students:
        if s["rollno"] == student.rollno:
                        raise HTTPException(status_code=400, detail="Roll number already exists")
    students.append(student.dict())
    return {"message": "Student added successfully", "students": students}


@app.delete("/students/{rollno}")
def delete_student(rollno: int):
    """ Delete a student by roll number.Raises 404 if the student is not found."""
    for s in students:
        if s["rollno"] == rollno:
            students.remove(s)
            return {"message": "Student deleted", "students": students}
    raise HTTPException(status_code=404, detail="Student not found")

#
@app.put("/students/{rollno}")
def update_student(rollno: int, updated_student: Student):
    """Update a student's information by roll number.Raises 404 if the student is not found."""
    for index, s in enumerate(students):
        if s["rollno"] == rollno:
            students[index] = updated_student.dict()
            return {"message": "Student updated", "students": students}
    raise HTTPException(status_code=404, detail="Student not found")


