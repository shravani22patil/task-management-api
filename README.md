# 🔐 Task Management API

A full-featured **Task Management REST API** built with **FastAPI**, progressively developed across the **FlyRank Backend Internship Weeks 2, 3, and 4**.

The project started as a simple CRUD-based task management API and was progressively enhanced with persistent databases, PostgreSQL, Docker containerization, Supabase authentication, JWT verification, protected routes, and interactive Swagger documentation.

---

## 📌 Project Overview

This repository represents the **continuous development of the same Task Management API across multiple internship assignments**.

Instead of creating a separate repository for each week, the project was incrementally upgraded as new backend concepts were introduced.

### Project Evolution

```text
┌───────────────────────────────────────────────┐
│                  WEEK 2                       │
│         FastAPI Task Management API           │
│                                               │
│  • REST API                                   │
│  • CRUD Operations                            │
│  • Pydantic Validation                        │
│  • Swagger / OpenAPI                          │
│  • Search & Filtering                         │
│  • Statistics                                 │
│  • Web Interface                              │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│                  WEEK 3                       │
│       Persistent Database + Docker            │
│                                               │
│  • PostgreSQL                                 │
│  • Database Persistence                       │
│  • psycopg                                    │
│  • Docker                                     │
│  • Docker Compose                             │
│  • Containerized API                          │
│  • PostgreSQL Container                       │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│                  WEEK 4                       │
│       Authentication & Protected API          │
│                                               │
│  • Supabase Auth                              │
│  • User Signup                                │
│  • User Login                                 │
│  • JWT Access Tokens                          │
│  • JWT Verification                           │
│  • Reusable Auth Dependency                   │
│  • Protected Routes                            │
│  • Logout                                     │
│  • HTTP Bearer Security                       │
│  • Swagger Authorization                      │
└───────────────────────────────────────────────┘
```

---

# ✨ Features

## Core Task Management

- ✅ Create tasks
- ✅ Read tasks
- ✅ Read individual tasks
- ✅ Update tasks
- ✅ Delete tasks
- ✅ Mark tasks as completed
- ✅ Search tasks
- ✅ Filter tasks by completion status
- ✅ Pagination support
- ✅ Task statistics
- ✅ Health check endpoint
- ✅ Demo task data

## Backend

- ✅ FastAPI REST API
- ✅ Pydantic request/response validation
- ✅ Proper HTTP methods
- ✅ HTTP status codes
- ✅ Error handling
- ✅ OpenAPI documentation
- ✅ Swagger UI
- ✅ ReDoc documentation

## Database

- ✅ PostgreSQL persistence
- ✅ psycopg PostgreSQL driver
- ✅ Database connection through environment variables
- ✅ Dockerized PostgreSQL
- ✅ Persistent Docker volume

## Authentication

- ✅ Supabase Authentication
- ✅ User signup
- ✅ User login
- ✅ JWT access token
- ✅ Refresh token
- ✅ JWT verification
- ✅ Protected endpoints
- ✅ Reusable FastAPI authentication dependency
- ✅ Logout
- ✅ Invalid/tampered token handling
- ✅ Missing token handling
- ✅ Expired token handling
- ✅ HTTP Bearer authentication in Swagger

## DevOps / Deployment

- ✅ Dockerfile
- ✅ Docker Compose
- ✅ Multi-stage Docker build
- ✅ PostgreSQL container
- ✅ API container
- ✅ Container health checks
- ✅ Environment-based configuration

---

# 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.11 | Programming language |
| FastAPI | REST API framework |
| Uvicorn | ASGI server |
| Pydantic | Data validation |
| PostgreSQL | Relational database |
| psycopg | PostgreSQL database driver |
| Supabase | Authentication |
| JWT | Authentication tokens |
| python-jose | JWT processing |
| Cryptography | Cryptographic operations |
| Docker | Containerization |
| Docker Compose | Multi-container development |
| Swagger UI | Interactive API documentation |
| ReDoc | API documentation |
| HTML5 | Frontend |
| CSS3 | Frontend styling |
| JavaScript | Frontend interaction |
| Git | Version control |
| GitHub | Source code hosting |

---

# 📸 Screenshots & Evidence

## Week 2 — FastAPI Task Management API

The initial version provided the core Task Management REST API with CRUD operations and interactive Swagger documentation.

<img width="1906" height="882" alt="Week 2 Task API" src="https://github.com/user-attachments/assets/069a130b-26a6-4fc2-ae24-f38405187f4b" />
---

## Week 3 — Docker + PostgreSQL

The API was containerized using Docker Compose with PostgreSQL as the persistent database.

<img width="1072" height="271" alt="Docker PostgreSQL Running" src="https://github.com/user-attachments/assets/5012c001-4c9d-4246-b7ee-501f8791440e" />

---

## Week 4 — Supabase Authentication

The API was extended with Supabase authentication, JWT bearer authentication, public

<img width="1860" height="952" alt="Week 4 Supabase Authentication" src="https://github.com/user-attachments/assets/666d67be-20ba-4067-9063-64be82ea12ed" />

---

# 📁 Project Structure

```text
task-api/
│
├── main.py
│   └── Current Week 4 FastAPI application
│
├── main_week2.py
│   └── Week 2 version of the API
│
├── main_week3.py
│   └── Week 3 PostgreSQL version
│
├── index.html
│   └── Task management web interface
│
├── requirements.txt
│   └── Python dependencies
│
├── Dockerfile
│   └── Docker image configuration
│
├── docker-compose.yaml
│   └── FastAPI + PostgreSQL services
│
├── .env.example
│   └── Environment variable template
│
├── .gitignore
│   └── Files excluded from Git
│
└── README.md
    └── Project documentation
```

> The real `.env` file is intentionally excluded from version control because it contains private credentials.

---

# 🚀 Getting Started

## Prerequisites

Before running the project, install:

- Python 3.11+
- Git
- Docker Desktop
- A Supabase account/project

---

# 🔑 Environment Configuration

The project uses environment variables for configuration.

Create a `.env` file in the project root.

You can use `.env.example` as a template.

```env
SUPABASE_URL=your_supabase_project_url
SUPABASE_KEY=your_supabase_anon_key
PORT=8000
DATABASE_URL=your_database_url
```

### Environment Variables

| Variable | Description |
|---|---|
| `SUPABASE_URL` | Supabase project URL |
| `SUPABASE_KEY` | Supabase anon/public API key |
| `PORT` | Port used by the FastAPI server |
| `DATABASE_URL` | PostgreSQL database connection string |

### Security Note

Never commit the actual `.env` file to GitHub.

The repository contains:

```text
.env.example
```

instead of the real credentials.

The `.gitignore` file contains:

```text
.env
```

to prevent accidental commits.

---

# ☁️ Supabase Setup

Create a Supabase project and obtain the project API information from the Supabase dashboard.

The application requires:

```text
SUPABASE_URL
SUPABASE_KEY
```

Use the **anon/public key** required by the application.

Do not commit private Supabase credentials to the repository.

For local development, Supabase authentication is used for:

- Creating users
- Authenticating users
- Generating access tokens
- Verifying authenticated users
- Ending authenticated sessions

---

# ▶️ Running the Project

There are two supported ways to run the project.

---

# 🐍 Option 1 — Run with Python

## 1. Clone the repository

```bash
git clone https://github.com/shravani22patil/task-management-api.git
```

Move into the project:

```bash
cd task-management-api
```

---

## 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 3. Configure environment variables

Create:

```text
.env
```

using:

```text
.env.example
```

as the reference.

---

## 4. Start the API

```bash
python main.py
```

The server starts on:

```text
http://localhost:8000
```

---

# 🐳 Option 2 — Run with Docker Compose

Docker Compose is the recommended way to run the current PostgreSQL-backed version.

Make sure **Docker Desktop is running**.

Run:

```bash
docker compose up --build
```

This starts:

```text
FastAPI API
     │
     ▼
PostgreSQL Database
```

The API is available at:

```text
http://localhost:8000
```

Swagger UI:

```text
http://localhost:8000/docs
```

ReDoc:

```text
http://localhost:8000/redoc
```

Stop the containers:

```bash
docker compose down
```

---

# 🐳 Docker Architecture

The project uses Docker Compose to run the backend API and PostgreSQL database as separate services.

```text
                   Docker Compose
                         │
          ┌──────────────┴──────────────┐
          │                             │
          ▼                             ▼
┌───────────────────┐        ┌───────────────────┐
│    FastAPI API    │        │    PostgreSQL     │
│                   │        │                   │
│    Port: 8000     │───────▶│    Port: 5432     │
│                   │        │                   │
└───────────────────┘        └───────────────────┘
```

The PostgreSQL database uses a persistent Docker volume so that database data can survive container restarts.

---

# 📖 API Documentation

FastAPI automatically generates OpenAPI documentation.

## Swagger UI

Open:

```text
http://localhost:8000/docs
```

Swagger allows the API to be tested directly from the browser.

## ReDoc

Open:

```text
http://localhost:8000/redoc
```

---

# 📚 API Reference

## Authentication & Access

| Method | Endpoint | Authentication | Description |
|---|---|---|---|
| POST | `/auth/signup` | ❌ Public | Create a new user |
| POST | `/auth/login` | ❌ Public | Authenticate user |
| POST | `/auth/logout` | 🔒 Bearer JWT | Logout authenticated user |
| GET | `/public/info` | ❌ Public | Public information |
| GET | `/protected/profile` | 🔒 Bearer JWT | Get authenticated user profile |
| GET | `/protected/tasks` | 🔒 Bearer JWT | Get protected tasks |
| POST | `/protected/tasks` | 🔒 Bearer JWT | Create protected task |
| PUT | `/protected/tasks/{task_id}` | 🔒 Bearer JWT | Update protected task |
| DELETE | `/protected/tasks/{task_id}` | 🔒 Bearer JWT | Delete protected task |

---

## Task Management

| Method | Endpoint | Description |
|---|---|---|
| GET | `/tasks` | List tasks |
| GET | `/tasks/{task_id}` | Get a specific task |
| POST | `/tasks` | Create a task |
| PUT | `/tasks/{task_id}` | Update a task |
| DELETE | `/tasks/{task_id}` | Delete a task |
| GET | `/stats` | Get task statistics |
| GET | `/health` | Health check |
| POST | `/reset` | Reset demo data |

---

# 🔐 Authentication Flow

The Week 4 implementation adds authentication on top of the existing task API.

The authentication flow is:

```text
              User
                │
                ▼
        POST /auth/signup
                │
                ▼
          Supabase Auth
                │
                ▼
             Account
                │
                ▼
        POST /auth/login
                │
                ▼
       Access + Refresh Token
                │
                ▼
     Authorization: Bearer <JWT>
                │
                ▼
       FastAPI Protected Route
                │
                ▼
       Verify JWT with Supabase
                │
         ┌──────┴──────┐
         │             │
       Valid         Invalid
         │             │
         ▼             ▼
       200 OK         401
```

---

# 👤 1. User Signup

Endpoint:

```http
POST /auth/signup
```

Request:

```json
{
  "email": "user@example.com",
  "password": "password123"
}
```

A successful signup returns:

```text
201 Created
```

The user is created through Supabase Authentication.

---

# 🔑 2. User Login

Endpoint:

```http
POST /auth/login
```

Request:

```json
{
  "email": "user@example.com",
  "password": "password123"
}
```

Successful authentication returns:

```text
200 OK
```

The response contains authentication tokens, including:

- Access token
- Refresh token

The access token is used to access protected endpoints.

---

# 🛡️ 3. Protected Routes

Protected routes require an HTTP Authorization header.

Format:

```http
Authorization: Bearer <access_token>
```

For example:

```http
GET /protected/profile
Authorization: Bearer eyJ...
```

The API extracts the bearer token and verifies it with Supabase.

---

# 👤 4. Protected Profile

Endpoint:

```http
GET /protected/profile
```

Authentication:

```text
Required
```

A valid JWT allows the authenticated user's safe profile information to be returned.

The endpoint rejects:

- Missing token
- Malformed authorization
- Invalid token
- Expired token
- Tampered token

---

# 📋 5. Protected Tasks

Endpoint:

```http
GET /protected/tasks
```

Authentication:

```text
Required
```

The endpoint uses the same reusable authentication dependency as the protected profile route.

Additional protected task operations include:

```http
POST /protected/tasks
PUT /protected/tasks/{task_id}
DELETE /protected/tasks/{task_id}
```

---

# 🚪 6. Logout

Endpoint:

```http
POST /auth/logout
```

Authentication:

```text
Required
```

The authenticated session is ended through Supabase.

Successful logout returns:

```text
204 No Content
```

---

# 🌐 Public Information

Endpoint:

```http
GET /public/info
```

This endpoint does not require authentication.

It can be accessed without an Authorization header.

---

# 🚨 Authentication Error Handling

The API handles authentication failures using appropriate HTTP status codes.

## Missing access token

```text
401 Unauthorized
```

Example:

```json
{
  "error": "Access token required"
}
```

---

## Invalid or expired token

```text
401 Unauthorized
```

Example:

```json
{
  "error": "Invalid or expired token"
}
```

---

## Invalid login credentials

```text
401 Unauthorized
```

Example:

```json
{
  "error": "Invalid login credentials"
}
```

---

## Missing signup/login information

```text
400 Bad Request
```

---

# 🔒 JWT Verification

The API does not simply trust a token supplied by the client.

The bearer token is extracted from the Authorization header and verified through Supabase.

```text
Client
  │
  │ Authorization: Bearer <token>
  ▼
FastAPI
  │
  │ Extract token
  ▼
Authentication Dependency
  │
  │ Verify token
  ▼
Supabase Auth
  │
  ├── Valid ────────▶ Authenticated User
  │
  └── Invalid ──────▶ 401 Unauthorized
```

This protects private API resources from unauthorized access.

---

# ♻️ Reusable Authentication Dependency

Authentication logic is implemented as a reusable FastAPI dependency.

Instead of duplicating JWT verification code inside every protected endpoint, protected routes use the same authentication mechanism.

Conceptually:

```text
Reusable Auth Dependency
          │
     ┌────┼─────────┐
     │    │         │
     ▼    ▼         ▼
 Profile Tasks    Logout
```

This improves:

- Code reuse
- Maintainability
- Consistency
- Security
- Scalability

---

# 🧪 API Testing

The authentication implementation can be tested using either:

- Swagger UI
- cURL
- PowerShell
- REST clients

---

## Test 1 — Signup

```http
POST /auth/signup
```

Example request:

```json
{
  "email": "test@example.com",
  "password": "password123"
}
```

Expected:

```text
201 Created
```

---

## Test 2 — Login

```http
POST /auth/login
```

Example:

```json
{
  "email": "test@example.com",
  "password": "password123"
}
```

Expected:

```text
200 OK
```

Save the returned:

```text
access_token
```

---

## Test 3 — Protected route without token

```http
GET /protected/profile
```

Expected:

```text
401 Unauthorized
```

---

## Test 4 — Protected route with valid token

```http
GET /protected/profile
Authorization: Bearer <access_token>
```

Expected:

```text
200 OK
```

---

## Test 5 — Tampered token

Change one character in the JWT and send it again.

Expected:

```text
401 Unauthorized
```

This verifies that the server is actually validating the token.

---

## Test 6 — Logout

```http
POST /auth/logout
Authorization: Bearer <access_token>
```

Expected:

```text
204 No Content
```

---

# 🧪 Testing with PowerShell

PowerShell users can use `Invoke-RestMethod`.

### Signup

```powershell
Invoke-RestMethod `
  -Uri "http://localhost:8000/auth/signup" `
  -Method POST `
  -ContentType "application/json" `
  -Body '{"email":"test@example.com","password":"password123"}'
```

### Login

```powershell
Invoke-RestMethod `
  -Uri "http://localhost:8000/auth/login" `
  -Method POST `
  -ContentType "application/json" `
  -Body '{"email":"test@example.com","password":"password123"}'
```

### Public endpoint

```powershell
Invoke-RestMethod `
  -Uri "http://localhost:8000/public/info" `
  -Method GET
```

### Protected endpoint

Replace `<TOKEN>` with the access token returned by login.

```powershell
Invoke-RestMethod `
  -Uri "http://localhost:8000/protected/profile" `
  -Method GET `
  -Headers @{Authorization="Bearer <TOKEN>"}
```

---

# 📝 Task API Examples

## Create a task

```http
POST /tasks
Content-Type: application/json
```

```json
{
  "title": "Complete FastAPI assignment",
  "description": "Finish the backend internship task"
}
```

---

## Get all tasks

```http
GET /tasks
```

Optional query parameters:

```text
done
search
limit
offset
```

Examples:

```text
GET /tasks?done=true
GET /tasks?search=FastAPI
GET /tasks?limit=10&offset=0
```

---

## Get one task

```http
GET /tasks/1
```

---

## Update a task

```http
PUT /tasks/1
Content-Type: application/json
```

Example:

```json
{
  "title": "Complete backend assignment",
  "done": true
}
```

---

## Delete a task

```http
DELETE /tasks/1
```

Successful deletion returns:

```text
204 No Content
```

---

# 📊 Task Statistics

Endpoint:

```http
GET /stats
```

The statistics endpoint provides task completion information such as:

```json
{
  "total": 10,
  "completed": 3,
  "pending": 7,
  "completion_rate": 30.0
}
```

---

# ❤️ Health Check

Endpoint:

```http
GET /health
```

The health endpoint is used to verify that the API is running correctly.

It can also be used by container health checks.

---

# 🎨 Web Interface

The project also includes a browser-based task management interface.

File:

```text
index.html
```

The interface provides functionality such as:

- Create tasks
- View tasks
- Search tasks
- Filter completed/pending tasks
- Mark tasks as complete
- Delete tasks
- View task statistics
- Responsive interface
- Dark-themed UI

The frontend communicates with the FastAPI backend.

---

# 📈 Week-by-Week Development

## 🟢 Week 2 — FastAPI Task Management API

The project began as a RESTful task management API.

### Implemented

- FastAPI application
- Uvicorn server
- Task CRUD operations
- Pydantic validation
- HTTP status codes
- Search
- Filtering
- Pagination
- Statistics
- Health check
- Swagger UI
- ReDoc
- Browser-based task management interface

The initial version demonstrated the fundamentals of building a REST API using FastAPI.

---

# 🟡 Week 3 — Database & Docker

The API was then extended beyond simple in-memory task storage.

### Implemented

- SQLite persistence during the database development phase
- PostgreSQL integration
- psycopg PostgreSQL driver
- Database connection configuration
- Dockerfile
- Docker Compose
- PostgreSQL Docker container
- Persistent PostgreSQL volume
- Container health checks

The Week 3 version introduced persistent backend storage and containerized development.

---

# 🔴 Week 4 — Authentication & Security

The existing API was upgraded with user authentication and protected resources.

### Implemented

- Supabase Authentication
- Signup
- Login
- Logout
- Access tokens
- Refresh tokens
- JWT verification
- HTTP Bearer authentication
- Protected profile endpoint
- Protected task endpoints
- Public endpoint
- Reusable authentication dependency
- Invalid token handling
- Expired token handling
- Tampered token handling
- Swagger authentication
- Swagger Authorize functionality

The API now supports authenticated and unauthenticated resources.

---

# 🔄 Current Architecture

The current project combines the major backend components developed throughout the internship.

```text
                         CLIENT
                           │
                           ▼
                  ┌─────────────────┐
                  │    FastAPI      │
                  │     Server      │
                  └────────┬────────┘
                           │
              ┌────────────┼────────────┐
              │            │            │
              ▼            ▼            ▼
          Task API      Auth API    Public API
              │            │
              │            ▼
              │       Supabase Auth
              │            │
              │            ▼
              │        JWT Token
              │
              ▼
       PostgreSQL Database
```

---

# 🔐 Security Design

The project separates public and protected resources.

```text
PUBLIC
│
├── POST /auth/signup
├── POST /auth/login
└── GET  /public/info


PROTECTED
│
├── POST   /auth/logout
├── GET    /protected/profile
├── GET    /protected/tasks
├── POST   /protected/tasks
├── PUT    /protected/tasks/{id}
└── DELETE /protected/tasks/{id}
```

Protected resources require:

```http
Authorization: Bearer <JWT>
```

---

# 📦 Dependencies

The main Python dependencies include:

```text
FastAPI
Uvicorn
Pydantic
python-multipart
psycopg
python-dotenv
Supabase
GoTrue
HTTPX
python-jose
cryptography
PyJWT
```

Install them using:

```bash
pip install -r requirements.txt
```

---

# 🧰 Development Workflow

The project was developed incrementally using Git and GitHub.

The general workflow was:

```text
Develop
   ↓
Test locally
   ↓
Fix errors
   ↓
Run API
   ↓
Verify Swagger
   ↓
Commit changes
   ↓
Push to GitHub
```

Git was used to track the progression of the backend throughout the internship assignments.

---

# 📜 Git Development History

The repository contains commits corresponding to the progressive development of the project.

Current development progression includes:

```text
Complete Task Management API with web UI
        ↓
Upgrade Task API with SQLite persistence
        ↓
Complete Week 3 Docker PostgreSQL Task API
        ↓
Prepare Week 4 authentication release
        ↓
Week 4 documentation and finalization
```

The repository therefore demonstrates the evolution of the same application rather than separate unrelated projects.

---

# 🧹 Repository Hygiene

The repository intentionally excludes sensitive and unnecessary local-development files.

Ignored files include:

```text
.env
*.db
__pycache__/
*.pyc
.venv/
venv/
env/
```

The repository contains:

```text
.env.example
```

so that another developer can understand which environment variables are required without exposing actual credentials.

---

# 🚨 Important Security Notes

Never commit:

```text
.env
```

Never expose:

```text
SUPABASE_KEY
DATABASE_URL
```

when they contain real credentials.

Use:

```text
.env.example
```

for public documentation and setup instructions.

---

# 🐛 Troubleshooting

## Port 8000 already in use

Check which application is using the port and stop it, or run the API on another port.

Example:

```bash
uvicorn main:app --host 0.0.0.0 --port 8001
```

---

## Docker containers are not running

Make sure Docker Desktop is running.

Then:

```bash
docker compose up --build
```

---

## Check running containers

```bash
docker compose ps
```

---

## View API logs

```bash
docker compose logs api
```

---

## View PostgreSQL logs

```bash
docker compose logs postgres
```

---

## Stop containers

```bash
docker compose down
```

---

## Rebuild containers

```bash
docker compose up --build
```

---

# 📖 Useful Endpoints

Once the API is running:

| Resource | URL |
|---|---|
| API | http://localhost:8000 |
| Swagger | http://localhost:8000/docs |
| ReDoc | http://localhost:8000/redoc |
| Health | http://localhost:8000/health |
| Public Info | http://localhost:8000/public/info |

---

# 🎯 Learning Outcomes

This project demonstrates practical experience with:

### Backend Development

- REST API design
- FastAPI
- Request validation
- Response models
- HTTP methods
- HTTP status codes
- Error handling

### Databases

- Relational databases
- PostgreSQL
- Database persistence
- Database connections

### Authentication

- User authentication
- JWT
- Bearer authentication
- Token validation
- Protected endpoints
- Authentication dependencies

### DevOps

- Docker
- Docker Compose
- Multi-stage builds
- Container health checks
- Environment variables

### API Documentation

- OpenAPI
- Swagger UI
- ReDoc
- Interactive endpoint testing

### Version Control

- Git
- GitHub
- Incremental development
- Meaningful commits

---

# 🚀 Future Improvements

Possible future improvements include:

- Automated unit and integration tests
- Role-based access control
- Refresh-token endpoint
- Rate limiting
- Task ownership at the database level
- Task categories
- Task priorities
- Due dates
- Notifications
- Background tasks
- Production cloud deployment
- CI/CD pipeline
- Automated database migrations
- Improved frontend authentication
- Better monitoring and logging

---

# 👩‍💻 Author

## Shravani Rajendra Patil

Computer Engineering Student

GitHub:

https://github.com/shravani22patil

LinkedIn:

https://linkedin.com/in/shravani-patil-38791b286

---

# 📌 Repository

GitHub Repository:

https://github.com/shravani22patil/task-management-api

This repository contains the cumulative development of the Task Management API across the FlyRank Backend Internship assignments.

---

# 🏆 Internship Progression

```text
╔══════════════════════════════════════════════════╗
║              TASK MANAGEMENT API                 ║
╠══════════════════════════════════════════════════╣
║                                                  ║
║  WEEK 2                                          ║
║  FastAPI + REST + CRUD + Swagger + Web UI        ║
║                     ↓                            ║
║  WEEK 3                                          ║
║  PostgreSQL + Persistence + Docker               ║
║                     ↓                            ║
║  WEEK 4                                          ║
║  Supabase Auth + JWT + Protected Routes          ║
║                                                  ║
╚══════════════════════════════════════════════════╝
```

The result is a progressively developed backend application demonstrating the transition from a basic REST API to a database-backed, containerized and authenticated backend service.

---

## 📄 License

This project was developed as part of the **FlyRank Backend Internship**.

---

**Built with Python, FastAPI, PostgreSQL, Supabase, Docker and GitHub. 🚀**
