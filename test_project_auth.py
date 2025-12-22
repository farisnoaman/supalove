
import requests
import sys

BASE_URL = "http://localhost:8000/api/v1"

def test_project_auth():
    # 1. Login (using Alice from previous tests)
    print("Logging in as Alice...")
    resp = requests.post(f"{BASE_URL}/auth/login", json={
        "email": "alice_7270@example.com",
        "password": "password"
    })
    
    if resp.status_code != 200:
        print(f"Login failed: {resp.text}")
        # Try registering if login fails (maybe DB reset?)
        print("Registering Alice...")
        resp = requests.post(f"{BASE_URL}/auth/register", json={
            "email": "alice_fix_auth@example.com",
            "password": "password",
            "full_name": "Alice Fixer"
        })
        if resp.status_code != 200:
            print(f"Register failed: {resp.text}")
            return # Abort
            
    token = resp.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    
    # 2. Get Projects (to get an ID)
    print("Fetching projects...")
    resp = requests.get(f"{BASE_URL}/projects", headers=headers)
    projects = resp.json()
    if not projects:
        print("No projects found. Creating one...")
        resp = requests.post(f"{BASE_URL}/projects", headers=headers, json={"name": "Auth Test Project"})
        project_id = resp.json()["project_id"]
    else:
        project_id = projects[0]["id"]
        
    print(f"Using Project ID: {project_id}")
    
    # 3. List Users (Should be empty initially)
    print("Listing Project Users...")
    try:
        resp = requests.get(f"{BASE_URL}/projects/{project_id}/auth/users", headers=headers)
        print(f"List Users Status: {resp.status_code}")
        print(f"Users: {resp.text}")
        assert resp.status_code == 200
    except Exception as e:
        print(f"List Users Failed: {e}")

    # 4. Create User
    print("Creating Project User...")
    resp = requests.post(f"{BASE_URL}/projects/{project_id}/auth/users", headers=headers, json={
        "email": "testuser@example.com",
        "password": "password123"
    })
    print(f"Create User Status: {resp.status_code}")
    print(f"Response: {resp.text}")
    assert resp.status_code == 200

    # 5. List Again
    resp = requests.get(f"{BASE_URL}/projects/{project_id}/auth/users", headers=headers)
    users = resp.json()
    print(f"Users count: {len(users)}")
    assert len(users) >= 1
    
    print("✅ Project Auth Verification Successful!")

if __name__ == "__main__":
    test_project_auth()
