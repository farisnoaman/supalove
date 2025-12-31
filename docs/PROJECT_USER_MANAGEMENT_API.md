# Project User Management API Documentation

## Overview

The Project User Management API provides endpoints to manage users within project databases. Each project has its own isolated set of users stored in the project's `auth.users` table.

---

## Base URL

```
http://localhost:8000/api/v1/projects/{project_id}
```

All endpoints require authentication via Bearer token.

---

## Authentication

Include your access token in the Authorization header:

```bash
Authorization: Bearer YOUR_ACCESS_TOKEN
```

---

## Endpoints

### 1. List Project Users

Get all users in a project.

**Endpoint:** `GET /projects/{project_id}/users`

**Parameters:**
- `project_id` (path, required): The project ID

**Response:** `200 OK`

```json
[
  {
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "email": "admin@example.com",
    "role": "admin",
    "created_at": "2024-01-01T00:00:00",
    "email_confirmed_at": "2024-01-01T00:00:00",
    "user_metadata": {
      "role": "admin",
      "created_by": "system",
      "is_project_admin": true
    }
  }
]
```

**Example:**

```bash
curl -X GET \
  http://localhost:8000/api/v1/projects/abc123/users \
  -H "Authorization: Bearer YOUR_TOKEN"
```

---

### 2. Create User

Create a new user in the project.

**Endpoint:** `POST /projects/{project_id}/users`

**Parameters:**
- `project_id` (path, required): The project ID

**Request Body:**

```json
{
  "email": "user@example.com",
  "password": "SecurePassword123!",
  "role": "member",
  "user_metadata": {
    "custom_field": "value"
  }
}
```

**Fields:**
- `email` (string, required): User's email address
- `password` (string, required): User's password
- `role` (string, optional): User role - "admin" or "member" (default: "member")
- `user_metadata` (object, optional): Additional metadata

**Response:** `200 OK`

```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "email": "user@example.com",
  "role": "member",
  "created_at": "2024-01-01T00:00:00",
  "user_metadata": {
    "role": "member",
    "custom_field": "value"
  }
}
```

**Example:**

```bash
curl -X POST \
  http://localhost:8000/api/v1/projects/abc123/users \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "newuser@example.com",
    "password": "SecurePass123!",
    "role": "member"
  }'
```

---

### 3. Delete User

Remove a user from the project.

**Endpoint:** `DELETE /projects/{project_id}/users/{user_id}`

**Parameters:**
- `project_id` (path, required): The project ID
- `user_id` (path, required): The user ID to delete

**Response:** `200 OK`

```json
{
  "message": "User deleted successfully"
}
```

**Example:**

```bash
curl -X DELETE \
  http://localhost:8000/api/v1/projects/abc123/users/550e8400-e29b-41d4-a716-446655440000 \
  -H "Authorization: Bearer YOUR_TOKEN"
```

---

### 4. Get Admin Password (One-Time)

Retrieve the auto-generated admin password. This can only be done once.

**Endpoint:** `GET /projects/{project_id}/admin-password`

**Parameters:**
- `project_id` (path, required): The project ID

**Response:** `200 OK`

```json
{
  "password": "HDnP!@3Bx9mK2vLq",
  "email": "owner@example.com"
}
```

**Response:** `404 Not Found` (if already retrieved)

```json
{
  "detail": "Admin password not found or already retrieved"
}
```

**Example:**

```bash
curl -X GET \
  http://localhost:8000/api/v1/projects/abc123/admin-password \
  -H "Authorization: Bearer YOUR_TOKEN"
```

---

## Error Responses

### 400 Bad Request

Invalid input or validation error.

```json
{
  "detail": "Email already exists"
}
```

### 401 Unauthorized

Missing or invalid authentication token.

```json
{
  "detail": "Could not validate credentials"
}
```

### 403 Forbidden

User doesn't have access to this project.

```json
{
  "detail": "Access denied to project"
}
```

### 404 Not Found

Resource not found.

```json
{
  "detail": "User not found"
}
```

### 500 Internal Server Error

Server error.

```json
{
  "detail": "Internal server error message"
}
```

---

## User Metadata Schema

The `user_metadata` field in user objects contains role information and custom data:

```json
{
  "role": "admin|member",
  "created_by": "system|manual",
  "is_project_admin": true|false,
  "created_at_project_setup": true|false,
  "custom_field": "any value"
}
```

**Standard Fields:**
- `role`: User's role in the project
- `created_by`: How the user was created ("system" for auto-created admin)
- `is_project_admin`: Boolean flag for project admin
- `created_at_project_setup`: True if user was created during project setup

---

## Automatic Admin User

When a project is created, an admin user is automatically provisioned:

- **Email:** Organization owner's email
- **Password:** Secure 16-character random password
- **Role:** admin
- **Metadata:** Marked as system-created project admin

The temporary password is stored in project secrets and can be retrieved **once** via the admin-password endpoint.

---

## Integration Examples

### JavaScript/TypeScript (Supabase Client)

```typescript
import { createClient } from '@supabase/supabase-js'

// Initialize Supabase client for your project
const supabase = createClient(
  'http://localhost:8083/project_abc123',
  'your-anon-key'
)

// Sign in with auto-created admin
const { data, error } = await supabase.auth.signInWithPassword({
  email: 'owner@example.com',
  password: 'temp-password-from-dashboard'
})

// Create a new user (requires admin token)
const response = await fetch('http://localhost:8000/api/v1/projects/abc123/users', {
  method: 'POST',
  headers: {
    'Authorization': `Bearer ${adminToken}`,
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    email: 'newuser@example.com',
    password: 'UserPassword123!',
    role: 'member'
  })
})
```

### Python

```python
import requests

API_URL = "http://localhost:8000/api/v1"
project_id = "abc123"
token = "your-access-token"

headers = {"Authorization": f"Bearer {token}"}

# List users
response = requests.get(f"{API_URL}/projects/{project_id}/users", headers=headers)
users = response.json()

# Create user
new_user = {
    "email": "user@example.com",
    "password": "SecurePass123!",
    "role": "member"
}
response = requests.post(
    f"{API_URL}/projects/{project_id}/users",
    headers=headers,
    json=new_user
)

# Get admin password (one-time)
response = requests.get(
    f"{API_URL}/projects/{project_id}/admin-password",
    headers=headers
)
admin_credentials = response.json()
print(f"Admin: {admin_credentials['email']}")
print(f"Password: {admin_credentials['password']}")
```

---

## Security Considerations

1. **Password Requirements:**
   - Minimum 16 characters
   - Must contain uppercase, lowercase, digits, and special characters

2. **One-Time Password Access:**
   - Admin password can only be retrieved once
   - After retrieval, the secret is permanently deleted

3. **Database Isolation:**
   - Users are completely isolated per project
   - Each project has its own `auth.users` table

4. **Access Control:**
   - All endpoints require valid authentication
   - Users can only access projects they own or have access to

---

## Rate Limits

Currently no rate limits enforced. Consider implementing rate limiting in production.

---

## Changelog

### v1.0.0 (2024-01-01)
- Initial release
- Auto-admin creation on project setup
- CRUD operations for project users
- One-time admin password retrieval
- Role-based user management
