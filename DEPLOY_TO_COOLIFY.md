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
    *   `ALLOWED_ORIGINS` (Comma-separated list of allowed origins) - Set this to your dashboard domain (e.g., `https://supalove.hayataxi.online`).
        *   **Crucial for CORS**: This fixes the "blocked by CORS policy" error. Coolify will pass this to the API.
    *   `NEXT_PUBLIC_API_URL` (Required build variable) - Set this to the public URL of your API (e.g., `https://api.hayataxi.online`).
        *   **Crucial**: In Coolify, ensure this is set in the **Environment Variables** section. Since we configured it as a build argument in `docker-compose.coolify.yml`, Coolify will pass it during the build process.
8.  **Expose Services**:
    *   **Dashboard**: Port `3000`. Assign a domain (e.g., `https://supalove.hayataxi.online`).
    *   **API**: Port `8000`. Assign a domain (e.g., `https://api.hayataxi.online`).
    *   **Keycloak**: Port `8080`. Assign a domain (e.g., `https://auth..hayataxi.online`).
    *   **MinIO Console**: Port `9001` (Optional, for admin).
    *   **MinIO API**: Port `9000`. Assign a domain (e.g., `https://s3.hayataxi.online`).

    *Note: You need to set `NEXT_PUBLIC_API_URL` to your API domain in the Dashboard environment variables.*

9.  **Deploy**.
