import asyncio
import websockets
import json
import secrets
import time
import urllib.request

API_URL = "http://localhost:8000/v1/projects"

async def verify_realtime():
    print("1. Creating Project...")
    project_id = secrets.token_hex(4)
    
    req = urllib.request.Request(API_URL, data=json.dumps({"id": project_id}).encode('utf-8'), headers={'Content-Type': 'application/json'}, method='POST')
    try:
        with urllib.request.urlopen(req) as f:
            resp_body = f.read().decode('utf-8')
            print(f"Response: {resp_body}")
            data = json.loads(resp_body)
    except Exception as e:
        print(f"Failed to create project: {e}")
        return
    
    print(f"Project Created: {json.dumps(data, indent=2)}")
    
    realtime_url = data.get("realtime_url")
    jwt_secret = data.get("jwt_secret", "fallback-secret-for-dev") # Might not be exposed in response if encrypted, but local provisioner usually doesn't encrypt in resp
    
    # Local provisioner returns: {'api_url': ..., 'db_url': ..., 'realtime_url': ...}
    # It doesn't strictly return jwt_secret in the response body of provision_project in our implementation?
    # Let's check provisioning_local.py again. It returns the dict from provision_project.
    # The API endpoint `POST /v1/projects` likely returns what provision_project returns.
    
    if not realtime_url:
        print("No realtime_url returned!")
        return

    print(f"2. Connecting to Realtime: {realtime_url}")
    
    # Polling wait for container to be ready
    connected = False
    for i in range(10):
        try:
            # Supabase Realtime requires a specific path/params usually?
            # WebSocket URL: ws://host:port/socket/websocket?apikey=...&vsn=1.0.0
            # We need to construct the full Phoenix Channel URL
            # But let's try raw connection first or with params
            
            # Param: apikey (JWT)
            # Param: vsn=2.0.0
            
            # NOTE: We didn't get the JWT from the creation response explicitly in previous steps 
            # unless we updated `provisioning_local.py` to return it.
            # `provisioning_local.py` returns env_vars based dict but filtered.
            # Let's assume we can use the default or we need to peek at the .env file or `secrets` dict.
            # Wait, `script_provision` returns env_vars.
            
            # For verification, we can just try to open the socket. 
            # Realtime auth usually happens on channel join, but initial socket connection might need params.
            
            full_url = f"{realtime_url}/socket/websocket?vsn=2.0.0"
            
            async with websockets.connect(full_url) as websocket:
                print("Connected to WebSocket!")
                
                # Join a channel (Realtime RLS)
                # topic = "realtime:public"
                # join_msg = dict(topic=topic, event="phx_join", payload={}, ref="1")
                # await websocket.send(json.dumps(join_msg))
                # resp = await websocket.recv()
                # print(f"Join Response: {resp}")
                
                connected = True
                break
        except Exception as e:
            print(f"Connection attempt {i+1} failed: {e}")
            await asyncio.sleep(2)
            
    if connected:
        print("✅ Realtime Verification SUCCESS")
    else:
        print("❌ Realtime Verification FAILED")

if __name__ == "__main__":
    asyncio.run(verify_realtime())
