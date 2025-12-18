# Step 4.3: Project Lifecycle Management (Enhanced)

## Goal description
Implement the ability to Stop, Start, Delete, and **Restore** projects via the Control Plane API. This completes the basic lifecycle management for projects.

## User Review Required
> [!NOTE]
> **Change in Deletion Logic**: "Delete" is now a "Soft Delete". Functional data is preserved in a `_deleted` directory to allow for Restoration.

## Proposed Changes

### Scripts Layer
#### [NEW] [lifecycle.py](file:///home/faris/Documents/MyApps/supalove/scripts/lifecycle.py)
- Implement `stop_project(project_id)`: Runs `docker compose down`
- Implement `start_project(project_id)`: Runs `docker compose up -d`
- **[UPDATED]** `delete_project(project_id)`: Runs `docker compose down`. Moves directory to `_deleted` suffix (Soft Delete).
- **[NEW]** `restore_project(project_id)`: Moves directory back from `_deleted`.

### Control Plane Service
#### [MODIFY] [provisioning_service.py](file:///home/faris/Documents/MyApps/supalove/control-plane/api/src/services/provisioning_service.py)
- Add wrappers for `stop_project`, `start_project`, `delete_project`, `restore_project`.

#### [MODIFY] [project_service.py](file:///home/faris/Documents/MyApps/supalove/control-plane/api/src/services/project_service.py)
- Add logic to update project status in DB (`stopped`, `running`, `deleted`).
- Implement `restore_project`: Updates status back to `stopped`.
- Call provisioning service methods.

### API Layer
#### [MODIFY] [projects.py](file:///home/faris/Documents/MyApps/supalove/control-plane/api/src/api/v1/projects.py)
- Add endpoints:
    - `POST /projects/{id}/stop`
    - `POST /projects/{id}/start`
    - `POST /projects/{id}/restore`
    - `DELETE /projects/{id}`

## Verification Plan

### Manual Verification
1. **Create Project**: `POST /projects` -> Get ID `abc`
2. **Stop Project**: `POST /projects/abc/stop` -> Verify container stopped (`docker ps`).
3. **Start Project**: `POST /projects/abc/start` -> Verify container running.
4. **Delete Project**: `DELETE /projects/abc` -> Verify container removed and directory moved to `_deleted`.
5. **Restore Project**: `POST /projects/abc/restore` -> Verify directory restored and status is `stopped`.
