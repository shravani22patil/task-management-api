# Task Management API 📋 (Docker + PostgreSQL Edition)

**Week 3 Assignment: Containerize Your Stack**

A production-ready **CRUD API** for task management built with **FastAPI**, **PostgreSQL**, and **Docker**. Everything runs in containers.

**Built for:** FlyRank Backend Internship - Week 2 → Week 3

---

## 🌟 What's New in Week 3?

✨ **PostgreSQL Database** — Professional relational database instead of SQLite  
✨ **Docker Containers** — App and database both containerized  
✨ **docker-compose** — One command to run everything  
✨ **Environment Secrets** — .env file for configuration  
✨ **Production Ready** — Can deploy to cloud immediately  

---

## 📊 Architecture Evolution

### Week 2: In-Memory
```
Client → FastAPI → Python List (memory)
                   ❌ Lost on restart
```

### Week 2: SQLite
```
Client → FastAPI → SQLite (tasks.db file)
                   ✅ Survives restart
```

### Week 3: Docker + PostgreSQL (You are here)
```
Client → FastAPI Container → PostgreSQL Container
         🐳 Docker           🐳 Docker
         ✅ Scalable
         ✅ Portable
         ✅ Professional
```

---

## 🎯 Features

✅ **Complete CRUD Operations** — Create, Read, Update, Delete  
✅ **PostgreSQL Database** — Enterprise-grade relational database  
✅ **Docker Containers** — Isolated, reproducible environments  
✅ **docker-compose** — One command to run entire stack  
✅ **Full REST API** — Same 8 endpoints from Week 2  
✅ **Input Validation** — Pydantic models  
✅ **Parameterized Queries** — SQL injection safe (psycopg)  
✅ **Error Handling** — Comprehensive responses  
✅ **Interactive Swagger UI** — Test endpoints in browser  
✅ **Modern Web Interface** — Task management dashboard  
✅ **Health Checks** — Docker monitors service health  
✅ **Data Persistence** — Volume mounts for PostgreSQL  

---

## 🚀 Quick Start

### Prerequisites

- **Docker** — https://www.docker.com/products/docker-desktop
- **Docker Compose** — Usually included with Docker Desktop

### 1. Clone Repository
```bash
git clone https://github.com/YOUR_USERNAME/task-api.git
cd task-api
```

### 2. Copy Environment File
```bash
cp .env.example .env
# .env already has correct values for docker-compose
```

### 3. Start Everything
```bash
docker-compose up
```

**That's it!** You'll see:
```
task-api-db  | database system is ready to accept connections ✅
task-api-app | 🚀 Starting Task API Server (PostgreSQL Edition)...
task-api-app | 🗄️  Database: postgres:5432
task-api-app | 📖 Swagger UI: http://localhost:8000/docs
```

### 4. Access the Application

- **Web Interface:** Open `index.html` in your browser
- **Swagger UI:** http://localhost:8000/docs ⭐ **Use this to test**
- **ReDoc:** http://localhost:8000/redoc
- **API Root:** http://localhost:8000/

---

## 🐳 Docker Concepts Explained

### Docker
A containerization platform that packages your app + dependencies into a self-contained unit.

**Advantages:**
- Runs identically on laptop, CI/CD, cloud, production
- "Works on my machine" → "Works everywhere"
- Isolation: multiple apps can run without conflicts
- Easy to scale: spin up more containers

### Docker Compose
Orchestrates multiple Docker containers (app + database) with one `docker-compose.yaml` file.

**What it does:**
```yaml
services:
  postgres:     # Database container
    ...
  api:          # App container
    ...
```

One command runs both, networks them together, manages volumes.

### Containers vs Virtual Machines
```
Virtual Machine:
OS → Hypervisor → VM (full OS) → App → Dependencies
Heavy (gigabytes), slow startup

Container:
OS → Docker → Container (runtime) → App → Dependencies
Light (megabytes), instant startup
```

---

## 📁 New Files in Week 3

```
task-api/
├── Dockerfile              ← Tells Docker how to build app image
├── docker-compose.yaml     ← Orchestrates app + database
├── .env                    ← Database credentials (git-ignored)
├── .env.example            ← Template for .env
├── main.py                 ← FastAPI (modified for Postgres)
├── index.html              ← Web UI (unchanged)
├── requirements.txt        ← Updated with psycopg
└── ... (other files)
```

---

## 📖 How Docker Compose Works

### Start Everything
```bash
docker-compose up
```

**What happens:**
1. Docker builds `task-api-app` image from Dockerfile
2. Docker starts `postgres` container
3. Docker waits for Postgres to be healthy (healthcheck)
4. Docker starts `api` container
5. App connects to database at `postgres:5432`
6. Seeds database with 3 demo tasks
7. API ready at `http://localhost:8000`

### Stop Everything
```bash
docker-compose down
```

**What happens:**
- Stops both containers
- Data persists in `postgres_data` volume
- Images remain (fast startup next time)

### Stop + Delete Everything
```bash
docker-compose down -v
```

**What happens:**
- Stops both containers
- Deletes `postgres_data` volume
- Starts fresh next time

---

## 🔧 Docker Commands

### See Running Containers
```bash
docker ps
```

### See All Containers (including stopped)
```bash
docker ps -a
```

### View Logs
```bash
docker-compose logs -f api       # API logs
docker-compose logs -f postgres  # Database logs
docker-compose logs -f           # All logs
```

### Execute Command in Running Container
```bash
# Open bash shell in app container
docker-compose exec api bash

# Query database from container
docker-compose exec postgres psql -U postgres -d tasks
```

### View Docker Resources
```bash
docker system df
docker image ls
docker volume ls
```

---

## 🔌 Environment Configuration

### .env File
```
DATABASE_URL=postgresql://postgres:dev@postgres:5432/tasks
```

**Structure:**
```
postgresql://[username]:[password]@[host]:[port]/[database]
```

**For docker-compose:** `postgres` hostname (container name)
**For localhost:** `localhost` hostname

### .env.example
Template file so teammates know what variables are needed. Always commit this, never commit `.env`.

### Why .env?
```bash
# ❌ BAD: Secrets in code
DATABASE_URL = "postgresql://user:password@prod.com/db"
git commit  # Oops! Password visible in git history forever!

# ✅ GOOD: Secrets in environment
.env file (git-ignored)
App reads from environment
git commit  # Password never goes to github!
```

---

## 📊 Database Schema

Same as Week 2:

| Column | Type | Notes |
|--------|------|-------|
| **id** | SERIAL | Primary key (auto-increment) |
| **title** | TEXT | Task title (required) |
| **description** | TEXT | Optional description |
| **done** | BOOLEAN | Completion status |
| **created_at** | TEXT | ISO 8601 timestamp |
| **updated_at** | TEXT | ISO 8601 timestamp |

---

## 📖 API Endpoints

**All endpoints identical to Week 2.** Same requests, same responses, same status codes.

### List Tasks
```bash
curl http://localhost:8000/tasks
```

### Create Task
```bash
curl -X POST http://localhost:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"Buy milk","description":"2 liters"}'
```

### Update Task
```bash
curl -X PUT http://localhost:8000/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"done":true}'
```

### Delete Task
```bash
curl -X DELETE http://localhost:8000/tasks/1
```

### Get Stats
```bash
curl http://localhost:8000/stats
```

### Health Check
```bash
curl http://localhost:8000/health
```

---

## 🏗️ Architecture

### Before Docker (Week 2)
```
Your laptop:
├── Python venv
├── FastAPI app
├── SQLite database
├── Requirements installed
└── Works only on YOUR machine
```

### After Docker (Week 3)
```
Container 1 (api):
├── Python 3.11
├── FastAPI app
├── Dependencies installed
└── Isolated environment

Container 2 (postgres):
├── PostgreSQL 15
├── task database
├── Data volume (persists)
└── Isolated environment

Network:
├── Both containers connected
└── Api talks to postgres:5432
```

**Same code, different deployment.** Clients see no difference.

---

## 🚢 Deployment

### Local Development
```bash
docker-compose up
```

### Production Deployment

```bash
# Build image
docker build -t task-api:latest .

# Push to registry (Docker Hub, AWS ECR, etc.)
docker push task-api:latest

# Deploy to cloud platform (Heroku, AWS, Google Cloud, etc.)
# Usually just: docker-compose up
# With real Postgres connection string in .env
```

### Cloud Services That Support Docker:
- **Heroku** — `docker-compose.yml` deployment
- **AWS ECS** — Container orchestration
- **Google Cloud Run** — Serverless containers
- **DigitalOcean** — App Platform
- **Railway** — Simple docker deployment
- **Render** — Free tier available

---

## 🧪 Testing

### Swagger UI (Easiest)
1. Go to http://localhost:8000/docs
2. Click any endpoint
3. Click "Try it out"
4. Click "Execute"
5. See response

### curl (Terminal)
```bash
# Test API is up
curl http://localhost:8000/health

# Create task
curl -X POST http://localhost:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"Docker test"}'

# List tasks
curl http://localhost:8000/tasks
```

### psql (Database Terminal)
```bash
# Connect to Postgres from host
psql -h localhost -U postgres -d tasks -W

# Inside postgres:
SELECT * FROM tasks;
SELECT COUNT(*) FROM tasks;
UPDATE tasks SET done = true WHERE id = 1;
DELETE FROM tasks WHERE id = 1;
```

---

## 🔒 Security Considerations

### Secrets Management
```bash
# ✅ GOOD: Secrets in .env (git-ignored)
# ✅ GOOD: Pass via docker -e flag
# ✅ GOOD: Use Docker secrets (production)

# ❌ BAD: Hardcoded in code
# ❌ BAD: In docker-compose.yaml (committed to git)
# ❌ BAD: In Dockerfile (visible in image)
```

### SQL Safety
All queries use parameterized placeholders:
```python
# ✅ SAFE: Parameterized
cursor.execute("SELECT * FROM tasks WHERE id = %s", (task_id,))

# ❌ DANGEROUS: String interpolation
cursor.execute(f"SELECT * FROM tasks WHERE id = {task_id}")
```

### Container Security
```dockerfile
# ✅ GOOD: Non-root user (production)
# ✅ GOOD: Minimal base image
# ✅ GOOD: Regular updates

# ❌ BAD: Running as root
# ❌ BAD: Large base image
# ❌ BAD: Outdated dependencies
```

---

## 📊 Comparison: Weeks 2 vs 3

| Feature | Week 2 | Week 3 |
|---------|--------|--------|
| **Database** | SQLite file | PostgreSQL server |
| **Storage** | tasks.db | Postgres volume |
| **Container** | None | Docker |
| **Orchestration** | Manual | docker-compose |
| **Environment** | Hardcoded | .env file |
| **Scalability** | Single instance | Multiple instances |
| **Deployment** | Copy files | docker-compose.yaml |
| **Production-ready** | No | Yes |
| **API Endpoints** | Same ✓ | Same ✓ |

---

## 🎓 What You're Learning

✅ **Containerization** — Docker & isolation
✅ **Orchestration** — docker-compose
✅ **Environment Management** — .env secrets
✅ **PostgreSQL** — Professional database
✅ **Health Checks** — Container monitoring
✅ **Volumes** — Data persistence
✅ **Networking** — Container communication
✅ **Production Patterns** — Real-world deployments

---

## 🚀 Next Steps

### Local Development
```bash
docker-compose up          # Start everything
docker-compose down        # Stop everything
docker-compose logs -f     # Watch logs
```

### Deploy to Cloud
```bash
# 1. Push code to GitHub
git push origin main

# 2. Create account on cloud platform (Heroku, Railway, etc.)

# 3. Connect GitHub repo

# 4. Platform automatically builds Dockerfile and runs docker-compose

# 5. Your app is live!
```

### Advanced
- Add environment-specific configs
- Use secrets manager
- Add CI/CD pipeline
- Scale to multiple instances
- Add monitoring and logging

---

## 📞 Troubleshooting

### Port Already in Use
```bash
# Find what's using port 5432
lsof -i :5432

# Change port in docker-compose.yaml:
postgres:
  ports:
    - "5433:5432"  # Change 5432 to 5433
```

### Database Won't Connect
```bash
# Check if postgres container is healthy
docker ps

# Check logs
docker-compose logs postgres

# Verify DATABASE_URL in .env
cat .env
```

### Container Won't Start
```bash
# See full error
docker-compose up --no-detach

# Check volumes
docker volume ls

# Rebuild image
docker-compose build --no-cache
```

### Data Lost After docker-compose down
**This shouldn't happen.** Volume persists. Check:
```bash
docker volume ls | grep postgres_data
docker volume inspect task-api_postgres_data
```

---

## 📚 Resources

- **Docker Docs:** https://docs.docker.com/
- **Docker Compose Docs:** https://docs.docker.com/compose/
- **PostgreSQL Docs:** https://www.postgresql.org/docs/
- **psycopg (Python Postgres driver):** https://www.psycopg.org/
- **FastAPI:** https://fastapi.tiangolo.com/

---

## 👤 Author

**Shravani Rajendra Patil**
- GitHub: https://github.com/shravani22patil
- LinkedIn: https://linkedin.com/in/shravani-patil-38791b286
- Email: shravanipatil580@gmail.com

---

## 📄 Version History

- **v3.0** (Week 3) — Docker + PostgreSQL, containerized stack
- **v2.0** (Week 3) — SQLite database, persistent storage
- **v1.0** (Week 2) — In-memory CRUD API, Swagger UI

---

**Production-ready and containerized.** 🐳🚀
