# Shared Projects Architecture & Management

## Overview

Supalove supports two types of projects:

1. **Dedicated Projects**: Each project gets its own isolated Docker containers for all services
2. **Shared Projects**: Multiple projects share common infrastructure for cost efficiency

This document explains how shared projects work and how they're managed.

---

## Architecture Comparison

### Dedicated Project Architecture

```
Project A                    Project B
┌─────────────────┐         ┌─────────────────┐
│ PostgreSQL:5500 │         │ PostgreSQL:5501 │
│ Auth:9000       │         │ Auth:9001       │
│ API:3000        │         │ API:3001        │
│ Storage:5000    │         │ Storage:5001    │
│ Realtime:4000   │         │ Realtime:4001   │
│ Gateway:8080    │         │ Gateway:8081    │
└─────────────────┘         └─────────────────┘
```

Each project has completely separate containers and ports.

### Shared Project Architecture

```
                   Shared Infrastructure
         ┌─────────────────────────────────────┐
         │   PostgreSQL:5435                   │
         │   ├─ Database: postgres (control)   │
         │   ├─ Database: project_abc123       │
         │   └─ Database: project_xyz789       │
         │                                      │
         │   Shared Gateway:8083                │
         │   Shared Auth:9999                   │
         │   Shared API (PostgREST)            │
         │   Shared Storage                     │
         │   Shared Realtime                    │
         └─────────────────────────────────────┘
                    ▲         ▲
                    │         │
            Project A     Project B
```

Multiple projects share the same service containers but are isolated at the database level.

---

## Database Isolation

### How It Works

**Shared PostgreSQL Instance:**
- Single PostgreSQL container running on port 5435 (default)
- Contains one "default" database (`postgres`) for control/shared schemas
- Each project gets its own isolated database: `project_{project_id}`

**Example:**
```
PostgreSQL Container (Port 5435)
├─ postgres (default database - used by shared services)
├─ project_abc123 (Project A's database)
│  ├─ auth schema (users, sessions)
│  ├─ public schema (user tables)
│  └─ storage schema (buckets, objects)
└─ project_xyz789 (Project B's database)
   ├─ auth schema
   ├─ public schema  
   └─ storage schema
```

**Key Points:**
- Each project database is completely isolated
- Projects cannot access each other's data
- Each project has its own database user: `project_{project_id}_user`
- Connection isolation is enforced at the PostgreSQL level

### SQL Editor Isolation

When you run SQL in the SQL editor:

1. Frontend calls: `/api/v1/projects/{project_id}/sql`
2. Backend retrieves project-specific secrets (DB_PORT, POSTGRES_DB, POSTGRES_USER)
3. Connects to: `postgresql://project_abc123_user:password@localhost:5435/project_abc123`
4. SQL executes **only** in that project's database

**Verification:**
```sql
-- Run in Project A
SELECT current_database(), current_user;
-- Returns: project_abc123, project_abc123_user

-- Run in Project B  
SELECT current_database(), current_user;
-- Returns: project_xyz789, project_xyz789_user
```

---

## Shared Services

### 1. Shared PostgreSQL (`shared-postgres`)

**Container:** `supalove_shared_postgres`
**Image:** `supabase/postgres:15.8.1.085`
**Port:** 5435 (host) → 5432 (container)

**Purpose:** 
- Hosts all shared project databases
- Each project gets isolated database

**Environment:**
```yaml
POSTGRES_USER: postgres
POSTGRES_PASSWORD: ${SHARED_POSTGRES_PASSWORD}
POSTGRES_DB: postgres
```

---

### 2. Shared Gateway (`shared-gateway-v3`)

**Container:** `supalove_shared_gateway_v3`
**Port:** 8083

**Purpose:**
- Routes API requests to correct project database
- Switches database context based on project ID in request
- Provides multi-tenant request routing

**How It Works:**
1. Receives request with project ID (e.g., `/projects/abc123/rest/v1/users`)
2. Extracts project ID from URL
3. Queries Control Plane API for project configuration
4. Dynamically sets PostgreSQL search_path or connection
5. Forwards request to shared services with correct context

**Environment:**
```yaml
CONTROL_PLANE_URL: http://host.docker.internal:8000
SHARED_POSTGRES_HOST: shared-postgres
SHARED_POSTGRES_USER: postgres
SHARED_POSTGRES_PASSWORD: ${SHARED_POSTGRES_PASSWORD}
```

---

### 3. Shared Auth Service (`shared-auth`)

**Container:** `supalove_shared_auth`
**Image:** `supabase/gotrue:v2.184.0`
**Port:** 9999

**Purpose:**
- Provides authentication for all shared projects
- Multi-tenant GoTrue compatible API

**Multi-Tenancy:**
- Each project's users are stored in their own database
- JWT tokens are signed with project-specific secrets
- Auth endpoints: `/projects/{project_id}/auth/v1/*`

**Custom Implementation:**
Located in: `control-plane/api/src/api/v1/shared_auth.py`

**Key Features:**
- Compatible with Supabase JS Client
- Project-specific database connections
- Per-project JWT secrets
- Bcrypt password hashing

**Endpoints:**
```
POST /projects/{project_id}/auth/v1/signup
POST /projects/{project_id}/auth/v1/token (login)
GET  /projects/{project_id}/auth/v1/user
POST /projects/{project_id}/auth/v1/logout
```

---

### 4. Shared API (`shared-api`)

**Container:** `supalove_shared_api`
**Image:** `postgrest/postgrest:v12.2.3`

**Purpose:**
- PostgREST API for database access
- Routed through gateway for multi-tenancy

**Database Switching:**
- Gateway handles database context switching
- Each request operates on correct project database

---

### 5. Shared Storage (`shared-storage`)

**Container:** `supalove_shared_storage`
**Image:** `supabase/storage-api:v1.33.0`

**Purpose:**
- File storage for all shared projects
- Multi-tenant file isolation

**Storage:**
- Files stored in shared volume
- Database metadata in project-specific database
- RLS policies enforce isolation

---

### 6. Shared Realtime (`shared-realtime`)

**Container:** `supalove_shared_realtime`
**Image:** `supabase/realtime:v2.68.0`

**Purpose:**
- WebSocket connections for real-time updates
- Listens to PostgreSQL replication

**Multi-Tenancy:**
- Connections routed by project ID
- Subscription filters by project database

---

## Project Provisioning

### Creating a Shared Project

**Flow:**

```mermaid
graph TD
    A[User Creates Project] --> B[Control Plane API]
    B --> C[Generate Project Secrets]
    C --> D[Create Database in Shared Postgres]
    D --> E[Initialize Auth Schema]
    E --> F[Set Up Storage Schema]
    F --> G[Update Project Status: Running]
    G --> H[Project Ready]
```

**Code Location:** `control-plane/api/src/services/provisioning_local.py`

**Secrets Generation:**

When plan = "shared":
```python
db_name = f"project_{project_id}"
db_user = f"{db_name}_user"
db_port = 5435  # Shared PostgreSQL port
jwt_secret = SHARED_JWT_SECRET  # Global shared secret
```

For dedicated projects:
```python
db_name = "postgres"
db_user = "postgres"
db_port = find_free_port(5500)  # Unique port
jwt_secret = generate_random_secret()  # Project-specific
```

### Database Creation

**Location:** Initialization happens in shared PostgreSQL

**Schema Setup:**
```sql
-- Create project database
CREATE DATABASE project_abc123;

-- Create project user
CREATE USER project_abc123_user WITH PASSWORD 'secret';

-- Grant permissions
GRANT ALL PRIVILEGES ON DATABASE project_abc123 TO project_abc123_user;

-- Inside project database:
\c project_abc123

-- Create schemas
CREATE SCHEMA auth;
CREATE SCHEMA storage;
CREATE SCHEMA public;

-- Initialize auth tables
CREATE TABLE auth.users (...);
CREATE TABLE auth.sessions (...);

-- Initialize storage tables
CREATE TABLE storage.buckets (...);
CREATE TABLE storage.objects (...);
```

---

## Request Routing

### API Request Flow

**Example: Fetching users from Project A**

```
1. Client Request:
   GET https://localhost:8083/projects/abc123/rest/v1/users
   Authorization: Bearer {project_a_jwt}

2. Shared Gateway receives request
   ├─ Extracts project_id: "abc123"
   ├─ Queries Control Plane for project config
   └─ Gets database name: "project_abc123"

3. Gateway modifies request for PostgREST
   ├─ Adds header: X-Database-Name: project_abc123
   └─ Forwards to shared-api:3000

4. PostgREST (shared-api)
   ├─ Connects to project_abc123 database
   ├─ Validates JWT with project's secret
   ├─ Queries: SELECT * FROM public.users
   └─ Returns results

5. Response flows back to client
```

### Authentication Flow

**Example: Login to Project A**

```
1. Client Request:
   POST /projects/abc123/auth/v1/token
   Body: {"email": "user@example.com", "password": "secret"}

2. Control Plane handles (shared_auth.py)
   ├─ Extracts project_id: "abc123"
   ├─ Fetches project secrets (DB connection, JWT secret)
   └─ Connects to database: project_abc123

3. Verify credentials
   ├─ Query: SELECT * FROM auth.users WHERE email = ?
   ├─ Verify password hash
   └─ Generate JWT with project's JWT_SECRET

4. Return tokens
   {
     "access_token": "eyJ...",
     "refresh_token": "...",
     "user": {...}
   }
```

---

## Management

### Starting Shared Infrastructure

**Command:**
```bash
cd data-plane/shared
docker compose up -d
```

**Services Started:**
- shared-postgres
- shared-gateway-v3
- shared-auth
- shared-api
- shared-storage
- shared-realtime

### Monitoring

**Check Service Health:**
```bash
docker ps | grep supalove_shared
```

**View Logs:**
```bash
# All services
docker compose logs -f

# Specific service
docker compose logs -f shared-postgres
docker compose logs -f shared-gateway-v3
```

**Database Access:**
```bash
# Connect to shared PostgreSQL
docker exec -it supalove_shared_postgres psql -U postgres

# List all databases
\l

# Connect to project database
\c project_abc123

# View tables
\dt auth.*
\dt public.*
```

### Debugging

**Verify Database Isolation:**
```sql
-- Inside PostgreSQL container
psql -U postgres

-- List all databases
SELECT datname FROM pg_database WHERE datname LIKE 'project_%';

-- Check database sizes
SELECT pg_database.datname, pg_size_pretty(pg_database_size(pg_database.datname)) AS size
FROM pg_database
WHERE datname LIKE 'project_%'
ORDER BY pg_database_size(pg_database.datname) DESC;
```

**Check Connection Counts:**
```sql
SELECT datname, count(*) as connections 
FROM pg_stat_activity 
GROUP BY datname;
```

---

## Cost Efficiency

### Resource Comparison

**Dedicated Project (per project):**
- PostgreSQL: ~100-200 MB RAM
- Auth: ~50 MB RAM
- API: ~30 MB RAM
- Storage: ~50 MB RAM
- Realtime: ~100 MB RAM
- **Total per project: ~330-430 MB RAM**

**Shared Infrastructure (for 10 projects):**
- PostgreSQL: ~300 MB RAM (handles all projects)
- Services: ~230 MB RAM (shared)
- **Total: ~530 MB RAM**
- **Per project: ~53 MB RAM** (10x reduction!)

### Scaling

**Vertical Scaling:**
- Increase PostgreSQL container resources
- More CPU/RAM for database operations

**Horizontal Scaling:**
- Multiple shared PostgreSQL instances (sharding)
- Cluster table in Control Plane tracks which projects are on which cluster
- Load balancing across gateway instances

---

## Security Considerations

### Database Isolation

✅ **Strong Isolation:**
- Separate PostgreSQL databases per project
- Separate database users per project
- PostgreSQL enforces access control

✅ **Cannot Be Bypassed:**
- Projects cannot access other project databases
- Database-level security rules

### JWT Tokens

✅ **Per-Project JWT Secrets:**
- Each shared project gets a unique JWT secret
- Tokens are cryptographically isolated per project
- Tokens from Project A cannot be validated in Project B
- Same security model as dedicated projects

**Implementation:**
```python
# secrets_service.py - for shared projects
jwt_secret = py_secrets.token_urlsafe(32)  # Unique per project
```

**Benefits:**
- Cryptographic separation between projects
- Independent key rotation per project
- No possibility of cross-project token validation

### Network Isolation

✅ **Container Network:**
- All shared services on isolated Docker network
- No external access except through gateway

---

## Troubleshooting

### Issue: SQL Editor Affects All Projects

**Symptom:** Creating tables in Project A appears in Project B

**Cause:** Database connection using wrong database name

**Solution:**
1. Check project secrets: `POSTGRES_DB` should be `project_{id}`
2. Restart backend to clear connection cache
3. Verify with: `SELECT current_database()`

### Issue: Authentication Fails

**Symptom:** Login returns 500 error

**Possible Causes:**
1. Auth schema not initialized
2. Wrong database connection
3. Missing JWT secret

**Debug:**
```bash
# Check auth tables exist
docker exec -it supalove_shared_postgres psql -U postgres -d project_abc123 -c "\dt auth.*"

# Check project secrets
# In Control Plane database
SELECT key, value FROM project_secrets WHERE project_id = 'abc123';
```

### Issue: Gateway Routing Error

**Symptom:** 404 or wrong project data returned

**Debug:**
```bash
# Check gateway logs
docker logs supalove_shared_gateway_v3 -f

# Verify Control Plane is accessible
curl http://localhost:8000/health
```

```

---

## User Management

### Automatic Admin Creation

When a shared project is created, an admin user is automatically provisioned:

**Flow:**
```mermaid
graph LR
    A[Project Created] --> B[Get Org Owner Email]
    B --> C[Generate Secure Password]
    C --> D[Create User in auth.users]
    D --> E[Store Temp Password in Secrets]
    E --> F[Admin User Ready]
```

**Implementation:**
- Email: Organization owner's email
- Password: Secure 16-character random password
- Role: `admin` in `user_metadata`
- Storage: Temporary password stored as `ADMIN_TEMP_PASSWORD` secret

**Code Location:** `control-plane/api/src/services/project_user_service.py`

### User Management API

**Endpoints:**
```
GET    /api/v1/projects/{project_id}/users          # List users
POST   /api/v1/projects/{project_id}/users          # Create user
DELETE /api/v1/projects/{project_id}/users/{id}     # Delete user
GET    /api/v1/projects/{project_id}/admin-password # Get temp password (one-time)
```

**User Data Structure:**
```json
{
  "id": "uuid",
  "email": "user@example.com",
  "role": "admin|member",
  "created_at": "timestamp",
  "email_confirmed_at": "timestamp",
  "user_metadata": {
    "role": "admin|member",
    "created_by": "system|manual",
    "is_project_admin": true|false
  }
}
```

### Dashboard UI

**Location:** `/projects/{id}/users`

**Features:**
- View all project users
- Create new users with roles
- Delete users
- Retrieve one-time admin password
- Role badges and status indicators

### Database Storage

Users are stored in each project's isolated database:

```sql
-- Project database: project_abc123
SELECT * FROM auth.users;

-- Example row
id              | email              | role         | user_metadata
----------------|--------------------|--------------|-------------------
uuid-here       | admin@example.com  | authenticated| {"role": "admin"}
```

**Isolation:**
- Users in `project_abc123` cannot access `project_xyz789`
- Each project has completely separate user tables
- No cross-project user data leakage

### Documentation

See detailed guides:
- [API Documentation](./PROJECT_USER_MANAGEMENT_API.md) - Complete API reference
- [User Guide](./USER_GUIDE_PROJECT_USERS.md) - How to manage users in dashboard

---

## Future Enhancements

1. ~~**Per-Project JWT Secrets**~~ ✅ **Complete** - Better security isolation
2. **Database Sharding** - Multiple PostgreSQL instances for scaling

3. **Connection Pooling** - PgBouncer for better performance
4. **Read Replicas** - Scale read operations
5. **Multi-Region** - Deploy shared infrastructure closer to users

---

## File References

**Configuration:**
- [`data-plane/shared/docker-compose.yml`](file:///home/faris/Documents/MyApps/supalove/data-plane/shared/docker-compose.yml)

**Code:**
- [`control-plane/api/src/services/secrets_service.py`](file:///home/faris/Documents/MyApps/supalove/control-plane/api/src/services/secrets_service.py) - Secret generation
- [`control-plane/api/src/services/database_service.py`](file:///home/faris/Documents/MyApps/supalove/control-plane/api/src/services/database_service.py) - Database connections
- [`control-plane/api/src/api/v1/shared_auth.py`](file:///home/faris/Documents/MyApps/supalove/control-plane/api/src/api/v1/shared_auth.py) - Shared auth implementation

**Gateway:**
- [`data-plane/shared/routing-proxy/main.py`](file:///home/faris/Documents/MyApps/supalove/data-plane/shared/routing-proxy/main.py) - Request routing logic
