# Security Isolation Strategy: Docker Socket Protection

## The Problem
The current Control Plane (V1) runs on the same host as the projects and interacts with the Docker socket directly. This is a security risk: if the Control Plane is compromised, the attacker has full root access to the host.

## V2 Mitigation Strategy
To achieve true production-grade isolation, we are moving towards an asynchronous, worker-based provisioning model.

### 1. Provisioning Worker
- The **Control Plane** never talks to Docker.
- It writes "Provisioning Tasks" to a secure queue (e.g., Redis/Postgres).
- A separate **Provisioning Worker** (running on a hardened host or VM) polls for tasks.
- Only the **Worker** has access to the Docker socket or the Cloud API (Coolify/AWS).

### 2. Filesystem Isolation
- Projects are provisioned in isolated directories.
- The Control Plane never "guesses" if a project exists by looking at `/data-plane/projects`.
- It **must** verify existence in the central database first (implemented in V2 `DatabaseService`).

### 3. Secrets Boundary
- Secrets are encrypted at rest (future step).
- Secrets are generated once and stored in the Control Plane database.
- They are passed to the Worker during provisioning and stored in the project's `.env` file, which is inaccessible to other projects.

### 4. Network Isolation
- Each project runs in its own Docker network.
- The Control Plane communicates via the Project's specific API port, not via internal Docker links unless necessary.
