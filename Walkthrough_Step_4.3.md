# Walkthrough - Step 4.2: Wiring Docker Compose Ports

I have successfully implemented Step 4.2. The control plane now correctly wires Docker Compose ports for each project and returns the accessible URLs.

## Changes

### 1. Control Plane Service
- Modified `provision_project` to capture environment variables (ports) from the script.
- Modified `create_project` to construct and return `api_url` and `db_url` using the assigned ports.

### 2. Provisioning Script
- Updated `provision_project.py` to:
    - Explicitly pass `.env` file to Docker Compose (fixing container configuration issues).
    - Return the assigned ports to the caller.

## Verification Results

### 1. Project Creation
I called the API to create a new project:
```bash
curl -X POST http://localhost:8000/v1/projects
```

**Response:**
```json
{
  "project_id": "dd8f6309ef31",
  "status": "running",
  "api_url": "http://localhost:7221",
  "db_url": "postgresql://app:v0qggVBNyiN2ieav8hTEj5xZYP14zlnC@localhost:6221/app"
}
```

### 2. Infrastructure Validation
I verified that the containers are running with the correct names and ports:

```bash
docker ps
```

**Output:**
```
CONTAINER ID   IMAGE                 PORTS                                         NAMES
a0b5051d782b   postgrest/postgrest   0.0.0.0:7221->3000/tcp                        project_dd8f6309ef31_rest
b32dc1536dc9   postgres:15           0.0.0.0:6221->5432/tcp                        project_dd8f6309ef31_db
```

- **Project ID**: `dd8f6309ef31`
- **DB Port**: `6221` (Matched response)
- **API Port**: `7221` (Matched response)
- **Container Names**: Correctly namespaced with project ID (e.g., `project_dd8f6309ef31_db`).

- **Container Names**: Correctly namespaced with project ID (e.g., `project_dd8f6309ef31_db`).

# Walkthrough - Step 4.3: Project Lifecycle (Enhanced)

I have successfully implemented Step 4.3 with **Restore Functionality**. The control plane now supports Stopping, Starting, Deleting (Soft), and Restoring projects.

## Changes

### 1. Lifecycle Script
- Created `scripts/lifecycle.py`:
  - `delete_project`: Soft deletes by renaming folder to `_deleted`.
  - `restore_project`: Restores folder from `_deleted`.

### 2. Services
- Updated `provisioning_service.py` and `project_service.py` to support restore operations.

### 3. API
- Added endpoints:
    - `POST /projects/{id}/stop`
    - `POST /projects/{id}/start`
    - `POST /projects/{id}/restore`
    - `DELETE /projects/{id}`

## Verification Results

### Lifecycle Test Sequence

1. **Created Project** (`4714de0c5c04`)
2. **Stopped Project**
   ```bash
   curl -X POST http://localhost:8000/v1/projects/4714de0c5c04/stop
   ```
   **Result**: `{ "status": "stopped", ... }`. Containers stopped.

3. **Soft Deleted Project**
   ```bash
   curl -X DELETE http://localhost:8000/v1/projects/4714de0c5c04
   ```
   **Result**: `{ "status": "deleted", ... }`. Folder renamed to `4714de0c5c04_deleted`.

4. **Restored Project**
   ```bash
   curl -X POST http://localhost:8000/v1/projects/4714de0c5c04/restore
   ```
   **Result**: `{ "status": "stopped", ... }`. Folder restored.

5. **Started Project**
    - (Tested in previous run, confirmed working).

## Conclusion
The project lifecycle is fully managed, including data safety via soft deletes and restoration.

## Conclusion
The system now correctly provisions isolated project stacks with predictable, accessible ports and returns the connection details to the user.
