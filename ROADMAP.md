# Roadmap

## Next Steps

1. Persist projects in control-plane DB
2. Inject secrets (JWT, DB passwords)
3. Replace shell scripts with Coolify API
4. Add Auth service
5. Add Storage
6. Add Realtime
7. Add Dashboard UI

----------------------

# Supabase Cloud Clone – Reference Architecture

This document describes a **production-grade, open-source architecture** that replicates **Supabase Cloud behavior**:

- Project-per-tenant

- Strong isolation

- Automated provisioning

- Managed APIs (DB, Auth, Storage, Realtime)

This is a **control-plane / data-plane** architecture similar to Supabase, Vercel, Railway, and Render.

---

## 1. Core Concept (Very Important)

Supabase Cloud is **NOT just Postgres**.  
It is:

- A **Control Plane** (project creation, secrets, billing, domains)

- A **Data Plane** (actual databases & services)

Your clone must separate these two.

```
┌──────────────────────────┐
│      CONTROL PLANE       │  ← Your SaaS app
└──────────┬───────────────┘
           │
┌──────────▼───────────────┐
│        DATA PLANE        │  ← Per-project stacks
└──────────────────────────┘
```

---

## 2. High-Level Architecture

```
User
 │
 ▼
Web Dashboard (Next.js)
 │
 ▼
Control Plane API (FastAPI)
 │
 ├── Project Provisioner
 ├── Secrets Manager
 ├── Domain Manager
 ├── Billing / Limits
 └── Audit Logs
 │
 ▼
Infrastructure Layer
 │
 ├── Docker / Coolify / Nomad
 ├── PostgreSQL Clusters
 ├── Keycloak (Auth)
 ├── MinIO (Storage)
 └── Realtime Services
```

---

## 3. Control Plane (Your "Supabase Dashboard")

### Tech Stack

- **Frontend**: Next.js 14 + App Router

- **Backend**: FastAPI

- **DB**: Postgres (control metadata only)

- **Auth**: Keycloak (admin realm)

### Control Plane Database Schema

```
organizations
projects
project_secrets
project_domains
project_usage
project_audit_logs
```

Each project row represents **ONE Supabase-like project**.

---

## 4. Project Lifecycle (Critical Flow)

### When user clicks: "Create Project"

```
1. Validate plan / limits
2. Generate project_id
3. Generate JWT_SECRET
4. Create Postgres database
5. Create Auth realm
6. Create Storage bucket
7. Deploy project stack
8. Assign subdomain
9. Return API keys
```

This is **exactly what Supabase Cloud does**.

---

## 5. Data Plane – Per Project Stack

Each project gets **isolated infrastructure**.

```
Project Stack
├── PostgreSQL (DB-per-project)
├── PostgREST (REST API)
├── Realtime
├── Storage API
├── Auth Adapter
└── API Gateway (Traefik / Kong)
```

### Deployment Model

- Docker Compose (simple)

- OR Kubernetes (scalable)

- OR Coolify apps (recommended for you)

---

## 6. Database Layer (Project Isolation)

### Recommended

```
Postgres Cluster
├── project_a_db
├── project_b_db
├── project_c_db
```

Isolation:

- Separate DB

- Separate DB users

- Separate passwords

This is **stronger than schema-per-tenant**.

---

## 7. Authentication (Supabase Auth Replacement)

### Keycloak Strategy

```
Keycloak
├── admin-realm (control plane)
├── project-a-realm
├── project-b-realm
```

Each project:

- Own users

- Own JWT issuer

- Own roles

JWT claims:

```
{
  "project_id": "proj_xxx",
  "role": "authenticated"
}
```

---

## 8. API Layer

### Option A – PostgREST (Supabase-like)

- Auto REST from Postgres

- RLS-based security

### Option B – Hasura

- GraphQL

- Role-based permissions

### Option C – FastAPI

- Full custom APIs

You can **mix them**.

---

## 9. Storage Layer

### MinIO Structure

```
minio
├── project-a-bucket
├── project-b-bucket
```

Each project:

- Separate bucket

- Separate access keys

Storage API enforces project_id.

---

## 10. Realtime Layer

Options:

- Supabase Realtime (self-hosted)

- Postgres LISTEN/NOTIFY

- WebSocket Gateway

Realtime subscribes **per database**.

---

## 11. Networking & Domains

```
api.project-a.yourcloud.com
api.project-b.yourcloud.com
```

Routing:

- Traefik / Nginx

- Route by subdomain → project stack

TLS:

- Wildcard certs (Cloudflare / Let's Encrypt)

---

## 12. Secrets Management

Each project has:

- JWT_SECRET

- DB_PASSWORD

- STORAGE_KEYS

Stored in:

- Control Plane DB (encrypted)

- Injected as env vars

---

## 13. Billing & Quotas (Optional but Realistic)

Track per project:

- DB size

- API requests

- Storage usage

- Realtime connections

Enforce:

- Rate limits

- DB size caps

---

## 14. Deployment with Coolify (Your Best Choice)

```
Coolify
├── Project Stack A
├── Project Stack B
├── Control Plane
```

Automation:

- Coolify API

- Docker templates

- Env injection

---

## 15. Scaling Strategy

### Small Scale

- 1 VPS

- Many project stacks

### Medium Scale

- Dedicated DB server

- Separate app server

### Large Scale

- Kubernetes

- DB clusters

- Dedicated Keycloak

---

## 16. What You Achieve

✅ True project-per-tenant  
✅ Supabase Cloud behavior  
✅ Full open-source  
✅ Vendor independence

This is **how Supabase is actually built internally**.

---

## 17. Recommended Stack for YOU

Based on your background:

- Control Plane: Next.js + FastAPI

- DB: Postgres (DB-per-project)

- Auth: Keycloak

- Storage: MinIO

- Infra: Coolify

---

## 18. Next Steps

If you want, next we can:

- Draw **sequence diagrams**

- Write **project provisioning code**

- Create **Coolify templates**

- Design **tenant-aware RLS**

- Plan **migration from Supabase**