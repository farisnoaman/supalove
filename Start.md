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



