"""
Task API - A professional CRUD API for task management
Built during FlyRank Backend Internship Week 2
Author: Shravani Rajendra Patil
"""

from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from pathlib import Path
import uvicorn

# Initialize FastAPI app
app = FastAPI(
    title="Task Management API",
    description="A production-ready CRUD API for managing tasks. Supports create, read, update, and delete operations with full validation and proper HTTP status codes.",
    version="1.0.0",
    contact={
        "name": "Shravani Patil",
        "url": "https://github.com/shravani22patil",
        "email": "shravanipatil580@gmail.com"
    }
)

# ============================================================================
# DATA MODELS
# ============================================================================

class TaskCreate(BaseModel):
    """Schema for creating a new task"""
    title: str = Field(..., min_length=1, max_length=200, description="Task title (required, 1-200 chars)")
    description: Optional[str] = Field(None, max_length=1000, description="Optional task description")
    
    class Config:
        json_schema_extra = {
            "example": {
                "title": "Buy milk",
                "description": "Get 2 liters of whole milk from the store"
            }
        }


class TaskUpdate(BaseModel):
    """Schema for updating a task"""
    title: Optional[str] = Field(None, min_length=1, max_length=200, description="Updated task title")
    description: Optional[str] = Field(None, max_length=1000, description="Updated task description")
    done: Optional[bool] = Field(None, description="Mark task as completed or pending")
    
    class Config:
        json_schema_extra = {
            "example": {
                "title": "Buy milk & bread",
                "done": True
            }
        }


class Task(BaseModel):
    """Schema for a task response"""
    id: int = Field(..., description="Unique task identifier")
    title: str = Field(..., description="Task title")
    description: Optional[str] = Field(None, description="Task description")
    done: bool = Field(default=False, description="Whether the task is completed")
    created_at: str = Field(..., description="ISO 8601 creation timestamp")
    updated_at: str = Field(..., description="ISO 8601 last update timestamp")
    
    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "title": "Buy milk",
                "description": "Get 2 liters of whole milk",
                "done": False,
                "created_at": "2026-06-15T10:30:00",
                "updated_at": "2026-06-15T10:30:00"
            }
        }


class ErrorResponse(BaseModel):
    """Schema for error responses"""
    error: str = Field(..., description="Error message")
    status_code: int = Field(..., description="HTTP status code")
    
    class Config:
        json_schema_extra = {
            "example": {
                "error": "Task 99 not found",
                "status_code": 404
            }
        }


class StatsResponse(BaseModel):
    """Schema for statistics"""
    total: int = Field(..., description="Total number of tasks")
    completed: int = Field(..., description="Number of completed tasks")
    pending: int = Field(..., description="Number of pending tasks")
    completion_rate: float = Field(..., description="Percentage of completed tasks")


# ============================================================================
# IN-MEMORY DATABASE
# ============================================================================

tasks_db = [
    {
        "id": 1,
        "title": "Learn FastAPI fundamentals",
        "description": "Complete the official FastAPI tutorial",
        "done": False,
        "created_at": "2026-06-15T09:00:00",
        "updated_at": "2026-06-15T09:00:00"
    },
    {
        "id": 2,
        "title": "Build CRUD endpoints",
        "description": "Implement POST, GET, PUT, DELETE with proper status codes",
        "done": True,
        "created_at": "2026-06-15T09:30:00",
        "updated_at": "2026-06-15T11:00:00"
    },
    {
        "id": 3,
        "title": "Add Swagger UI documentation",
        "description": "Make the API interactive and testable in the browser",
        "done": False,
        "created_at": "2026-06-15T10:00:00",
        "updated_at": "2026-06-15T10:00:00"
    }
]

next_task_id = 4  # Next available ID


# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def get_current_timestamp() -> str:
    """Get current timestamp in ISO 8601 format"""
    return datetime.now().isoformat()


def find_task_by_id(task_id: int) -> Optional[dict]:
    """Find a task by ID"""
    return next((task for task in tasks_db if task["id"] == task_id), None)


def task_to_response(task: dict) -> Task:
    """Convert internal task dict to response model"""
    return Task(**task)


# ============================================================================
# ROOT ENDPOINTS
# ============================================================================

@app.get("/", include_in_schema=False)
async def root():
    """Serve the web UI."""
    return FileResponse(Path(__file__).parent / "index.html")
    
async def root():
    """
    Returns metadata about the Task API.
    
    This is your entry point — lists all available endpoints.
    """
    return {
        "name": "Task Management API",
        "version": "1.0.0",
        "description": "A production-ready CRUD API for task management",
        "endpoints": {
            "info": "/",
            "health": "/health",
            "tasks": "/tasks",
            "stats": "/stats",
            "docs": "/docs",
            "openapi": "/openapi.json"
        },
        "author": "Shravani Rajendra Patil",
        "built_for": "FlyRank Backend Internship Week 2"
    }


@app.get(
    "/health",
    tags=["Info"],
    summary="Health Check",
    description="Verify the API is running and healthy"
)
async def health():
    """
    Health check endpoint.
    
    Used by monitoring systems to verify the server is alive.
    Returns 200 if healthy.
    """
    return {
        "status": "ok",
        "timestamp": get_current_timestamp(),
        "tasks_in_memory": len(tasks_db)
    }


# ============================================================================
# READ ENDPOINTS (GET)
# ============================================================================

@app.get(
    "/tasks",
    response_model=List[Task],
    tags=["Tasks"],
    summary="List All Tasks",
    description="Retrieve all tasks with optional filtering"
)
async def list_tasks(
    done: Optional[bool] = Query(None, description="Filter by completion status (true/false)"),
    search: Optional[str] = Query(None, description="Search tasks by title (case-insensitive)"),
    limit: int = Query(100, ge=1, le=1000, description="Maximum number of tasks to return"),
    offset: int = Query(0, ge=0, description="Number of tasks to skip")
):
    """
    Get all tasks with optional filtering and pagination.
    
    **Query Parameters:**
    - `done`: Filter by completion status (true for completed, false for pending)
    - `search`: Search in task titles (case-insensitive substring match)
    - `limit`: Maximum tasks to return (default: 100, max: 1000)
    - `offset`: Skip first N tasks (for pagination)
    
    **Examples:**
    - `GET /tasks` — Get all tasks
    - `GET /tasks?done=true` — Get only completed tasks
    - `GET /tasks?search=milk` — Get tasks with "milk" in title
    - `GET /tasks?limit=10&offset=20` — Get tasks 20-30 (pagination)
    """
    # Start with all tasks
    filtered = tasks_db
    
    # Filter by done status
    if done is not None:
        filtered = [t for t in filtered if t["done"] == done]
    
    # Filter by search term
    if search:
        search_lower = search.lower()
        filtered = [t for t in filtered if search_lower in t["title"].lower()]
    
    # Apply pagination
    paginated = filtered[offset:offset + limit]
    
    # Convert to response models
    return [Task(**task) for task in paginated]


@app.get(
    "/tasks/{task_id}",
    response_model=Task,
    tags=["Tasks"],
    summary="Get Single Task",
    description="Retrieve a specific task by ID",
    responses={
        200: {"description": "Task found"},
        404: {"model": ErrorResponse, "description": "Task not found"}
    }
)
async def get_task(task_id: int):
    """
    Get a single task by ID.
    
    **Path Parameters:**
    - `task_id`: The unique identifier of the task
    
    **Status Codes:**
    - `200`: Task found and returned
    - `404`: Task with given ID does not exist
    
    **Example:**
    - `GET /tasks/1` — Get task with ID 1
    """
    task = find_task_by_id(task_id)
    if not task:
        raise HTTPException(
            status_code=404,
            detail={"error": f"Task {task_id} not found", "status_code": 404}
        )
    return Task(**task)


@app.get(
    "/stats",
    response_model=StatsResponse,
    tags=["Info"],
    summary="Task Statistics",
    description="Get aggregated statistics about all tasks"
)
async def get_stats():
    """
    Get statistics about tasks.
    
    Returns total count, completion count, and completion rate.
    """
    total = len(tasks_db)
    completed = len([t for t in tasks_db if t["done"]])
    pending = total - completed
    completion_rate = (completed / total * 100) if total > 0 else 0
    
    return StatsResponse(
        total=total,
        completed=completed,
        pending=pending,
        completion_rate=round(completion_rate, 2)
    )


# ============================================================================
# CREATE ENDPOINT (POST)
# ============================================================================

@app.post(
    "/tasks",
    response_model=Task,
    status_code=201,
    tags=["Tasks"],
    summary="Create New Task",
    description="Add a new task to the list",
    responses={
        201: {"description": "Task created successfully"},
        400: {"model": ErrorResponse, "description": "Invalid input"}
    }
)
async def create_task(task_data: TaskCreate):
    """
    Create a new task.
    
    **Request Body:**
    - `title` (required): Task title, 1-200 characters
    - `description` (optional): Longer description, up to 1000 characters
    
    **Status Codes:**
    - `201`: Task created successfully (includes new task ID)
    - `400`: Missing or invalid title
    
    **Response:**
    Returns the newly created task with ID, timestamps, and done=false by default.
    
    **Example:**
    ```
    POST /tasks
    {
        "title": "Buy milk",
        "description": "Get 2 liters of whole milk"
    }
    
    Response (201):
    {
        "id": 4,
        "title": "Buy milk",
        "description": "Get 2 liters of whole milk",
        "done": false,
        "created_at": "2026-06-15T12:00:00",
        "updated_at": "2026-06-15T12:00:00"
    }
    ```
    """
    global next_task_id
    
    # Pydantic validation already checked min_length, but double-check
    if not task_data.title or not task_data.title.strip():
        raise HTTPException(
            status_code=400,
            detail={"error": "Title cannot be empty", "status_code": 400}
        )
    
    # Create new task
    now = get_current_timestamp()
    new_task = {
        "id": next_task_id,
        "title": task_data.title.strip(),
        "description": task_data.description,
        "done": False,
        "created_at": now,
        "updated_at": now
    }
    
    tasks_db.append(new_task)
    next_task_id += 1
    
    return Task(**new_task)


# ============================================================================
# UPDATE ENDPOINT (PUT)
# ============================================================================

@app.put(
    "/tasks/{task_id}",
    response_model=Task,
    tags=["Tasks"],
    summary="Update Task",
    description="Update an existing task",
    responses={
        200: {"description": "Task updated successfully"},
        400: {"model": ErrorResponse, "description": "Invalid input"},
        404: {"model": ErrorResponse, "description": "Task not found"}
    }
)
async def update_task(task_id: int, task_data: TaskUpdate):
    """
    Update an existing task.
    
    **Path Parameters:**
    - `task_id`: The ID of the task to update
    
    **Request Body** (all fields optional):
    - `title`: New task title
    - `description`: New description
    - `done`: Mark as completed (true) or pending (false)
    
    **Status Codes:**
    - `200`: Task updated successfully
    - `400`: Invalid input (empty title)
    - `404`: Task not found
    
    **Note:**
    - At least one field must be provided
    - Empty titles are not allowed
    - Only provided fields are updated; others remain unchanged
    
    **Example:**
    ```
    PUT /tasks/1
    {
        "title": "Buy milk & bread",
        "done": true
    }
    ```
    """
    task = find_task_by_id(task_id)
    if not task:
        raise HTTPException(
            status_code=404,
            detail={"error": f"Task {task_id} not found", "status_code": 404}
        )
    
    # Validate title if provided
    if task_data.title is not None:
        if not task_data.title.strip():
            raise HTTPException(
                status_code=400,
                detail={"error": "Title cannot be empty", "status_code": 400}
            )
        task["title"] = task_data.title.strip()
    
    # Update other fields if provided
    if task_data.description is not None:
        task["description"] = task_data.description
    
    if task_data.done is not None:
        task["done"] = task_data.done
    
    # Update timestamp
    task["updated_at"] = get_current_timestamp()
    
    return Task(**task)


# ============================================================================
# DELETE ENDPOINT
# ============================================================================

@app.delete(
    "/tasks/{task_id}",
    status_code=204,
    tags=["Tasks"],
    summary="Delete Task",
    description="Remove a task permanently",
    responses={
        204: {"description": "Task deleted successfully"},
        404: {"model": ErrorResponse, "description": "Task not found"}
    }
)
async def delete_task(task_id: int):
    """
    Delete a task permanently.
    
    **Path Parameters:**
    - `task_id`: The ID of the task to delete
    
    **Status Codes:**
    - `204`: Task deleted (No Content — success with empty body)
    - `404`: Task not found
    
    **Note:**
    Returns 204 with an empty body (nothing to say, operation successful).
    
    **Example:**
    `DELETE /tasks/1` → Status 204 (no response body)
    """
    global tasks_db
    task = find_task_by_id(task_id)
    if not task:
        raise HTTPException(
            status_code=404,
            detail={"error": f"Task {task_id} not found", "status_code": 404}
        )
    
    # Remove task from list
    tasks_db = [t for t in tasks_db if t["id"] != task_id]
    
    # Return 204 No Content
    return None


# ============================================================================
# BONUS: RESET ENDPOINT (for testing)
# ============================================================================

@app.post(
    "/reset",
    tags=["Admin"],
    summary="Reset to Demo Data",
    description="Restore original 3 demo tasks (for testing/demos)"
)
async def reset_tasks():
    """
    Reset tasks to original demo state.
    
    Useful for testing and demonstrations.
    Restores the 3 example tasks and resets the task ID counter.
    """
    global tasks_db, next_task_id
    
    tasks_db = [
        {
            "id": 1,
            "title": "Learn FastAPI fundamentals",
            "description": "Complete the official FastAPI tutorial",
            "done": False,
            "created_at": "2026-06-15T09:00:00",
            "updated_at": "2026-06-15T09:00:00"
        },
        {
            "id": 2,
            "title": "Build CRUD endpoints",
            "description": "Implement POST, GET, PUT, DELETE with proper status codes",
            "done": True,
            "created_at": "2026-06-15T09:30:00",
            "updated_at": "2026-06-15T11:00:00"
        },
        {
            "id": 3,
            "title": "Add Swagger UI documentation",
            "description": "Make the API interactive and testable in the browser",
            "done": False,
            "created_at": "2026-06-15T10:00:00",
            "updated_at": "2026-06-15T10:00:00"
        }
    ]
    next_task_id = 4
    
    return {
        "message": "Tasks reset to demo state",
        "tasks_count": len(tasks_db),
        "timestamp": get_current_timestamp()
    }


# ============================================================================
# RUN THE SERVER
# ============================================================================

if __name__ == "__main__":
    print("🚀 Starting Task API Server...")
    print("📖 Swagger UI: http://localhost:8000/docs")
    print("🔗 ReDoc: http://localhost:8000/redoc")
    print("🏠 API Root: http://localhost:8000/")
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
