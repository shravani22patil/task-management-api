# 🚀 Setup Guide - Task API

Follow these steps to get the Task API running in 2 minutes.

---

## Step 1: Install Python Dependencies

```bash
pip install -r requirements.txt
```

**Expected output:**
```
Successfully installed fastapi uvicorn pydantic python-multipart
```

If you get errors, make sure you have Python 3.8+ installed:
```bash
python --version
```

---

## Step 2: Start the Server

```bash
python main.py
```

**You should see:**
```
🚀 Starting Task API Server...
📖 Swagger UI: http://localhost:8000/docs
🔗 ReDoc: http://localhost:8000/redoc
🏠 API Root: http://localhost:8000/
INFO:     Uvicorn running on http://0.0.0.0:8000
```

✅ **Server is running!**

---

## Step 3: Access the Application

### Option A: Interactive Swagger UI (Recommended)
Open your browser and go to:
```
http://localhost:8000/docs
```

Click on any endpoint, click "Try it out", and test the API directly!

### Option B: Beautiful ReDoc Documentation
```
http://localhost:8000/redoc
```

Nice, readable API documentation.

### Option C: Web Interface
Open the file `index.html` directly in your browser:
```bash
# On macOS/Linux
open index.html

# On Windows
start index.html
```

Or double-click the file in your file explorer.

### Option D: Terminal/cURL
```bash
# Get all tasks
curl http://localhost:8000/tasks

# Create a task
curl -X POST http://localhost:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"Buy milk"}'

# Get statistics
curl http://localhost:8000/stats
```

---

## Step 4: Test All Endpoints

### In Swagger UI (http://localhost:8000/docs):

1. **List Tasks** — GET /tasks
   - Click "Try it out" → "Execute"
   - See all 3 demo tasks

2. **Create Task** — POST /tasks
   - Click "Try it out"
   - Fill in: `{"title":"My new task","description":"Do this"}`
   - Click "Execute"
   - Status should be 201

3. **Get Single Task** — GET /tasks/1
   - Click "Try it out"
   - Leave task_id = 1
   - Click "Execute"

4. **Update Task** — PUT /tasks/1
   - Click "Try it out"
   - Fill in: `{"done":true}`
   - Click "Execute"
   - Status should be 200

5. **Delete Task** — DELETE /tasks/1
   - Click "Try it out"
   - Leave task_id = 1
   - Click "Execute"
   - Status should be 204

6. **Get Stats** — GET /stats
   - Click "Try it out" → "Execute"
   - See task statistics

---

## Step 5: Use the Web Interface

Open `index.html` in your browser:

1. **Create Task**
   - Enter title: "Buy groceries"
   - Enter description: "Milk, bread, eggs"
   - Click "Create Task"
   - ✅ Task appears in the list

2. **Mark as Done**
   - Click the checkbox next to a task
   - Task is marked as complete

3. **Delete**
   - Click the delete button
   - Task is removed

4. **Search**
   - Type in search box
   - Tasks are filtered in real-time

5. **Filter**
   - Click "Pending" to see incomplete tasks
   - Click "Completed" to see done tasks
   - Click "All Tasks" to see everything

---

## Step 6: Check Stats

The dashboard shows:
- **Total Tasks** — All tasks
- **Completed** — Done tasks
- **Pending** — Incomplete tasks
- **Completion Rate** — Percentage done

---

## Troubleshooting

### Problem: "Port 8000 already in use"
```bash
# Use a different port
uvicorn main:app --port 8001

# Then access at http://localhost:8001
```

### Problem: "ModuleNotFoundError"
```bash
# Install dependencies again
pip install -r requirements.txt
```

### Problem: Web interface can't connect to API
- Make sure the server is running (`python main.py`)
- Check that it's on port 8000
- The API should respond at `http://localhost:8000/tasks`

### Problem: CORS errors in browser console
The web interface is designed to be opened as a local file (`index.html`), not hosted on a separate server. This prevents CORS issues.

---

## Understanding the Code

### `main.py`
- **Lines 1-50:** Imports and setup
- **Lines 51-120:** Data models (Task, TaskCreate, etc.)
- **Lines 121-160:** In-memory database
- **Lines 161-200:** Utility functions
- **Lines 201-250:** GET endpoints
- **Lines 251-300:** POST endpoint (create)
- **Lines 301-350:** PUT endpoint (update)
- **Lines 351-380:** DELETE endpoint
- **Lines 381-400:** Bonus endpoints (stats, reset)

### `index.html`
- **CSS:** Dark theme, responsive design, smooth animations
- **JavaScript:** Fetch API for talking to backend
- **Features:** Create, read, update, delete, search, filter

---

## Next: Prepare for GitHub

```bash
# Initialize git (if not already)
git init

# Add all files
git add .

# Make first commit
git commit -m "Initial commit: Task API with CRUD endpoints"

# Connect to GitHub and push
git remote add origin <your-github-url>
git push -u origin main
```

---

## Final Checklist

- [ ] Server runs without errors
- [ ] Swagger UI loads at /docs
- [ ] Web interface loads
- [ ] Can create tasks
- [ ] Can read tasks
- [ ] Can update tasks
- [ ] Can delete tasks
- [ ] Statistics work
- [ ] Search works
- [ ] Filter works
- [ ] Code is committed to GitHub
- [ ] README explains everything

✅ **You're ready to submit!**

---

## Need Help?

1. **Check the README.md** — Full API documentation
2. **Test in Swagger UI** — Interactive testing
3. **Check browser console** — JavaScript errors
4. **Check terminal** — Server errors
5. **Check requirements.txt** — All dependencies listed

---

Happy coding! 🚀
