from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
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
#READ
@app.get("/students")
def getTodo():
    return students
#CREATE
@app.post("/addStudent")
def addStudent(student:Student): # its a type hint . Accepts and validates JSON input using Pydantic
    for s in students:
        if s["rollno"] == student.rollno:
                        raise HTTPException(status_code=400, detail="Roll number already exists")
    students.append(student.dict())
    return {"message": "Student added successfully", "students": students}

# DELETE: 
@app.delete("/students/{rollno}")
def delete_student(rollno: int):
    for s in students:
        if s["rollno"] == rollno:
            students.remove(s)
            return {"message": "Student deleted", "students": students}
    raise HTTPException(status_code=404, detail="Student not found")

# UPDATE:
@app.put("/students/{rollno}")
def update_student(rollno: int, updated_student: Student):
    for index, s in enumerate(students):
        if s["rollno"] == rollno:
            students[index] = updated_student.dict()
            return {"message": "Student updated", "students": students}
    raise HTTPException(status_code=404, detail="Student not found")


