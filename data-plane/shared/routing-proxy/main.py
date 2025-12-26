"""
Routing Proxy for Shared Supalove Stack

This service handles multi-tenant routing for shared projects:
1. Extracts project ID from request headers or subdomain
2. Looks up project configuration from control plane
3. Routes requests to the appropriate database
4. Injects correct JWT secret for authentication
"""
import os
import httpx
from fastapi import FastAPI, Request, HTTPException, Header
from fastapi.responses import JSONResponse
from typing import Optional
import psycopg2
from psycopg2 import pool
from functools import lru_cache
import asyncio


app = FastAPI(title="Supalove Shared Routing Proxy")

# Configuration
CONTROL_PLANE_URL = os.getenv("CONTROL_PLANE_URL", "http://localhost:8000")
SHARED_POSTGRES_HOST = os.getenv("SHARED_POSTGRES_HOST", "shared-postgres")
SHARED_POSTGRES_PORT = int(os.getenv("SHARED_POSTGRES_PORT", "5432"))
SHARED_POSTGRES_USER = os.getenv("SHARED_POSTGRES_USER", "postgres")
SHARED_POSTGRES_PASSWORD = os.getenv("SHARED_POSTGRES_PASSWORD", "postgres")

# Upstream service URLs
POSTGREST_URL = os.getenv("POSTGREST_URL", "http://shared-api:3000")
AUTH_URL = os.getenv("AUTH_URL", "http://shared-auth:9999")
STORAGE_URL = os.getenv("STORAGE_URL", "http://shared-storage:5000")
REALTIME_URL = os.getenv("REALTIME_URL", "http://shared-realtime:4000")

# Project config cache
project_cache = {}
cache_ttl = 300  # 5 minutes


async def get_project_config(project_id: str) -> dict:
    """
    Fetch project configuration from control plane.
    Caches results for performance.
    """
    cached = project_cache.get(project_id)
    if cached and (asyncio.get_event_loop().time() - cached["timestamp"]) < cache_ttl:
        return cached["config"]
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                f"{CONTROL_PLANE_URL}/api/v1/projects/{project_id}",
                timeout=10.0
            )
            if response.status_code == 200:
                config = response.json()
                project_cache[project_id] = {
                    "config": config,
                    "timestamp": asyncio.get_event_loop().time()
                }
                return config
            else:
                raise HTTPException(status_code=404, detail=f"Project {project_id} not found")
        except httpx.RequestError as e:
            raise HTTPException(status_code=503, detail=f"Control plane unavailable: {str(e)}")


def extract_project_id(request: Request, x_project_id: Optional[str] = None) -> str:
    """
    Extract project ID from:
    1. X-Project-Id header
    2. Subdomain (project-id.shared.supalove.com)
    3. Path prefix (/projects/{id}/...)
    """
    # 1. Check header
    if x_project_id:
        return x_project_id
    
    # 2. Check subdomain
    host = request.headers.get("host", "")
    if ".shared." in host:
        subdomain = host.split(".")[0]
        if subdomain:
            return subdomain
    
    # 3. Check path
    path = request.url.path
    if path.startswith("/projects/"):
        parts = path.split("/")
        if len(parts) >= 3:
            return parts[2]
    
    raise HTTPException(
        status_code=400,
        detail="Project ID required. Use X-Project-Id header or subdomain."
    )


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "service": "routing-proxy"}


@app.api_route("/projects/{project_id}/rest/v1/{path:path}", methods=["GET", "POST", "PUT", "PATCH", "DELETE"])
async def proxy_rest(
    request: Request,
    project_id: str,
    path: str,
    x_project_id: Optional[str] = Header(None),
):
    """
    Proxy REST API requests to PostgREST with correct database context.
    """
    config = await get_project_config(project_id)
    db_name = config.get("db_name", f"project_{project_id}")
    
    # Forward the request to PostgREST
    async with httpx.AsyncClient() as client:
        # Construct headers - pass through auth headers
        headers = dict(request.headers)
        headers["X-Supalove-DB"] = db_name
        
        # Remove host header to avoid conflicts
        headers.pop("host", None)
        
        body = await request.body()
        
        response = await client.request(
            method=request.method,
            url=f"{POSTGREST_URL}/{path}",
            headers=headers,
            content=body,
            params=dict(request.query_params),
            timeout=30.0
        )
        
        return JSONResponse(
            content=response.json() if response.content else None,
            status_code=response.status_code,
            headers=dict(response.headers)
        )


@app.api_route("/projects/{project_id}/auth/v1/{path:path}", methods=["GET", "POST", "PUT", "PATCH", "DELETE"])
async def proxy_auth(
    request: Request,
    project_id: str,
    path: str,
):
    """
    Proxy Auth requests to GoTrue.
    """
    config = await get_project_config(project_id)
    
    async with httpx.AsyncClient() as client:
        headers = dict(request.headers)
        headers.pop("host", None)
        
        body = await request.body()
        
        response = await client.request(
            method=request.method,
            url=f"{AUTH_URL}/{path}",
            headers=headers,
            content=body,
            params=dict(request.query_params),
            timeout=30.0
        )
        
        return JSONResponse(
            content=response.json() if response.content else None,
            status_code=response.status_code,
            headers=dict(response.headers)
        )


@app.api_route("/projects/{project_id}/storage/v1/{path:path}", methods=["GET", "POST", "PUT", "PATCH", "DELETE"])
async def proxy_storage(
    request: Request,
    project_id: str,
    path: str,
):
    """
    Proxy Storage requests.
    """
    config = await get_project_config(project_id)
    
    async with httpx.AsyncClient() as client:
        headers = dict(request.headers)
        headers.pop("host", None)
        
        body = await request.body()
        
        response = await client.request(
            method=request.method,
            url=f"{STORAGE_URL}/{path}",
            headers=headers,
            content=body,
            params=dict(request.query_params),
            timeout=30.0
        )
        
        # Handle both JSON and binary responses
        content_type = response.headers.get("content-type", "")
        if "application/json" in content_type:
            return JSONResponse(
                content=response.json() if response.content else None,
                status_code=response.status_code,
                headers=dict(response.headers)
            )
        else:
            from fastapi.responses import Response
            return Response(
                content=response.content,
                status_code=response.status_code,
                headers=dict(response.headers)
            )


@app.get("/projects/{project_id}")
async def get_project_info(project_id: str):
    """Get project connection information."""
    config = await get_project_config(project_id)
    return {
        "project_id": project_id,
        "endpoints": {
            "rest": f"/projects/{project_id}/rest/v1",
            "auth": f"/projects/{project_id}/auth/v1",
            "storage": f"/projects/{project_id}/storage/v1",
        },
        "status": config.get("status")
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
