Step 5: Replace Shell Scripts with Coolify API
Goal Description
Transition from local Docker Compose scripts to a proper orchestration API using Coolify. To ensure robustness and easier testing, we will first refactor the current provisioning logic into a modular ProvisioningProvider interface. This allows us to support both "Local Docker" (legacy/dev) and "Coolify" (prod) backends.

User Review Required
IMPORTANT

Configuration Required: To use Coolify, you must provide COOLIFY_API_URL and COOLIFY_API_TOKEN in your 
.env
. If not provided, the system will default to the existing Local Docker provisioner.

NOTE

This plan introduces a Strategy Pattern for provisioning.

Proposed Changes
1. Refactoring: Provisioning Interface
[NEW] 
provisioning_interface.py
Define abstract base class ProvisioningProvider with methods:
provision_project(project_id: str) -> dict
stop_project(project_id: str)
start_project(project_id: str)
delete_project(project_id: str)
restore_project(project_id: str)
2. Implementation: Local Provider
[NEW] 
provisioning_local.py
Moves logic from 
provisioning_service.py
 functions into LocalProvisioner class.
Calls existing 
scripts/provision_project.py
 and 
scripts/lifecycle.py
.
3. Implementation: Coolify Provider
[NEW] 
provisioning_coolify.py
Implements CoolifyProvisioner.
Uses httpx to communicate with Coolify API (v4).
Maps operations:
provision_project
 -> Create Project/Resource in Coolify.
stop/start/delete -> Call respective Coolify endpoints.
4. Service Layer Update
[MODIFY] 
provisioning_service.py
Delete old procedural functions.
Instantiate the correct provider based on env vars:
if os.getenv("COOLIFY_API_URL"):
    provider = CoolifyProvisioner(...)
else:
    provider = LocalProvisioner(...)
Expose methods that delegate to provider.
Verification Plan
1. Regression Test (Local)
Ensure COOLIFY_API_URL is unset.
Run POST /projects.
Verify docker ps shows containers (Local Docker).
2. Coolify Test (Mock/Real)
Set COOLIFY_API_URL=https://demo.coolify.io/api/v1 (or mock).
Run POST /projects.
Verify code attempts to call Coolify API (check logs).