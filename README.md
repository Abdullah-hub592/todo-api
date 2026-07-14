# Task API

A small CRUD API for managing a to-do list, built with FastAPI.

## How to run

1. Clone this repo: `git clone https://github.com/YOUR_USERNAME/todo-api.git`
2. Create a virtual environment: `python3 -m venv venv`
3. Activate it: `venv\Scripts\Activate.ps1` (Windows) or `source venv/bin/activate` (Mac/Linux)
4. Install dependencies: `pip install -r requirements.txt`
5. Run the server: `uvicorn main:app --reload`
6. Visit `http://localhost:8000/docs` for interactive Swagger UI

## Endpoints

| Method | Path          | Description              |
|--------|---------------|---------------------------|
| GET    | /             | API info                  |
| GET    | /health       | Health check               |
| GET    | /tasks        | List all tasks             |
| GET    | /tasks/{id}   | Get a single task          |
| POST   | /tasks        | Create a new task          |
| PUT    | /tasks/{id}   | Update a task               |
| DELETE | /tasks/{id}   | Delete a task               |

## Example request

    curl -i http://localhost:8000/tasks/1

    HTTP/1.1 200 OK
    content-type: application/json
    {"id":1,"title":"Buy milk","done":false}

## Swagger UI

![Swagger screenshot](swagger-screenshot.png)

## Notes

- Data is stored in memory only — it resets when the server restarts.
- FastAPI's built-in validation returns `422` for invalid input rather than `400`. This is FastAPI's standard behavior (via Pydantic) and was left as-is rather than manually overridden.