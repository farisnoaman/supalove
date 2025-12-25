# Supalove API Reference

Base URL: `https://api.yourdomain.com/api/v1`

All endpoints require authentication via Bearer token except `/auth/login` and `/auth/register`.

---

## Authentication

### Register

Create a new platform user account.

```http
POST /auth/register
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "securepassword",
  "name": "John Doe"
}
```

**Response** `200 OK`:
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIs...",
  "token_type": "bearer"
}
```

---

### Login

Authenticate and receive access token.

```http
POST /auth/login
Content-Type: application/x-www-form-urlencoded

username=user@example.com&password=securepassword
```

**Response** `200 OK`:
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIs...",
  "token_type": "bearer"
}
```

---

### Get Current User

```http
GET /auth/me
Authorization: Bearer <token>
```

**Response** `200 OK`:
```json
{
  "id": "uuid",
  "email": "user@example.com",
  "name": "John Doe",
  "created_at": "2024-01-01T00:00:00Z"
}
```

---

## Organizations

### List Organizations

```http
GET /orgs
Authorization: Bearer <token>
```

**Response** `200 OK`:
```json
[
  {
    "id": "uuid",
    "name": "My Organization",
    "slug": "my-org",
    "created_at": "2024-01-01T00:00:00Z"
  }
]
```

---

### Create Organization

```http
POST /orgs
Authorization: Bearer <token>
Content-Type: application/json

{
  "name": "New Organization"
}
```

---

## Projects

### List Projects

```http
GET /projects?org_id=<org_uuid>
Authorization: Bearer <token>
```

**Response** `200 OK`:
```json
[
  {
    "id": "abc123def456",
    "name": "My Project",
    "status": "running",
    "org_id": "uuid",
    "created_at": "2024-01-01T00:00:00Z"
  }
]
```

---

### Create Project

```http
POST /projects
Authorization: Bearer <token>
Content-Type: application/json

{
  "name": "My New Project",
  "org_id": "uuid"
}
```

**Response** `200 OK`:
```json
{
  "id": "abc123def456",
  "name": "My New Project",
  "status": "provisioning",
  "api_url": "http://localhost:5501",
  "db_url": "postgresql://...",
  "anon_key": "eyJ...",
  "service_role_key": "eyJ..."
}
```

---

### Get Project

```http
GET /projects/{project_id}
Authorization: Bearer <token>
```

---

### Start Project

```http
POST /projects/{project_id}/start
Authorization: Bearer <token>
```

---

### Stop Project

```http
POST /projects/{project_id}/stop
Authorization: Bearer <token>
```

---

### Delete Project

```http
DELETE /projects/{project_id}
Authorization: Bearer <token>
```

---

## Project Secrets

### List Secrets

```http
GET /projects/{project_id}/secrets
Authorization: Bearer <token>
```

**Response** `200 OK`:
```json
{
  "DB_PASSWORD": "********",
  "JWT_SECRET": "********",
  "ANON_KEY": "eyJ...",
  "SERVICE_ROLE_KEY": "eyJ...",
  "DB_PORT": "5500",
  "REST_PORT": "5501"
}
```

---

### Update Secret

```http
PUT /projects/{project_id}/secrets
Authorization: Bearer <token>
Content-Type: application/json

{
  "key": "CUSTOM_VAR",
  "value": "custom_value"
}
```

---

## Project Auth Users

### List Auth Users

```http
GET /projects/{project_id}/auth/users
Authorization: Bearer <token>
```

**Response** `200 OK`:
```json
{
  "users": [
    {
      "id": "uuid",
      "email": "projectuser@example.com",
      "created_at": "2024-01-01T00:00:00Z"
    }
  ]
}
```

---

### Create Auth User

```http
POST /projects/{project_id}/auth/users
Authorization: Bearer <token>
Content-Type: application/json

{
  "email": "newuser@example.com",
  "password": "userpassword"
}
```

---

### Delete Auth User

```http
DELETE /projects/{project_id}/auth/users/{user_id}
Authorization: Bearer <token>
```

---

## Storage

### List Files

```http
GET /projects/{project_id}/storage?bucket=public&path=/
Authorization: Bearer <token>
```

---

### Upload File

```http
POST /projects/{project_id}/storage/upload
Authorization: Bearer <token>
Content-Type: multipart/form-data

bucket=public
path=/images
file=@photo.jpg
```

---

### Delete File

```http
DELETE /projects/{project_id}/storage
Authorization: Bearer <token>
Content-Type: application/json

{
  "bucket": "public",
  "path": "/images/photo.jpg"
}
```

---

## Edge Functions

### List Functions

```http
GET /projects/{project_id}/functions
Authorization: Bearer <token>
```

---

### Deploy Function

```http
POST /projects/{project_id}/functions
Authorization: Bearer <token>
Content-Type: application/json

{
  "name": "hello-world",
  "code": "Deno.serve(() => new Response('Hello!'))"
}
```

---

## Database

### Execute SQL

```http
POST /projects/{project_id}/database/sql
Authorization: Bearer <token>
Content-Type: application/json

{
  "query": "SELECT * FROM users LIMIT 10"
}
```

---

### List Tables

```http
GET /projects/{project_id}/database/tables
Authorization: Bearer <token>
```

---

## Health Check

```http
GET /health
```

**Response** `200 OK`:
```json
{
  "status": "healthy",
  "version": "1.0.0"
}
```

---

## Error Responses

All errors follow this format:

```json
{
  "detail": "Error message describing what went wrong"
}
```

**Common Status Codes**:
| Code | Description |
|------|-------------|
| 400 | Bad Request - Invalid input |
| 401 | Unauthorized - Missing or invalid token |
| 403 | Forbidden - Insufficient permissions |
| 404 | Not Found - Resource doesn't exist |
| 500 | Internal Server Error |
