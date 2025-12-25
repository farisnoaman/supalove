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
    *   `POSTGRES_PASSWORD` (Generate a strong one)
    *   `KEYCLOAK_ADMIN_PASSWORD` (Generate a strong one)
    *   `MINIO_ROOT_PASSWORD` (Generate a strong one)
8.  **Expose Services**:
    *   **Dashboard**: Port `3000`. Assign a domain (e.g., `https://supalove.yourdomain.com`).
    *   **API**: Port `8000`. Assign a domain (e.g., `https://api.supalove.yourdomain.com`).
    *   **Keycloak**: Port `8080`. Assign a domain (e.g., `https://auth.supalove.yourdomain.com`).
    *   **MinIO Console**: Port `9001` (Optional, for admin).
    *   **MinIO API**: Port `9000`. Assign a domain (e.g., `https://s3.supalove.yourdomain.com`).

    *Note: You need to set `NEXT_PUBLIC_API_URL` to your API domain in the Dashboard environment variables.*

9.  **Deploy**.
