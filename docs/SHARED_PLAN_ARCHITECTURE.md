# Shared Plan Architecture

This document explains the architecture of the **Shared Plan** feature in Supalove.

## Overview

Supalove supports two project plans:

| Plan | Description | Use Case |
|------|-------------|----------|
| **Shared (Free)** | Multiple projects share a single infrastructure | Development, small projects |
| **Dedicated (Premium)** | Each project gets its own isolated Docker stack | Production workloads |

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────────────┐
│                           CONTROL PLANE                                  │
│  ┌─────────────┐  ┌─────────────────┐  ┌───────────────────────┐       │
│  │  Dashboard  │  │   FastAPI API   │  │   Control Plane DB    │       │
│  └─────────────┘  └─────────────────┘  └───────────────────────┘       │
└─────────────────────────────────────────────────────────────────────────┘
                              │
           ┌──────────────────┴───────────────────┐
           │                                      │
           ▼                                      ▼
┌─────────────────────────────┐    ┌──────────────────────────────────────┐
│     DEDICATED DATA PLANE    │    │        SHARED DATA PLANE             │
│  ┌─────────────────────────┐│    │  ┌────────────────────────────────┐  │
│  │    Project A Stack      ││    │  │      Shared Postgres Cluster   │  │
│  │  ┌───────┐ ┌─────────┐  ││    │  │  ┌──────┐ ┌──────┐ ┌──────┐   │  │
│  │  │Postgres│ │PostgREST│  ││    │  │  │DB: A │ │DB: B │ │DB: C │   │  │
│  │  └───────┘ └─────────┘  ││    │  │  └──────┘ └──────┘ └──────┘   │  │
│  │  ┌───────┐ ┌─────────┐  ││    │  └────────────────────────────────┘  │
│  │  │ Auth  │ │ Storage │  ││    │                                      │
│  │  └───────┘ └─────────┘  ││    │  ┌────────────────────────────────┐  │
│  └─────────────────────────┘│    │  │       Routing Gateway          │  │
│  ┌─────────────────────────┐│    │  │   (FastAPI Proxy / Nginx)      │  │
│  │    Project B Stack      ││    │  └────────────────────────────────┘  │
│  │       (isolated)        ││    │                                      │
│  └─────────────────────────┘│    │  ┌────────────────────────────────┐  │
└─────────────────────────────┘    │  │  Shared Services (Auth, API,   │  │
                                   │  │  Storage, Realtime, Functions) │  │
                                   │  └────────────────────────────────┘  │
                                   └──────────────────────────────────────┘
```

## Shared Plan Flow

### 1. Project Creation

When a user creates a **Shared** project:

1. Control Plane creates a project record with `plan = "shared"`
2. `shared_provisioning_service.py` creates a new database in the shared Postgres cluster
3. Supabase migrations are applied to the new database
4. JWT secrets are generated and stored
5. **No Docker containers are spawned**

### 2. Request Routing

The **Routing Gateway** handles multi-tenancy:

1. Client sends request with `X-Project-Id: abc123` header
2. Gateway looks up project configuration from Control Plane
3. Routes request to shared services with correct database context
4. Services connect to the project-specific database

### 3. Data Isolation

Each shared project has:
- ✅ Separate PostgreSQL database
- ✅ Separate JWT secrets
- ✅ Separate storage namespace
- ❌ Shared compute resources (PostgREST, Auth, etc.)

## Key Files

| File | Purpose |
|------|---------|
| `control-plane/api/src/models/project.py` | Project model with `plan`, `backend_type`, `db_name` |
| `control-plane/api/src/services/shared_provisioning_service.py` | Database creation & migrations |
| `data-plane/shared/docker-compose.yml` | Shared infrastructure stack |
| `data-plane/shared/routing-proxy/main.py` | Multi-tenant routing gateway |

## Starting the Shared Stack

```bash
cd data-plane/shared
cp .env.example .env
# Edit .env with your secrets
docker compose up -d
```

## API Usage

### Creating a Shared Project

```bash
curl -X POST http://localhost:8000/api/v1/projects \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"name": "my-project", "plan": "shared"}'
```

### Accessing a Shared Project

```bash
curl http://localhost:8080/projects/abc123/rest/v1/your_table \
  -H "Authorization: Bearer $ANON_KEY"
```
