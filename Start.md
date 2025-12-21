# Start :
## open two termainls
### Temrinal 1: 

cd ~/Documents/MyApps/supabase_lovable_cloud_clone/control-plane/api
python3 -m venv .venv
source .venv/bin/activate

### terminal 2
 source /home/faris/Documents/MyApps/supabase_lovable_cloud_clone/.venv/bin/activate
 docker ps
 docker compose up -d
 psql -h localhost -p 5433 -U platform control_plane
 "password: platform"
 : 
 If you get a psql prompt → DB is 100% healthy ✅
 ### in Terminal 1
cd src
uvicorn main:app --reload --port 8000
### Terminal 3: Open new terminal window

curl -X POST http://localhost:8000/v1/projects

-------------------The result should be: ------
{
  "project_id": "...",
  "status": "running",
  "api_url": "http://localhost:..."
}
----------------------
../.venv/bin/python -m uvicorn main:app --reload --port 8000
curl -X POST http://localhost:8000/v1/projects/11e6ecfe5c8f/stop


---------------------new implemntation-------------
ps aux | grep uvicorn | grep -v grep

ps aux | grep "npm run dev" | grep -v grep

nohup ../.venv/bin/uvicorn main:app --host 0.0.0.0 --port 8000 > api.log 2>&1 &

curl -s http://localhost:8000/v1/projects | head -n 20
-----------
nohup ../.venv/bin/uvicorn main:app --host 0.0.0.0 --port 8000 --reload > api.log 2>&1 &
-------
tail -n 15 api.log
---------


curl -s -H "Origin: http://localhost:3000" -H "Access-Control-Request-Method: GET" -H "Access-Control-Request-Headers: Content-Type" -X OPTIONS http://localhost:8000/v1/projects -v 2>&1 | grep -i "access-control"
----------------
Walkthrough: Backend running in Virtual Environment
I have successfully set up and started the backend within the Python virtual environment.

Changes Made
1. Environment Preparation
Verified the existence of .venv in control-plane/api.
Installed all dependencies from requirements.txt using the venv's pip:
/home/faris/Documents/MyApps/supalove/control-plane/api/.venv/bin/pip install -r requirements.txt
2. Infrastructure Setup
Started the required services (PostgreSQL, Keycloak, MinIO) via Docker Compose to allow the backend to initialize its database connection:
docker compose up -d control-plane-db keycloak minio
3. Backend Startup
Launched the FastAPI server using the uvicorn binary from the virtual environment:
/home/faris/Documents/MyApps/supalove/control-plane/api/.venv/bin/uvicorn main:app --reload --port 8000
Verification Results
Server Status
The server started successfully and reached the "Application startup complete" state.

INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [14321] using WatchFiles
[Provisioning] Using Local Docker provider
INFO:     Started server process [14323]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
Health Check
I verified the server is responding to requests:

curl http://localhost:8000/ returned {"detail":"Not Found"}, confirming the application is active and handling requests.

to check m, a project is working: in root
curl -X POST http://localhost:8000/v1/projects
```
````psql -h localhost -p 5433 -U platform control_plane -c "SELECT key, value FROM 
project_secrets WHERE project_id = 'fa254754371f';"
```

cd data-plane/projects/fa254754371f && docker compose down -v && cd ../../.. && rm -rf data-plane/projects/fa254754371f

---------
## to create repo tree:
# Show only source files, ignore all build/generated folders

tree -I 'node_modules|.git|dist|build|.next|.nuxt|.venv|coverage|*.log|*.tmp' > repo_structure.txt
