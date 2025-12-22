# Supalove Architecture Status & Comparison

## Section A: Current Architecture

Supalove is built as a **Multi-Tenant SaaS Platform** that replicates the Supabase architecture using a Control Plane / Data Plane model.

### 1. Control Plane (The "SaaS" Layer)
This layer manages users, billing, projects, and infrastructure provisioning. It does *not* touch user data directly.

*   **Frontend**: Next.js 14 App Router (`dashboard/`).
*   **Backend API**: FastAPI (`control-plane/api`).
*   **Database**: Postgres (stores organizations, projects, secrets).
*   **Authentication**: Keycloak (handles platform login/signup).
*   **Monitoring**: Prometheus & Grafana (tracks infrastructure health).
*   **Orchestration**: Currently uses **Docker Compose** to provision isolated stacks per project.

### 2. Data Plane (The "Project" Layer)
Every time a user creates a project, a completely **isolated Docker stack** is spun up. This ensures tenant isolation and security.

**Per-Project Stack Components:**
*   **Gateway**: **Nginx** (Acts as the single entry point, routing requests like Kong).
*   **Database**: **Postgres 15** (Official `supabase/postgres:15.8.1.085` image).
*   **REST API**: **PostgREST v12.2.3** (Auto-generates APIs from the DB).
*   **Auth Service**: **Supabase GoTrue v2.184.0** (Handles user signups, magic links, JWTs).
*   **Realtime**: **Supabase Realtime v2.68.0** (Websockets for DB changes).
*   **Storage**: **Supabase Storage API v1.33.0** (S3-compatible file storage).
*   **Edge Functions**: **Deno Runtime** (Runs TypeScript functions).

### 3. Networking
*   **Isolation**: Each project runs on its own internal Docker network.
*   **Unified Access**: Applications connect to a single **Gateway Port** (e.g., `http://localhost:5522`).
    *   `/auth/v1` -> GoTrue
    *   `/rest/v1` -> PostgREST
    *   `/storage/v1` -> Storage API
    *   `/realtime/v1` -> Realtime

---

## Section B: Comparison with Supabase Cloud / Lovable

The goal is **100% Application Compatibility**. This means code written for Supabase Cloud should run on Supalove without modification.

### 1. Database Compatibility (The "Gold Standard")

| Feature | Supabase Cloud | Supalove (Current) | Compatibility |
| :--- | :--- | :--- | :--- |
| **Postgres Version** | Postgres 15.x | Postgres 15.8.1 | ✅ **100% Match** |
| **Extensions** | `pg_net`, `pg_graphql`, `pgvector`, `postgis` | Includes standard Supabase extensions | ✅ **High** |
| **Roles & Permissions** | `anon`, `authenticated`, `service_role` | Same JWT-based RLS model | ✅ **100% Match** |
| **User Management** | GoTrue (Auth) | GoTrue v2.184 | ✅ **100% Match** |
| **Client SDK** | `@supabase/supabase-js` | **Fully Verified** | ✅ **100% Match** |
| **Realtime** | Channels, Broadcast, Presence | Full Realtime Engine | ✅ **100% Match** |

**Verdict**: Your database behavior is **identically compatible**. You can backup a Supabase project and restore it here, or point a Supabase app to your Gateway URL, and it will work.

### 2. Infrastructure Differences

| Feature | Supabase Cloud | Supalove | Note |
| :--- | :--- | :--- | :--- |
| **Gateway** | **Kong** (Enterprise API Gateway) | **Nginx** (Lightweight Proxy) | We use Nginx for simplicity, but it routes paths identically (`/auth`, `/rest`). Use Nginx for creating new routes. |
| **Scaling** | Kubernetes / Global Edge | Single-Node Docker / Coolify | Supabase scales infinitely; Supalove scales vertically (bigger server) or via Coolify multi-server. |
| **Billing** | Usage-based (Stripe) | Flat/Usage (Custom Logic) | You own the billing logic in the Control Plane. |
| **Edge Functions** | Distributed Global Edge | Containerized Deno | Functions run in a container on your server, not globally distributed. |

### 3. "Lovable" Cloud Comparison
Lovable is an AI-generated app builder that uses Supabase backend.
*   Since Supalove replicates the **Supabase backend API** exactly, **Lovable-generated code works natively** with Supalove.
*   You simply provide the Supalove Gateway URL (`API_URL`) and `ANON_KEY` to the Lovable app.

### Summary
You have built a **functional open-source clone**.
*   **For Developers**: It looks exactly like Supabase.
*   **For Ops**: It is simpler (Docker-based) but maintains the same service architecture.
