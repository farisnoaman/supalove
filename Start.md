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
