# Task Management API 📋 (SQLite Edition)

**Week 3 Assignment: Connecting CRUD to Database**

A production-ready **CRUD API** for task management built with **FastAPI** and **SQLite**. All data is now persistent and survives server restarts.

**Built for:** FlyRank Backend Internship - Week 2 → Week 3

---

## 🌟 What's New in Week 3?

✨ **Data Persistence** — Tasks now live in a SQLite database (tasks.db)  
✨ **Survive Restarts** — Create a task, restart the server, task is still there  
✨ **Same API** — All endpoints work identically; clients don't notice the change  
✨ **File-Based** — No database server needed; just a single tasks.db file  

---

## 📊 Architecture Change

### Week 2 (In-Memory):
```
Client → FastAPI → Python List (in memory)
                   ↑ Lost on restart
```

### Week 3 (SQLite):
```
Client → FastAPI → SQLite Database (tasks.db on disk)
                   ↑ Survives restart
```

**The API endpoints are identical.** Only storage changed.

---

## 🎯 Features

✅ **Complete CRUD Operations** — Create, Read, Update, Delete  
✅ **SQLite Database** — Persistent storage in tasks.db file  
✅ **Automatic Setup** — Database and table created on first run  
✅ **Demo Data** — 3 example tasks seeded only once  
✅ **Full REST API** — Proper HTTP methods and status codes  
✅ **Input Validation** — Pydantic models validate all data  
✅ **Parameterized Queries** — Safe SQL with ? placeholders (no SQL injection)  
✅ **Error Handling** — Comprehensive error responses  
✅ **Interactive Swagger UI** — Test endpoints in the browser  
✅ **Modern Web Interface** — Beautiful task management dashboard  

---

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the Server
```bash
python main.py
```

You'll see:
```
🚀 Starting Task API Server (SQLite Edition)...
🗄️  Database: tasks.db
📖 Swagger UI: http://localhost:8000/docs
🔗 ReDoc: http://localhost:8000/redoc

✨ All data now persists in SQLite database!
🔄 Restart the server and tasks will still be there.
```

### 3. Access the Application

- **Web Interface:** Open `index.html` in your browser
- **Swagger UI (Interactive Docs):** http://localhost:8000/docs ⭐ **Use this to test**
- **ReDoc (Beautiful Docs):** http://localhost:8000/redoc
- **Database File:** `tasks.db` (created automatically)

---

## 📁 Database Information

### What is SQLite?

**SQLite** is a lightweight, file-based database with these advantages:

✅ **Zero Setup** — No server to install or run  
✅ **Single File** — Entire database is just `tasks.db`  
✅ **Portable** — Copy the file and your database goes with it  
✅ **Production-Ready** — Used by millions (Chrome, Firefox, iOS, Android)  
✅ **ACID Compliant** — Reliable transactions and data integrity  

### Why SQLite for This Project?

- **No configuration** — Database creates itself
- **Single file** — Easy to backup, deploy, share
- **Perfect for prototypes and small apps** — What you're building here
- **Scales reasonably** — Millions of rows, no problem
- **Zero dependencies** — Built into Python (import sqlite3)

### Database Location

```
task-api/
├── main.py
├── index.html
├── requirements.txt
├── README.md
└── tasks.db           ← Your database file (created automatically)
```

**Important:** `tasks.db` is in `.gitignore` so each clone starts fresh. This is intentional.

---

## 📊 Database Schema

### tasks table

| Column | Type | Notes |
|--------|------|-------|
| **id** | INTEGER | Primary key (auto-incrementing, assigned by SQLite) |
| **title** | TEXT | Task title (required) |
| **description** | TEXT | Optional task description |
| **done** | BOOLEAN | 0 = pending, 1 = completed |
| **created_at** | TEXT | ISO 8601 timestamp |
| **updated_at** | TEXT | ISO 8601 timestamp |

---

## 📖 API Endpoints

### All endpoints work identically to Week 2. Same requests, same responses.

#### **1. List All Tasks** ✅
```http
GET /tasks
```

**Optional Query Parameters:**
- `done=true` — Only completed tasks
- `done=false` — Only pending tasks
- `search=milk` — Search in titles
- `limit=10&offset=20` — Pagination

**Example:**
```bash
curl http://localhost:8000/tasks
curl "http://localhost:8000/tasks?done=true"
curl "http://localhost:8000/tasks?search=buy"
```

**Response (200 OK):**
```json
[
  {
    "id": 1,
    "title": "Learn FastAPI fundamentals",
    "description": "Complete the official FastAPI tutorial",
    "done": false,
    "created_at": "2026-06-15T09:00:00",
    "updated_at": "2026-06-15T09:00:00"
  }
]
```

---

#### **2. Get Single Task** ✅
```http
GET /tasks/{task_id}
```

**Example:**
```bash
curl http://localhost:8000/tasks/1
```

**Response (200 OK):**
```json
{
  "id": 1,
  "title": "Learn FastAPI fundamentals",
  "description": "Complete the official FastAPI tutorial",
  "done": false,
  "created_at": "2026-06-15T09:00:00",
  "updated_at": "2026-06-15T09:00:00"
}
```

**Response (404 Not Found):**
```json
{"error": "Task 999 not found", "status_code": 404}
```

---

#### **3. Create Task** ✅
```http
POST /tasks
Content-Type: application/json

{
  "title": "Buy milk",
  "description": "2 liters of whole milk"
}
```

**Example:**
```bash
curl -X POST http://localhost:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"Buy milk","description":"2 liters"}'
```

**Response (201 Created):**
```json
{
  "id": 4,
  "title": "Buy milk",
  "description": "2 liters of whole milk",
  "done": false,
  "created_at": "2026-06-15T12:00:00",
  "updated_at": "2026-06-15T12:00:00"
}
```

---

#### **4. Update Task** ✅
```http
PUT /tasks/{task_id}
Content-Type: application/json

{
  "title": "Updated title",
  "done": true
}
```

**Example:**
```bash
curl -X PUT http://localhost:8000/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"done":true}'
```

**Response (200 OK):**
```json
{
  "id": 1,
  "title": "Learn FastAPI fundamentals",
  "description": "Complete the official FastAPI tutorial",
  "done": true,
  "created_at": "2026-06-15T09:00:00",
  "updated_at": "2026-06-15T15:30:00"
}
```

---

#### **5. Delete Task** ✅
```http
DELETE /tasks/{task_id}
```

**Example:**
```bash
curl -X DELETE http://localhost:8000/tasks/1
```

**Response (204 No Content):**
```
(empty body)
```

---

#### **6. Get Statistics** 📊
```http
GET /stats
```

**Example:**
```bash
curl http://localhost:8000/stats
```

**Response (200 OK):**
```json
{
  "total": 10,
  "completed": 3,
  "pending": 7,
  "completion_rate": 30.0
}
```

---

#### **7. Health Check** 🏥
```http
GET /health
```

**Response (200 OK):**
```json
{
  "status": "ok",
  "timestamp": "2026-06-15T12:00:00",
  "database": "SQLite",
  "database_file": "tasks.db",
  "tasks_in_database": 10
}
```

---

## 🧪 Testing with cURL

```bash
# Get all tasks
curl http://localhost:8000/tasks

# Create a new task
curl -X POST http://localhost:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"Buy groceries","description":"Milk, bread, eggs"}'

# Get specific task
curl http://localhost:8000/tasks/1

# Update task (mark as done)
curl -X PUT http://localhost:8000/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"done":true}'

# Delete task
curl -X DELETE http://localhost:8000/tasks/1

# Get statistics
curl http://localhost:8000/stats

# Health check
curl http://localhost:8000/health

# Search tasks
curl "http://localhost:8000/tasks?search=milk"

# Filter completed tasks
curl "http://localhost:8000/tasks?done=true"
```

---

## 🗄️ SQL Queries Used

Here are the SQL queries executed by the API:

### Create Table
```sql
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    done BOOLEAN DEFAULT 0,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL
)
```

### Read All Tasks
```sql
SELECT * FROM tasks
```

### Read Single Task
```sql
SELECT * FROM tasks WHERE id = ?
```

### Search Tasks
```sql
SELECT * FROM tasks WHERE title LIKE ?
```

### Filter Completed Tasks
```sql
SELECT * FROM tasks WHERE done = 1
```

### Create Task
```sql
INSERT INTO tasks (title, description, done, created_at, updated_at)
VALUES (?, ?, 0, ?, ?)
```

### Update Task
```sql
UPDATE tasks SET title = ?, done = ?, updated_at = ? WHERE id = ?
```

### Delete Task
```sql
DELETE FROM tasks WHERE id = ?
```

### Get Statistics
```sql
SELECT COUNT(*) FROM tasks                    -- Total
SELECT COUNT(*) FROM tasks WHERE done = 1    -- Completed
```

**Note:** All queries use `?` parameterized placeholders for safety (prevents SQL injection).

---

## 🛠️ Viewing the Database with DB Browser

### Download DB Browser for SQLite
- **Free tool:** https://sqlitebrowser.org/
- **Platforms:** Windows, Mac, Linux

### Steps to View Your Database

1. **Start the server:** `python main.py`
2. **Open DB Browser for SQLite**
3. **File → Open Database → Select `tasks.db`**
4. **Browse your data:**
   - Click "Browse Data" tab
   - Select "tasks" table
   - See all your data in a spreadsheet view

### Run SQL Queries by Hand

In DB Browser, click the "Execute SQL" tab:

```sql
-- See all tasks
SELECT * FROM tasks;

-- Only completed tasks
SELECT * FROM tasks WHERE done = 1;

-- Count tasks
SELECT COUNT(*) FROM tasks;

-- Find tasks with "buy" in title
SELECT * FROM tasks WHERE title LIKE '%buy%';

-- Mark all tasks as done
UPDATE tasks SET done = 1;

-- Delete all completed tasks
DELETE FROM tasks WHERE done = 1;
```

**Important:** Any change you make in DB Browser is immediately visible through the API (same file, one source of truth).

---

## 📸 Database Screenshot

*(When you run this project, you should see tasks.db in your folder)*

```
task-api/
├── main.py
├── index.html
├── requirements.txt
├── README.md
├── .gitignore
└── tasks.db  ← This file appears after first run
```

Open it in DB Browser to see:

| id | title | description | done | created_at | updated_at |
|---|---|---|---|---|---|
| 1 | Learn FastAPI fundamentals | Complete the official... | 0 | 2026-06-15T09:00:00 | 2026-06-15T09:00:00 |
| 2 | Build CRUD endpoints | Implement POST, GET... | 1 | 2026-06-15T09:30:00 | 2026-06-15T11:00:00 |
| 3 | Add Swagger UI doc... | Make the API interactive... | 0 | 2026-06-15T10:00:00 | 2026-06-15T10:00:00 |

---

## 🎓 Learning: Persistence Explained

### Week 2 (In-Memory)
```python
tasks_db = [...]  # List in Python memory
```
- Fast
- Disappears on restart ❌
- Only one user at a time

### Week 3 (SQLite)
```python
conn = sqlite3.connect("tasks.db")  # File on disk
cursor.execute("SELECT * FROM tasks")
```
- Still fast (microseconds for small data)
- Survives restarts ✅
- Can handle multiple users
- Professional applications work this way

**This is the difference between a toy and something real.**

---

## 📝 Code Quality

✅ **Type Hints** — Every function annotated  
✅ **Docstrings** — Every endpoint documented  
✅ **Parameterized Queries** — All SQL uses ? placeholders (safe)  
✅ **Error Handling** — Proper status codes (200, 201, 204, 400, 404)  
✅ **Validation** — Pydantic models validate all input  
✅ **Clean Code** — Organized in logical sections  

---

## 🚀 Deployment

### To deploy on a server:

```bash
pip install -r requirements.txt
python main.py
```

Or with a production server:

```bash
pip install gunicorn
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app
```

The `tasks.db` file travels with your deployment.

---

## 📂 Project Structure

```
task-api/
├── main.py                      # FastAPI app + SQLite operations
├── index.html                   # Web interface (unchanged from Week 2)
├── requirements.txt             # Python dependencies
├── README.md                    # This file
├── SETUP_GUIDE.md              # Step-by-step instructions
├── SUBMISSION_CHECKLIST.md     # Pre-submission guide
├── .gitignore                  # Ignore tasks.db on git
└── tasks.db                    # SQLite database (created on first run)
```

---

## 🎯 Why This Matters

**The same API works with:**
- In-memory list (Week 2)
- SQLite database (Week 3)
- PostgreSQL database (Week 4)
- MongoDB (Week 5)

The endpoints never change. Only storage changes. This separation of concerns is professional software engineering.

---

## ✅ Proof of Persistence

1. **Create a task:**
   ```bash
   curl -X POST http://localhost:8000/tasks \
     -H "Content-Type: application/json" \
     -d '{"title":"Test task"}'
   ```

2. **Verify it's in the database:**
   ```bash
   curl http://localhost:8000/tasks
   ```

3. **Stop the server:** Press Ctrl+C

4. **Start it again:** `python main.py`

5. **Verify the task is STILL THERE:**
   ```bash
   curl http://localhost:8000/tasks
   ```

**That task survived the restart.** That's persistence. That's real.

---

## 🐛 Troubleshooting

**Problem: "tasks.db not found"**  
→ Database is created automatically on first run. If missing, just delete and restart.

**Problem: "ModuleNotFoundError: No module named 'sqlite3'"**  
→ sqlite3 is built-in to Python. This shouldn't happen. Check your Python installation.

**Problem: "Database is locked"**  
→ Two processes trying to access tasks.db at once. Stop the server and try again.

**Problem: Database corrupted**  
→ Delete tasks.db and restart. Database and seeded data will be recreated.

---

## 🏆 Week 3 Checklist

- ✅ Database automatically created on first run
- ✅ Table automatically created on first run
- ✅ 3 demo tasks seeded only once (not duplicated on restart)
- ✅ All CRUD operations use SQLite queries
- ✅ All queries use ? parameterized placeholders (safe)
- ✅ Data survives server restart
- ✅ All endpoints work identically to Week 2
- ✅ Correct status codes (200, 201, 204, 400, 404)
- ✅ Swagger UI works
- ✅ Web interface works
- ✅ Comprehensive documentation
- ✅ Ready for deployment

---

## 📞 Resources

- **SQLite Documentation:** https://www.sqlite.org/docs.html
- **Python sqlite3:** https://docs.python.org/3/library/sqlite3.html
- **DB Browser for SQLite:** https://sqlitebrowser.org/
- **FastAPI:** https://fastapi.tiangolo.com/

---

## 👤 Author

**Shravani Rajendra Patil**
- GitHub: https://github.com/shravani22patil
- LinkedIn: https://linkedin.com/in/shravani-patil-38791b286
- Email: shravanipatil580@gmail.com

---

## 📄 Version History

- **v2.0** (Week 3) — SQLite database, persistent storage
- **v1.0** (Week 2) — In-memory CRUD API, Swagger UI

---

**Ready for production.** 🚀

All data now persists. Your backend is real.
