from sqlmodel import SQLModel, Field

class Todo(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)  
    title: str
    description: str
    is_completed: bool

class CreateTodo(SQLModel):
    title: str
    description: str
    is_completed: bool

class UpdateTodo(SQLModel):
    title: str | None = None
    description: str | None = None
    is_completed: bool | None = None
