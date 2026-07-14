from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, field_validator
from typing import Optional


app = FastAPI(title="Task API", version="1.0")
tasks = [
    {"id": 1, "title": "Buy milk", "done": False},
    {"id": 2, "title": "Walk the dog", "done": True},
    {"id": 3, "title": "Learn FastAPI", "done": False},
]
class TaskUpdate(BaseModel):
    title: Optional[str] = None
    done: Optional[bool] = None

class TaskCreate(BaseModel):
    title: str

    @field_validator("title")
    @classmethod
    def title_not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError("title must not be empty")
        return v

@app.get("/")
def root():
    return {
        "name": "Task API",
        "version": "1.0",
        "endpoints": ["/tasks"]
    }

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/tasks", summary="List all tasks")
def get_tasks():
    return tasks

@app.get("/tasks/{task_id}", summary="Get a single task by id")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail=f"Task {task_id} not found")

@app.post("/tasks", status_code=201, summary="Create a new task")
def create_task(task: TaskCreate):
    new_id = max((t["id"] for t in tasks), default=0) + 1
    new_task = {"id": new_id, "title": task.title, "done": False}
    tasks.append(new_task)
    return new_task

@app.put("/tasks/{task_id}", summary="Update a task's title and/or done status")
def update_task(task_id: int, update: TaskUpdate):
    for task in tasks:
        if task["id"] == task_id:
            if update.title is not None:
                if not update.title.strip():
                    raise HTTPException(status_code=400, detail="title must not be empty")
                task["title"] = update.title
            if update.done is not None:
                task["done"] = update.done
            return task
    raise HTTPException(status_code=404, detail=f"Task {task_id} not found")

@app.delete("/tasks/{task_id}", status_code=204, summary="Delete a task")
def delete_task(task_id: int):
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            tasks.pop(i)
            return
    raise HTTPException(status_code=404, detail=f"Task {task_id} not found")    