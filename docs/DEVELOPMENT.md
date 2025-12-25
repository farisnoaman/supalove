# Development Guide

This guide covers setting up a local development environment for Supalove.

## Prerequisites

- **Docker** & **Docker Compose** (v2+)
- **Node.js** 20+ and npm
- **Python** 3.12+
- **Git**

---

## Initial Setup

### 1. Clone Repository

```bash
git clone https://github.com/farisnoaman/supalove.git
cd supalove
```

### 2. Start Control Plane Services

```bash
# Start PostgreSQL, Keycloak, and MinIO
docker compose up -d
```

Verify services are running:
```bash
docker ps
```

Expected containers:
- `control-plane-db` (PostgreSQL on port 5433)
- `keycloak` (Auth on port 8080)
- `minio` (S3 on ports 9000/9001)

---

## Backend Development (FastAPI)

### 1. Setup Python Environment

```bash
cd control-plane/api
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or: venv\Scripts\activate  # Windows
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Start Development Server

```bash
uvicorn src.main:app --reload --port 8000
```

**Available URLs:**
- API: http://localhost:8000
- Swagger Docs: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### 4. Running Tests

```bash
pytest
```

---

## Frontend Development (Next.js)

### 1. Install Dependencies

```bash
cd dashboard
npm install
```

### 2. Configure Environment

Create `.env.local`:
```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

### 3. Start Development Server

```bash
npm run dev
```

**Available at:** http://localhost:3000

---

## Project Structure

### Backend (`control-plane/api/src/`)

```
src/
├── api/v1/           # Route handlers
│   ├── auth.py       # Login/register
│   ├── projects.py   # Project CRUD
│   ├── database.py   # SQL execution
│   └── ...
├── services/         # Business logic
│   ├── project_service.py
│   ├── provisioning_local.py
│   └── secrets_service.py
├── models/           # SQLAlchemy ORM
│   ├── project.py
│   ├── user.py
│   └── ...
├── core/             # Config & utilities
│   ├── database.py
│   └── security.py
└── main.py           # FastAPI app
```

### Frontend (`dashboard/src/`)

```
src/
├── app/              # Next.js App Router
│   ├── login/
│   ├── org/[orgId]/
│   ├── projects/[id]/
│   └── ...
├── components/       # React components
│   ├── ui/           # Shadcn components
│   └── ...
├── hooks/            # Custom hooks
└── lib/              # Utilities
```

---

## Database Migrations

Currently using SQLAlchemy auto-create:
```python
Base.metadata.create_all(bind=engine)
```

For production, consider Alembic:
```bash
alembic revision --autogenerate -m "description"
alembic upgrade head
```

---

## Creating a New API Endpoint

### 1. Create Router

```python
# src/api/v1/my_feature.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import get_db

router = APIRouter()

@router.get("/")
def list_items(db: Session = Depends(get_db)):
    return {"items": []}

@router.post("/")
def create_item(data: dict, db: Session = Depends(get_db)):
    return {"created": True}
```

### 2. Register in main.py

```python
from api.v1.my_feature import router as my_feature_router

app.include_router(my_feature_router, prefix="/api/v1/my-feature", tags=["My Feature"])
```

---

## Docker Development

### Build API Image

```bash
docker build -t supalove-api -f control-plane/api/Dockerfile .
```

### Build Dashboard Image

```bash
docker build -t supalove-dashboard -f dashboard/Dockerfile dashboard/
```

### Full Stack (Production-like)

```bash
docker compose -f docker-compose.coolify.yml up --build
```

---

## Debugging

### API Logs

```bash
# If running via uvicorn directly
# Logs appear in terminal

# If running via Docker
docker logs -f <container_id>
```

### Database Access

```bash
docker exec -it <postgres_container> psql -U platform -d control_plane
```

### Project Container Logs

```bash
# Find project containers
docker ps --filter "name=<project_id>"

# View logs
docker logs -f <project_id>-postgres-1
```

---

## Code Style

### Python (Backend)

```bash
# Linting
ruff check .

# Formatting
ruff format .
```

### TypeScript (Frontend)

```bash
npm run lint
```

---

## Environment Variables Reference

### Backend

| Variable | Description | Default |
|----------|-------------|---------|
| `DATABASE_URL` | Control plane DB | `postgresql://platform:platform@localhost:5433/control_plane` |
| `ALLOWED_ORIGINS` | CORS origins | `http://localhost:3000` |

### Frontend

| Variable | Description | Required |
|----------|-------------|----------|
| `NEXT_PUBLIC_API_URL` | Backend API URL | Yes |

---

## Troubleshooting

### Port Already in Use

```bash
# Find process
lsof -i :8000

# Kill it
kill -9 <PID>
```

### Docker Permission Issues

```bash
sudo usermod -aG docker $USER
# Then logout and login
```

### Database Connection Failed

1. Check Docker is running: `docker ps`
2. Check connection string matches docker-compose ports
3. Restart containers: `docker compose restart`
