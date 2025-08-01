from fastapi import FastAPI, HTTPException
from sqlmodel import Session, select
from dotenv import load_dotenv
load_dotenv()


from .models.todos import Todo, UpdateTodo, CreateTodo
from .config.db import create_tables, engine


app = FastAPI()

# Ensure tables are created at startup
create_tables()

@app.get("/get_todos")
def get_todos():
    with Session(engine) as session:
        statement = select(Todo)
        results = session.exec(statement)
        data = results.all()
        print("Fetched:", data)
        return data

@app.post("/create_todo")
def create_todo(todo: CreateTodo):
    with Session(engine) as session:
        new_todo = Todo(**todo.dict())
        session.add(new_todo)
        session.commit()
        session.refresh(new_todo)
        return new_todo

@app.put("/update_todo/{id}")
def update_todo(id: int, todo: UpdateTodo):
    with Session(engine) as session:
        db_todo = session.get(Todo, id)
        if not db_todo:
            raise HTTPException(status_code=404, detail="Todo not found")
        todo_data = todo.model_dump(exclude_unset=True)
        db_todo.sqlmodel_update(todo_data)
        session.add(db_todo)
        session.commit()
        session.refresh(db_todo)
        return db_todo

@app.delete("/delete_todo/{todo_id}")
def delete_todo(todo_id: int):
    with Session(engine) as session:
        db_todo = session.get(Todo, todo_id)
        if not db_todo:
            raise HTTPException(status_code=404, detail="Todo not found")
        session.delete(db_todo)
        session.commit()
        return {"message": "Todo deleted successfully"}




      

