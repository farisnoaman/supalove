Step 4.3: Project Lifecycle Management
Goal description
Implement the ability to Stop, Start, and Delete projects via the Control Plane API. This completes the basic lifecycle management for projects, moving beyond just "Provisioning".

User Review Required
NOTE

This step continues to use local Docker Compose specific logic. The "Replace with Coolify" step from the Roadmap is deferred to Step 5, as we first want to establish the Control Plane's contract for these operations.

Proposed Changes
Scripts Layer
[NEW] 
lifecycle.py
Implement stop_project(project_id): Runs docker compose down
Implement start_project(project_id): Runs docker compose up -d
Implement delete_project(project_id): Runs docker compose down -v and deletes directory.
Control Plane Service
[MODIFY] 
provisioning_service.py
Add wrappers for stop_project, start_project, delete_project.
[MODIFY] 
project_service.py
Add logic to update project status in DB (stopped, running, deleted).
Call provisioning service methods.
API Layer
[MODIFY] 
projects.py
(Note: I need to verify if this file exists or if it's in 
main.py
 or routes)

Add endpoints:
POST /projects/{id}/stop
POST /projects/{id}/start
DELETE /projects/{id}
Verification Plan
Manual Verification
Create Project: POST /projects -> Get ID abc
Stop Project: POST /projects/abc/stop -> Verify container stopped (docker ps).
Start Project: POST /projects/abc/start -> Verify container running.
Delete Project: DELETE /projects/abc -> Verify container removed and directory gone.