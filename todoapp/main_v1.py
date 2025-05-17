from fastapi import FastAPI, HTTPException

api = FastAPI()

all_todos = [
    {"id": 1, "task": "Buy groceries", "completed": False},
    {"id": 2, "task": "Read a book", "completed": True},
    {"id": 3, "task": "Go for a walk", "completed": False}, 
    {"id": 4, "task": "Write code", "completed": True},
    {"id": 5, "task": "Clean the house", "completed": False},
]

@api.get("/")
def index():
    return {"message": "Welcome to the Todo API!"}

@api.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in all_todos:
        if todo["id"] == todo_id:
            return {'result': todo}

@api.get("/todos")
def get_todos(first_n: int = None):
    if first_n is not None:
        return {'result': all_todos[:first_n]}
    else:
        return {'result': all_todos}
    
@api.post("/todos")
def create_todo(todo: dict):
    new_todo = {
        "id": len(all_todos) + 1,
        "task": todo["task"],
        "completed": False
    }
    all_todos.append(new_todo)
    return {'result': new_todo}

@api.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated_todo: dict):
    for todo in all_todos:
        if todo["id"] == todo_id:
            todo["task"] = updated_todo["task"]
            todo["completed"] = updated_todo["completed"]
            return {'result': updated_todo}

@api.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for todo in all_todos:
        if todo["id"] == todo_id:
            all_todos.remove(todo)
            return {'result': todo} 