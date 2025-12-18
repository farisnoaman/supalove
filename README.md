# Supabase Cloud Clone – v1 Starter Repo

This is a **minimal, correct v1** repository to get your first milestone working:

> **POST /projects → project backend is provisioned and reachable via subdomain**

Everything here directly supports that goal.

---

## 📁 Repository Structure

```
supabase-cloud-clone/
├── control-plane/
│   ├── api/
│   │   ├── src/
│   │   │   ├── api/
│   │   │   │       └── v1/
│   │   │   │           └── projects.py
│   │   │   ├── core/
│   │   │   │   ├── config.py
│   │   │   │   └── database.py
│   │   │   ├── services/
│   │   │   │   ├── project_service.py
│   │   │   │   └── provisioning_service.py
│   │   │   └── main.py
│   │   └── Dockerfile
│   └── migrations/
│       └── 001_init.sql
│
├── data-plane/
│   └── project-template/
│       ├── docker-compose.yml
│       ├── postgres/
│       │   └── init.sql
│       ├── auth/
│       │   └── env.example
│       ├── storage/
│       │   └── env.example
│       ├── realtime/
│       │   └── env.example
│       └── functions/
│           └── Dockerfile
│
├── infra/
│   ├── coolify/
│   │   └── project-template.json
│   └── traefik/
│       └── traefik.yml
│
├── scripts/
│   ├── create-project.sh
│   └── delete-project.sh
│
├── docker-compose.yml
├── README.md
└── ROADMAP.md
```

---

## 🧠 control-plane (FastAPI)

### `main.py`

```python
from fastapi import FastAPI
from api.v1.projects import router as projects_router

app = FastAPI(title="Supabase Cloud Clone")

app.include_router(projects_router, prefix="/v1/projects")
```

### `projects.py`

```python
from fastapi import APIRouter
from services.project_service import create_project

router = APIRouter()

@router.post("/")
def create():
    return create_project()
```

### `project_service.py`

```python
import uuid
from services.provisioning_service import provision_project


def create_project():
    project_id = uuid.uuid4().hex[:16]
    provision_project(project_id)
    return {
        "project_id": project_id,
        "api_url": f"https://{project_id}.api.yourdomain.com"
    }
```

### `provisioning_service.py`

```python
import subprocess


def provision_project(project_id: str):
    subprocess.run([
        "bash",
        "scripts/create-project.sh",
        project_id
    ], check=True)
```

---

## 🧱 data-plane (Project Template)

### `docker-compose.yml` (simplified)

```yaml
version: "3.9"
services:
  postgres:
    image: postgres:15
    environment:
      POSTGRES_PASSWORD: postgres
    volumes:
      - postgres_data:/var/lib/postgresql/data

  api:
    image: postgrest/postgrest
    depends_on:
      - postgres

volumes:
  postgres_data:
```

This file will later expand to:

* Auth
* Storage
* Realtime
* Functions

But **do NOT add them yet**.

---

## ⚙️ infra (Coolify / Traefik)

### `project-template.json` (conceptual)

```json
{
  "name": "supabase-project",
  "source": "./data-plane/project-template",
  "domains": ["{project_id}.api.yourdomain.com"]
}
```

---

## 🛠 scripts

### `create-project.sh`

```bash
#!/bin/bash
PROJECT_ID=$1

cp -r data-plane/project-template /tmp/project-$PROJECT_ID
cd /tmp/project-$PROJECT_ID

docker compose up -d
```

---

## ✅ First Milestone (CRITICAL)

When this works:

```bash
curl -X POST http://localhost:8000/v1/projects
```

And you get:

```json
{
  "project_id": "abc123...",
  "api_url": "https://abc123.api.yourdomain.com"
}
```

👉 **YOU HAVE WON**

Everything else is iteration.

---

## 🗺️ ROADMAP (Next Steps)

1. Persist projects in control-plane DB
2. Inject secrets (JWT, DB passwords)
3. Replace shell scripts with Coolify API
4. Add Auth service
5. Add Storage
6. Add Realtime
7. Add Dashboard UI

---

## 🧠 Final Guidance

* Do not optimize early
* Do not add multi-cloud
* Do not add Kubernetes yet

**One project. One click. One success.**
--------------------------------
## 🚀 Deployment Architecture
🎉 **Excellent — this is a BIG milestone**

You now have a **working control plane**:

```
curl → FastAPI → create_project() → response
```

This is exactly how Supabase Cloud starts internally.

---

# ✅ STEP 2 — Persist Projects (Control-Plane Database)

Right now, projects are **ephemeral**.
If you restart FastAPI → all projects are forgotten.

In this step we will:

> **Store projects in a control-plane database**
> (NOT project databases — this is platform metadata)




---

## 2️⃣.3 Add Postgres (local dev)

At repo root, update **top-level** `docker-compose.yml`:

📍 `supabase_lovable_cloud_clone/docker-compose.yml`

```yaml
version: "3.9"

services:
  control-plane-db:
    image: postgres:15
    environment:
      POSTGRES_USER: platform
      POSTGRES_PASSWORD: platform
      POSTGRES_DB: control_plane
    ports:
      - "5433:5432"
    volumes:
      - control_plane_data:/var/lib/postgresql/data

volumes:
  control_plane_data:
```

Start it:

```bash
docker compose up -d
```

Verify:

```bash
docker ps
```

---

## 2️⃣.4 Add DB Dependencies

Inside your venv:

```bash
pip install sqlalchemy psycopg2-binary
```

Update `requirements.txt`:

```txt
fastapi
uvicorn
sqlalchemy
psycopg2-binary
```

---

## 2️⃣.5 Create Database Connection

📍 `control-plane/api/src/core/database.py`

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://platform:platform@localhost:5433/control_plane"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()
```

---

## 2️⃣.6 Create Project Model

📍 `control-plane/api/src/models/project.py`

```python
from sqlalchemy import Column, String, DateTime
from datetime import datetime
from core.database import Base

class Project(Base):
    __tablename__ = "projects"

    id = Column(String, primary_key=True, index=True)
    status = Column(String, default="provisioning")
    created_at = Column(DateTime, default=datetime.utcnow)
```

---

## 2️⃣.7 Create Tables Automatically (v1 shortcut)

📍 `control-plane/api/src/main.py`

```python
from fastapi import FastAPI
from api.v1.projects import router as projects_router
from core.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Supabase Cloud Clone")
app.include_router(projects_router, prefix="/v1/projects")
```

⚠️ Later we’ll replace this with Alembic.

---

## 2️⃣.8 Save Project When Created

📍 `services/project_service.py`

```python
import uuid
from sqlalchemy.orm import Session
from core.database import SessionLocal
from models.project import Project
from services.provisioning_service import provision_project

def create_project():
    project_id = uuid.uuid4().hex[:12]

    db: Session = SessionLocal()
    project = Project(id=project_id, status="provisioning")
    db.add(project)
    db.commit()

    provision_project(project_id)

    project.status = "running"
    db.commit()

    return {
        "project_id": project_id,
        "status": project.status,
        "api_url": f"http://localhost:{project_id}"
    }
```

---

## 2️⃣.9 Restart & Test Again

Restart API:

```bash
uvicorn main:app --reload --port 8000
```

Test:

```bash
curl -X POST http://localhost:8000/v1/projects
```

---

## 2️⃣.🔟 Verify Data Is Stored

Connect to DB:

```bash
docker exec -it <postgres_container_id> psql -U platform -d control_plane
```

Then:

```sql
SELECT * FROM projects;
```

You should see your project 🎉

---

---


---