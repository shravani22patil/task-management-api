"""
Task API - PostgreSQL Database Version (Containerized)
A production-ready CRUD API running against Postgres in Docker
Built during FlyRank Backend Internship Week 3
Author: Shravani Rajendra Patil
"""

from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

def get_current_timestamp() -> str:
    """Get current timestamp in ISO 8601 format"""
    return datetime.now().isoformat()

import psycopg
from psycopg import sql
import os
import uvicorn

# Initialize FastAPI app
app = FastAPI(
    title="Task Management API (PostgreSQL)",
    description="A production-ready CRUD API with containerized PostgreSQL database. Runs with docker-compose.",
    version="3.0.0",
    contact={
        "name": "Shravani Patil",
        "url": "https://github.com/shravani22patil",
        "email": "shravanipatil580@gmail.com"
    }
)

# ============================================================================
# DATABASE CONFIGURATION
# ============================================================================

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/tasks")

def get_db():
    """Get database connection to PostgreSQL"""
    try:
        conn = psycopg.connect(DATABASE_URL)
        return conn
    except psycopg.OperationalError as e:
        print(f"❌ Database connection error: {e}")
        raise

def init_db():
    """Initialize database with table and seed data"""
    conn = None
    try:
        conn = get_db()
        cursor = conn.cursor()
        
        # Create tasks table if it doesn't exist
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id SERIAL PRIMARY KEY,
                title TEXT NOT NULL,
                description TEXT,
                done BOOLEAN DEFAULT false,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL
            )
        """)
        
        # Seed data only if table is empty
        cursor.execute("SELECT COUNT(*) FROM tasks")
        count = cursor.fetchone()[0]
        
        if count == 0:
            now = get_current_timestamp()
            seed_tasks = [
                ("Learn FastAPI fundamentals", "Complete the official FastAPI tutorial", False),
                ("Build CRUD endpoints", "Implement POST, GET, PUT, DELETE with proper status codes", True),
                ("Add Swagger UI documentation", "Make the API interactive and testable in the browser", False)
            ]
            
            for title, description, done in seed_tasks:
                cursor.execute("""
                    INSERT INTO tasks (title, description, done, created_at, updated_at)
                    VALUES (%s, %s, %s, %s, %s)
                """, (title, description, done, now, now))
            
            conn.commit()
            print(f"✅ PostgreSQL initialized with 3 seed tasks")
        else:
            print(f"✅ PostgreSQL loaded with {count} existing tasks")
    
    except Exception as e:
        print(f"⚠️  Database initialization: {e}")
        if conn:
            conn.rollback()
    
    finally:
        if conn:
            conn.close()

# Initialize database on startup
print("🗄️  Connecting to PostgreSQL...")
init_db()

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
# DATABASE OPERATIONS
# ============================================================================

def row_to_dict(row) -> Optional[dict]:
    """Convert PostgreSQL row tuple to dictionary"""
    if row is None:
        return None
    return {
        "id": row[0],
        "title": row[1],
        "description": row[2],
        "done": bool(row[3]),
        "created_at": row[4],
        "updated_at": row[5]
    }

def get_all_tasks(done: Optional[bool] = None, search: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[dict]:
    """Get all tasks from PostgreSQL with optional filtering"""
    conn = get_db()
    cursor = conn.cursor()
    
    try:
        query = "SELECT id, title, description, done, created_at, updated_at FROM tasks WHERE 1=1"
        params = []
        
        if done is not None:
            query += " AND done = %s"
            params.append(done)
        
        if search:
            query += " AND title ILIKE %s"
            params.append(f"%{search}%")
        
        query += " LIMIT %s OFFSET %s"
        params.extend([limit, offset])
        
        cursor.execute(query, params)
        rows = cursor.fetchall()
        return [row_to_dict(row) for row in rows]
    
    finally:
        conn.close()

def get_task_by_id(task_id: int) -> Optional[dict]:
    """Get single task by ID from PostgreSQL"""
    conn = get_db()
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT id, title, description, done, created_at, updated_at FROM tasks WHERE id = %s", (task_id,))
        row = cursor.fetchone()
        return row_to_dict(row)
    
    finally:
        conn.close()

def create_task(title: str, description: Optional[str]) -> dict:
    """Insert new task into PostgreSQL"""
    conn = get_db()
    cursor = conn.cursor()
    
    try:
        now = get_current_timestamp()
        cursor.execute("""
            INSERT INTO tasks (title, description, done, created_at, updated_at)
            VALUES (%s, %s, false, %s, %s)
            RETURNING id, title, description, done, created_at, updated_at
        """, (title, description, now, now))
        
        conn.commit()
        row = cursor.fetchone()
        return row_to_dict(row)
    
    finally:
        conn.close()

def update_task(task_id: int, title: Optional[str], description: Optional[str], done: Optional[bool]) -> Optional[dict]:
    """Update task in PostgreSQL"""
    conn = get_db()
    cursor = conn.cursor()
    
    try:
        # Check if task exists
        cursor.execute("SELECT id FROM tasks WHERE id = %s", (task_id,))
        if cursor.fetchone() is None:
            return None
        
        # Build dynamic update query
        updates = []
        params = []
        
        if title is not None:
            updates.append("title = %s")
            params.append(title)
        
        if description is not None:
            updates.append("description = %s")
            params.append(description)
        
        if done is not None:
            updates.append("done = %s")
            params.append(done)
        
        # Always update timestamp
        updates.append("updated_at = %s")
        params.append(get_current_timestamp())
        
        # Execute update and return result
        params.append(task_id)
        query = f"UPDATE tasks SET {', '.join(updates)} WHERE id = %s RETURNING id, title, description, done, created_at, updated_at"
        cursor.execute(query, params)
        conn.commit()
        
        row = cursor.fetchone()
        return row_to_dict(row)
    
    finally:
        conn.close()

def delete_task(task_id: int) -> bool:
    """Delete task from PostgreSQL. Returns True if deleted, False if not found"""
    conn = get_db()
    cursor = conn.cursor()
    
    try:
        # Check if task exists
        cursor.execute("SELECT id FROM tasks WHERE id = %s", (task_id,))
        if cursor.fetchone() is None:
            return False
        
        # Delete task
        cursor.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
        conn.commit()
        return True
    
    finally:
        conn.close()

def get_stats() -> dict:
    """Get task statistics from PostgreSQL"""
    conn = get_db()
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT COUNT(*) as total FROM tasks")
        total = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) as completed FROM tasks WHERE done = true")
        completed = cursor.fetchone()[0]
        
        pending = total - completed
        completion_rate = (completed / total * 100) if total > 0 else 0
        
        return {
            "total": total,
            "completed": completed,
            "pending": pending,
            "completion_rate": round(completion_rate, 2)
        }
    
    finally:
        conn.close()



# ============================================================================
# ROOT ENDPOINTS
# ============================================================================

@app.get(
    "/",
    tags=["Info"],
    summary="API Overview",
    description="Get basic information about this Task API"
)
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
    description="Verify the API and PostgreSQL database are running and healthy"
)
async def health_check():
    """
    Health check endpoint.
    
    Verifies API is running and Postgres is accessible.
    Returns 200 if healthy with task count from database.
    """
    try:
        stats = get_stats()
        return {
            "status": "ok",
            "timestamp": get_current_timestamp(),
            "database": "PostgreSQL",
            "database_url": DATABASE_URL.split("@")[1] if "@" in DATABASE_URL else "localhost",
            "tasks_in_database": stats["total"]
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={"error": f"Database error: {str(e)}", "status_code": 500}
        )


# ============================================================================
# READ ENDPOINTS (GET)
# ============================================================================

@app.get(
    "/tasks",
    response_model=List[Task],
    tags=["Tasks"],
    summary="List All Tasks",
    description="Retrieve all tasks from database with optional filtering"
)
async def list_tasks(
    done: Optional[bool] = Query(None, description="Filter by completion status (true/false)"),
    search: Optional[str] = Query(None, description="Search tasks by title (case-insensitive)"),
    limit: int = Query(100, ge=1, le=1000, description="Maximum number of tasks to return"),
    offset: int = Query(0, ge=0, description="Number of tasks to skip")
):
    """
    Get all tasks from database with optional filtering and pagination.
    
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
    
    **Database:** Queries are executed with parameterized SQL for safety.
    """
    tasks = get_all_tasks(done=done, search=search, limit=limit, offset=offset)
    return [Task(**task) for task in tasks]


@app.get(
    "/tasks/{task_id}",
    response_model=Task,
    tags=["Tasks"],
    summary="Get Single Task",
    description="Retrieve a specific task by ID from database",
    responses={
        200: {"description": "Task found"},
        404: {"model": ErrorResponse, "description": "Task not found"}
    }
)
async def get_task(task_id: int):
    """
    Get a single task by ID from the database.
    
    **Path Parameters:**
    - `task_id`: The unique identifier of the task
    
    **Status Codes:**
    - `200`: Task found and returned
    - `404`: Task with given ID does not exist
    
    **Example:**
    - `GET /tasks/1` — Get task with ID 1
    
    **Database:** Uses parameterized query: SELECT * FROM tasks WHERE id = ?
    """
    task = get_task_by_id(task_id)
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
    description="Get aggregated statistics about all tasks from database"
)
async def get_task_stats():
    """
    Get statistics about tasks from database.
    
    Returns total count, completion count, and completion rate.
    
    **Database:** Uses COUNT(*) queries:
    - SELECT COUNT(*) FROM tasks
    - SELECT COUNT(*) FROM tasks WHERE done = 1
    """
    stats = get_stats()
    return StatsResponse(**stats)


# ============================================================================
# CREATE ENDPOINT (POST)
# ============================================================================

@app.post(
    "/tasks",
    response_model=Task,
    status_code=201,
    tags=["Tasks"],
    summary="Create New Task",
    description="Insert a new task into the database",
    responses={
        201: {"description": "Task created successfully"},
        400: {"model": ErrorResponse, "description": "Invalid input"}
    }
)
async def create_new_task(task_data: TaskCreate):
    """
    Create a new task and insert into database.
    
    **Request Body:**
    - `title` (required): Task title, 1-200 characters
    - `description` (optional): Longer description, up to 1000 characters
    
    **Status Codes:**
    - `201`: Task created successfully (includes new task ID from database)
    - `400`: Missing or invalid title
    
    **Response:**
    Returns the newly created task with database-assigned ID and timestamps.
    
    **Database:** Uses parameterized INSERT:
    INSERT INTO tasks (title, description, done, created_at, updated_at) VALUES (?, ?, 0, ?, ?)
    
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
    # Validate title
    if not task_data.title or not task_data.title.strip():
        raise HTTPException(
            status_code=400,
            detail={"error": "Title cannot be empty", "status_code": 400}
        )
    
    # Insert into database and get the created task
    new_task = create_task(task_data.title.strip(), task_data.description)
    
    return Task(**new_task)


# ============================================================================
# UPDATE ENDPOINT (PUT)
# ============================================================================

@app.put(
    "/tasks/{task_id}",
    response_model=Task,
    tags=["Tasks"],
    summary="Update Task",
    description="Update an existing task in the database",
    responses={
        200: {"description": "Task updated successfully"},
        400: {"model": ErrorResponse, "description": "Invalid input"},
        404: {"model": ErrorResponse, "description": "Task not found"}
    }
)
async def update_existing_task(task_id: int, task_data: TaskUpdate):
    """
    Update an existing task in the database.
    
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
    - updated_at timestamp is automatically set to current time
    
    **Database:** Uses parameterized UPDATE with dynamic WHERE clause
    
    **Example:**
    ```
    PUT /tasks/1
    {
        "title": "Buy milk & bread",
        "done": true
    }
    ```
    """
    # Validate title if provided
    if task_data.title is not None:
        if not task_data.title.strip():
            raise HTTPException(
                status_code=400,
                detail={"error": "Title cannot be empty", "status_code": 400}
            )
    
    # Update in database
    updated_task = update_task(
        task_id,
        task_data.title.strip() if task_data.title else None,
        task_data.description,
        task_data.done
    )
    
    if not updated_task:
        raise HTTPException(
            status_code=404,
            detail={"error": f"Task {task_id} not found", "status_code": 404}
        )
    
    return Task(**updated_task)


# ============================================================================
# DELETE ENDPOINT
# ============================================================================

@app.delete(
    "/tasks/{task_id}",
    status_code=204,
    tags=["Tasks"],
    summary="Delete Task",
    description="Remove a task permanently from database",
    responses={
        204: {"description": "Task deleted successfully"},
        404: {"model": ErrorResponse, "description": "Task not found"}
    }
)
async def delete_existing_task(task_id: int):
    """
    Delete a task permanently from the database.
    
    **Path Parameters:**
    - `task_id`: The ID of the task to delete
    
    **Status Codes:**
    - `204`: Task deleted (No Content — success with empty body)
    - `404`: Task not found
    
    **Note:**
    Returns 204 with an empty body (nothing to say, operation successful).
    Data is permanently removed from tasks.db
    
    **Database:** Uses parameterized DELETE: DELETE FROM tasks WHERE id = ?
    
    **Example:**
    `DELETE /tasks/1` → Status 204 (no response body)
    """
    if not delete_task(task_id):
        raise HTTPException(
            status_code=404,
            detail={"error": f"Task {task_id} not found", "status_code": 404}
        )
    
    # Return 204 No Content
    return None


# ============================================================================
# BONUS: RESET ENDPOINT (for testing)
# ============================================================================

@app.post(
    "/reset",
    tags=["Admin"],
    summary="Reset to Demo Data",
    description="Clear database and restore original 3 demo tasks (for testing/demos)"
)
async def reset_tasks():
    """
    Reset tasks to original demo state.
    
    Clears the tasks table and reinserts the 3 example tasks.
    Useful for testing and demonstrations.
    """
    conn = get_db()
    cursor = conn.cursor()
    
    try:
        # Delete all tasks
        cursor.execute("DELETE FROM tasks")
        
        # Reset sequence (for PostgreSQL auto-increment)
        cursor.execute("ALTER SEQUENCE tasks_id_seq RESTART WITH 1")
        
        # Reinsert demo tasks
        now = get_current_timestamp()
        demo_tasks = [
            ("Learn FastAPI fundamentals", "Complete the official FastAPI tutorial", False),
            ("Build CRUD endpoints", "Implement POST, GET, PUT, DELETE with proper status codes", True),
            ("Add Swagger UI documentation", "Make the API interactive and testable in the browser", False)
        ]
        
        for title, description, done in demo_tasks:
            cursor.execute("""
                INSERT INTO tasks (title, description, done, created_at, updated_at)
                VALUES (%s, %s, %s, %s, %s)
            """, (title, description, done, now, now))
        
        conn.commit()
        
        stats = get_stats()
        return {
            "message": "Tasks reset to demo state",
            "tasks_count": stats["total"],
            "timestamp": get_current_timestamp()
        }
    
    finally:
        conn.close()


# ============================================================================
# RUN THE SERVER
# ============================================================================

if __name__ == "__main__":
    print("🚀 Starting Task API Server (PostgreSQL Edition)...")
    print(f"🗄️  Database: {DATABASE_URL.split('@')[1] if '@' in DATABASE_URL else DATABASE_URL}")
    print("📖 Swagger UI: http://localhost:8000/docs")
    print("🔗 ReDoc: http://localhost:8000/redoc")
    print("🏠 API Root: http://localhost:8000/")
    print("\n✨ Running against containerized PostgreSQL database!")
    print("🐳 Started with: docker-compose up\n")
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        reload=False,
        log_level="info"
    )
