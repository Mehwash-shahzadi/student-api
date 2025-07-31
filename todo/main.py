from sqlmodel import Field, Session, SQLModel, create_engine, select
from fastapi import FastAPI

app = FastAPI()

DATABASE_URL = "postgresql://postgres:route@localhost:5432/studentdb"
engine = create_engine(DATABASE_URL, echo=True)

class Student(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    age: int
    is_active: bool

SQLModel.metadata.create_all(engine)

@app.get("/getStudents")
def getStudents():
    with Session(engine) as session:
        statement = select(Student)
        results = session.exec(statement)
        data = results.all()
        print("Fetched:", data)
        return data
    
@app.post("/addStudent")
def add_student(student: Student):
    with Session(engine) as session:
        session.add(student)
        session.commit()
        session.refresh(student)
        return student