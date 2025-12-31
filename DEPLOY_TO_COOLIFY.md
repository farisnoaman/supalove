# Deploying Supalove to Coolify

This guide explains how to deploy Supalove to your Coolify instance.

## Prerequisites

1.  A Coolify instance (e.g., https://coolify.hayataxi.online).
2.  Your Supalove source code pushed to a Git repository (GitHub/GitLab).

## Steps

1.  **Login to Coolify**.
2.  **Create a New Project**.
3.  **Select "Production" Environment**.
4.  **Add New Resource** -> **Git Repository** (or **Private Git Repository** if it's private).
5.  **Select your Supalove repository**.
6.  **Configuration**:
    *   **Build Pack**: Docker Compose
    *   **Docker Compose File**: `docker-compose.coolify.yml` (Enter this path in the configuration field)
    *   **Install Command**: (Leave default)
    *   **Build Command**: (Leave default)
    *   **Start Command**: (Leave default)
7.  **Environment Variables**:
    You can leave the defaults or override them in the specific secrets section:
    *   `MINIO_ROOT_PASSWORD` (Generate a strong one)
    *   `ALLOWED_ORIGINS` (Comma-separated list of allowed origins) - Set this to your dashboard domain.
    *   `NEXT_PUBLIC_API_URL` (Required build variable) - Set this to the public URL of your API.
    *   `SHARED_POSTGRES_PASSWORD` (Secure password for shared DB)
    *   `SHARED_JWT_SECRET` (32+ char random string for JWT signing)
    *   `SECRET_KEY_BASE` (64+ char random string for Realtime service)

8.  **Expose Services**:
    *   **Dashboard**: Port `3000`. Assign a domain (e.g., `https://console.example.com`).
    *   **API (Control Plane)**: Port `8000`. Assign a domain (e.g., `https://api.example.com`).
    *   **Shared Gateway**: Port `8083`. Assign a domain (e.g., `https://gateway.example.com`).
    *   **MinIO Console**: Port `9001`. Assign a domain (e.g., `https://s3-console.example.com`).
    *   **MinIO API**: Port `9000`. Assign a domain (e.g., `https://s3.example.com`).
    *   **Keycloak** (Legacy): Port `8080`. (Optional).

    *Note: The Shared Gateway (Port 8083) handles all project API traffic (Auth, API, Realtime).*

9.  **Deploy**.

