# Task Management API 📋

A production-ready **CRUD API** for task management built with **FastAPI** and **Python**. Features full API documentation, interactive Swagger UI, and a modern web interface.

**Built for:** FlyRank Backend Internship - Week 2 Assignment

---

## 🌟 Features

✅ **Complete CRUD Operations** — Create, Read, Update, Delete tasks  
✅ **Full REST API** — Proper HTTP methods and status codes (201, 204, 404, etc.)  
✅ **Interactive Swagger UI** — Test endpoints directly in the browser  
✅ **Modern Web Interface** — Beautiful, responsive task management dashboard  
✅ **Search & Filter** — Find tasks by title or filter by completion status  
✅ **Statistics** — Real-time task completion metrics  
✅ **Input Validation** — Pydantic models for data validation  
✅ **Error Handling** — Comprehensive error responses  
✅ **Well-Documented** — Detailed docstrings and OpenAPI specs  
✅ **Demo Data** — Comes with 3 sample tasks  

---

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd task-api
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Server
```bash
python main.py
```

You'll see:
```
🚀 Starting Task API Server...
📖 Swagger UI: http://localhost:8000/docs
🔗 ReDoc: http://localhost:8000/redoc
🏠 API Root: http://localhost:8000/
INFO:     Uvicorn running on http://0.0.0.0:8000
```

### 4. Access the Application

- **Web Interface:** Open `index.html` in your browser
- **Swagger UI (Interactive Docs):** http://localhost:8000/docs
- **ReDoc (Beautiful Docs):** http://localhost:8000/redoc
- **API Root:** http://localhost:8000/

---

## 📖 API Endpoints

### Base URL
```
http://localhost:8000
```

### Endpoints Reference

#### **1. List All Tasks** ✅
```http
GET /tasks
```
**Optional Query Parameters:**
- `done` (boolean): Filter by completion status
- `search` (string): Search task titles
- `limit` (int): Number of results (default: 100)
- `offset` (int): Number to skip (pagination)

**Examples:**
```bash
# Get all tasks
curl http://localhost:8000/tasks

# Get only completed tasks
curl "http://localhost:8000/tasks?done=true"

# Search for "milk" in tasks
curl "http://localhost:8000/tasks?search=milk"

# Pagination: get tasks 20-30
curl "http://localhost:8000/tasks?limit=10&offset=20"
```

**Response (200 OK):**
```json
[
  {
    "id": 1,
    "title": "Learn FastAPI",
    "description": "Complete the tutorial",
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

**Examples:**
```bash
curl http://localhost:8000/tasks/1
```

**Response (200 OK):**
```json
{
  "id": 1,
  "title": "Learn FastAPI",
  "description": "Complete the tutorial",
  "done": false,
  "created_at": "2026-06-15T09:00:00",
  "updated_at": "2026-06-15T09:00:00"
}
```

**Response (404 Not Found):**
```json
{
  "detail": {
    "error": "Task 999 not found",
    "status_code": 404
  }
}
```

---

#### **3. Create Task** ✅
```http
POST /tasks
Content-Type: application/json

{
  "title": "Buy milk",
  "description": "Get 2 liters of whole milk"
}
```

**Examples:**
```bash
curl -X POST http://localhost:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"Buy milk","description":"Get 2 liters"}'
```

**Response (201 Created):**
```json
{
  "id": 4,
  "title": "Buy milk",
  "description": "Get 2 liters of whole milk",
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
  "title": "Buy milk and bread",
  "done": true
}
```

**Examples:**
```bash
# Update title and mark as done
curl -X PUT http://localhost:8000/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"title":"Updated title","done":true}'

# Only mark as done
curl -X PUT http://localhost:8000/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"done":true}'
```

**Response (200 OK):**
```json
{
  "id": 1,
  "title": "Updated title",
  "description": "Description unchanged",
  "done": true,
  "created_at": "2026-06-15T09:00:00",
  "updated_at": "2026-06-15T12:30:00"
}
```

---

#### **5. Delete Task** ✅
```http
DELETE /tasks/{task_id}
```

**Examples:**
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

**Examples:**
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
  "tasks_in_memory": 10
}
```

---

#### **8. Reset to Demo Data** 🔄
```http
POST /reset
```

**Response (200 OK):**
```json
{
  "message": "Tasks reset to demo state",
  "tasks_count": 3,
  "timestamp": "2026-06-15T12:00:00"
}
```

---

## 🧪 Testing with cURL

```bash
# 1. Get all tasks
curl http://localhost:8000/tasks

# 2. Create a new task
curl -X POST http://localhost:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"Buy groceries","description":"Milk, bread, eggs"}'

# 3. Get specific task
curl http://localhost:8000/tasks/1

# 4. Update task (mark as done)
curl -X PUT http://localhost:8000/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"done":true}'

# 5. Delete task
curl -X DELETE http://localhost:8000/tasks/1

# 6. Get statistics
curl http://localhost:8000/stats

# 7. Search tasks
curl "http://localhost:8000/tasks?search=milk"

# 8. Filter completed tasks
curl "http://localhost:8000/tasks?done=true"
```

---

## 💻 Testing in Swagger UI

1. Go to **http://localhost:8000/docs**
2. Click on any endpoint
3. Click "Try it out"
4. Fill in parameters/body
5. Click "Execute"
6. See the response immediately

This is **much easier** than cURL for manual testing!

---

## 🎨 Web Interface Features

- **Create Tasks** — Add new tasks with title and description
- **Search** — Find tasks by typing in the search box
- **Filter** — View all, pending, or completed tasks
- **Toggle Done** — Click the checkbox to mark tasks complete
- **Delete** — Remove tasks permanently
- **Real-time Stats** — See total, completed, and pending counts
- **Responsive Design** — Works on desktop and mobile
- **Dark Mode** — Professional dark theme with smooth animations

---

## 📁 Project Structure

```
task-api/
├── main.py                 # FastAPI application (ALL ENDPOINTS)
├── index.html             # Web interface (modern, interactive UI)
├── requirements.txt       # Python dependencies
├── README.md             # This file
└── .gitignore           # Git ignore file
```

---

## 🔧 Tech Stack

- **Framework:** FastAPI (modern Python web framework)
- **Server:** Uvicorn (async HTTP server)
- **Validation:** Pydantic (data validation)
- **Frontend:** HTML5, CSS3, Vanilla JavaScript
- **Database:** In-memory list (can be swapped with SQLite/PostgreSQL)

---

## 📝 Code Quality

✅ **Comprehensive Docstrings** — Every function documented  
✅ **Type Hints** — Full type annotations  
✅ **Error Handling** — Proper HTTP status codes and error messages  
✅ **Input Validation** — Pydantic models validate all inputs  
✅ **RESTful Design** — Proper HTTP methods and semantics  
✅ **Comments** — Code organized into sections with clear intent

---

## 🚀 Deployment

### To deploy on a server:

```bash
# Install on server
pip install -r requirements.txt

# Run with production settings
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```

Or with a process manager (Gunicorn):

```bash
pip install gunicorn
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app
```

---

## 📊 Example API Flow

```
1. User opens index.html
   ↓
2. JavaScript fetches GET /tasks
   ↓
3. API returns all tasks
   ↓
4. UI renders tasks in cards
   ↓
5. User clicks "Create Task"
   ↓
6. JavaScript POSTs to /tasks
   ↓
7. API creates task, returns 201 with new task
   ↓
8. UI refreshes, new task appears
```

---

## 🎓 Learning Objectives (Week 2 Assignment)

This project demonstrates:

✅ **HTTP Methods** — GET, POST, PUT, DELETE  
✅ **Status Codes** — 200, 201, 204, 400, 404  
✅ **REST Principles** — Proper endpoint design  
✅ **CRUD Operations** — Complete data lifecycle  
✅ **API Documentation** — Swagger/OpenAPI  
✅ **Data Validation** — Input checking  
✅ **Error Handling** — User-friendly error messages  
✅ **Frontend Integration** — Client-side API calls  
✅ **Modern Web Development** — HTML/CSS/JS best practices

---

## ✅ Checklist for FlyRank Submission

- [ ] Clone repo
- [ ] Install dependencies: `pip install -r requirements.txt`
- [ ] Run server: `python main.py`
- [ ] Test in Swagger UI: http://localhost:8000/docs
- [ ] Test web interface: Open `index.html`
- [ ] All CRUD operations work
- [ ] Status codes are correct
- [ ] Documentation is complete
- [ ] Code is well-commented
- [ ] Repo has ≥6 commits
- [ ] README explains everything
- [ ] Submit GitHub link to FlyRank

---

## 🐛 Troubleshooting

**Port 8000 already in use:**
```bash
# Change port
uvicorn main:app --port 8001
```

**CORS issues with web interface:**
The API is designed to run on localhost:8000 — open `index.html` locally in browser.

**Module not found errors:**
```bash
pip install -r requirements.txt
```

**Can't connect to API:**
- Ensure server is running: `python main.py`
- Check firewall isn't blocking port 8000
- Use `http://` not `https://`

---

## 📚 Resources

- **FastAPI Docs:** https://fastapi.tiangolo.com/
- **Pydantic Docs:** https://docs.pydantic.dev/
- **HTTP Status Codes:** https://httpwg.org/specs/rfc9110.html#status.codes
- **REST Best Practices:** https://restfulapi.net/

---

## 👤 Author

**Shravani Rajendra Patil**
- GitHub: https://github.com/shravani22patil
- LinkedIn: https://linkedin.com/in/shravani-patil-38791b286
- Email: shravanipatil580@gmail.com

---

## 📄 License

Built as an assignment for FlyRank Backend Internship Week 2.

---

## 🎯 Next Steps

To make this production-ready:

1. Add SQLite/PostgreSQL database
2. Add user authentication (JWT tokens)
3. Add task categories/priorities
4. Add due dates and reminders
5. Add unit tests
6. Add rate limiting
7. Deploy to cloud (Heroku, Railway, AWS)

---

**Happy coding! 🚀**
