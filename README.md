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
