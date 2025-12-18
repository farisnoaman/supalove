# Implementation Plan - Step 6: Realtime Service

The goal is to add the Supabase Realtime service to the per-project infrastructure stack. This allows clients to listen to database changes.

## User Review Required

> [!IMPORTANT]
> The Realtime service requires the Postgres `wal_level` to be set to `logical` and the `supabase_realtime` publication to be present.
> We must ensure the postgres container is started with the command `-c wal_level=logical`.

## Changes

### Project Template

#### [MODIFY] [docker-compose.project.yml](file:///home/faris/Documents/MyApps/supalove/data-plane/templates/docker-compose.project.yml)
- Update `db` service:
    - Add `command: ["postgres", "-c", "wal_level=logical"]` to enable replication.
- Add `realtime` service:
    - Image: `supabase/realtime:v2.28.32` (stable version).
    - Environment variables:
        - `DB_HOST`: `db`
        - `DB_PORT`: `5432`
        - `DB_NAME`: `app`
        - `DB_USER`: `app`
        - `DB_PASSWORD`: `${DB_PASSWORD}`
        - `JWT_SECRET`: `${JWT_SECRET}`
        - `REPLICATION_MODE`: `RLS`
        - `REPLICATION_POLL_INTERVAL`: `100`
        - `SECURE_CHANNELS`: `true`
        - `SLOT_NAME`: `supabase_realtime_replication_slot`
        - `TEMPORARY_SLOT`: `true`
    - Ports: `${REALTIME_PORT}:4000`

### Provisioning Scripts

#### [MODIFY] [scripts/provision_project.py](file:///home/faris/Documents/MyApps/supalove/scripts/provision_project.py)
- Calculate `REALTIME_PORT` (e.g., `8000` + offset).
- Add `REALTIME_PORT` to `.env`.

#### [MODIFY] [provisioning_local.py](file:///home/faris/Documents/MyApps/supalove/control-plane/api/src/services/provisioning_local.py)
- Return `realtime_url` in the result dict.

#### [MODIFY] [provisioning_coolify.py](file:///home/faris/Documents/MyApps/supalove/control-plane/api/src/services/provisioning_coolify.py)
- Add `REALTIME_PORT` to env vars generation.

## Verification Plan

### Manual Verification
1.  **Provision Project**: `POST /v1/projects`.
2.  **Check Logs**: `docker logs project_<id>_realtime`.
3.  **Client Test**: Use a simple WebSocket client or curl to check connection to Realtime port.
