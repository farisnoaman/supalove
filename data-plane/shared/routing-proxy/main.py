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
from fastapi import FastAPI, Request, HTTPException, Header, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, Response
from typing import Optional
import psycopg2
from psycopg2 import pool
from functools import lru_cache
import asyncio
import websockets
from websockets.exceptions import ConnectionClosed

app = FastAPI(title="Supalove Shared Routing Proxy")

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Local development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

async def handle_realtime_request(request: Request, path: str, project_id: Optional[str] = None):
    # Extract project ID from header if not provided in arg
    if not project_id:
        project_id = request.headers.get("X-Tenant-Id")
    
    if not project_id:
         # Try query param? Realtime client might send it
         project_id = request.query_params.get("tenant")
         
    if not project_id and path == "api/tenants":
        # Health check might not have tenant, just pass through if generic?
        # But Realtime requires tenant for most things.
        pass

    async with httpx.AsyncClient() as client:
        headers = dict(request.headers)
        headers.pop("host", None)
        headers.pop("content-length", None) # let httpx handle it
        
        if project_id:
            headers["X-Tenant-Id"] = project_id
        
        body = await request.body()
        
        try:
            response = await client.request(
                method=request.method,
                url=f"{REALTIME_URL}/{path}",
                headers=headers,
                content=body,
                params=dict(request.query_params),
                timeout=30.0
            )
            
            return Response(
                content=response.content,
                status_code=response.status_code,
                headers=dict(response.headers)
            )
        except httpx.ConnectError:
             return JSONResponse({"error": "Realtime service unavailable"}, status_code=503)

@app.api_route("/projects/{project_id}/realtime/v1/{path:path}", methods=["GET", "POST", "PUT", "PATCH", "DELETE"])
async def proxy_realtime_project(
    request: Request,
    project_id: str,
    path: str,
):
    """Proxy Realtime requests with project_id in path"""
    return await handle_realtime_request(request, path, project_id)

@app.api_route("/realtime/v1/{path:path}", methods=["GET", "POST", "PUT", "PATCH", "DELETE"])
async def proxy_realtime_generic(
    request: Request,
    path: str,
):
    """Proxy Realtime requests without project_id in path (relies on header)"""
    return await handle_realtime_request(request, path)

@app.websocket("/realtime/v1/websocket")
async def websocket_proxy(websocket: WebSocket):
    await websocket.accept()
    
    # Realtime client usually sends params like ?vsn=1.0.0&token=...
    # We need to extract tenant from params or headers if possible
    # Supabase JS client sends 'apikey' in params which is the anon key.
    # We might need to inspect that to find the project, OR require X-Tenant-Id header if possible.
    # However, standard WebSocket API in browser defaults don't allow custom headers easily.
    # So we rely on the URL path or query params.
    # BUT, our route is generic. 
    # Let's check query params.
    
    params = dict(websocket.query_params)
    project_id = params.get("tenant") # Some clients send this
    if not project_id:
        # Fallback: Is there a way to map key to project? Not easily here.
        # Ideally client connects to /projects/{id}/realtime/v1/websocket
        pass

    # Construct upstream URL
    upstream_ws_url = f"{REALTIME_URL.replace('http', 'ws')}/websocket"
    
    try:
        async with websockets.connect(
            upstream_ws_url, 
            extra_headers=dict(websocket.headers) if project_id else None # Filter headers?
        ) as upstream_ws:
            
            async def forward_to_client():
                try:
                    async for message in upstream_ws:
                        await websocket.send_text(message)
                except ConnectionClosed:
                    await websocket.close()

            async def forward_to_upstream():
                try:
                    while True:
                        data = await websocket.receive_text()
                        await upstream_ws.send(data)
                except WebSocketDisconnect:
                    await upstream_ws.close()

            await asyncio.gather(forward_to_client(), forward_to_upstream())
            
    except Exception as e:
        print(f"WebSocket proxy error: {e}")
        await websocket.close(code=1011)



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
            "realtime": f"/projects/{project_id}/realtime/v1",
        },
        "status": config.get("status")
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
