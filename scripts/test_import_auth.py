#!/usr/bin/env python3
"""
Test the database import with proper authentication.
"""

import requests
import json

API_URL = "http://localhost:8000"

# Step 1: Login to get a token
print("🔐 Logging in...")
login_response = requests.post(
    f"{API_URL}/api/v1/auth/login",
    json={
        "email": "admin@example.com",
        "password": "admin123"
    }
)

if login_response.status_code == 200:
    token_data = login_response.json()
    token = token_data.get("access_token")
    print(f"✅ Logged in successfully")
    print(f"Token: {token[:20]}...")
    
    # Step 2: Get projects
    print("\n📋 Fetching projects...")
    projects_response = requests.get(
        f"{API_URL}/api/v1/projects",
        headers={"Authorization": f"Bearer {token}"}
    )
    
    if projects_response.status_code == 200:
        projects = projects_response.json()
        if projects:
            project_id = projects[0]["id"]
            print(f"✅ Found project: {project_id}")
            
            # Step 3: Test import
            print(f"\n🧪 Testing import for project {project_id}...")
            sql_file = "/home/faris/Documents/MyApps/supalove/vps_logs.md"
            
            with open(sql_file, 'rb') as f:
                files = {'file': ('vps_dump.sql', f, 'text/plain')}
                headers = {"Authorization": f"Bearer {token}"}
                
                print("📤 Uploading SQL dump (this may take a few minutes)...")
                import_response = requests.post(
                    f"{API_URL}/api/v1/projects/{project_id}/import",
                    files=files,
                    headers=headers,
                    timeout=300
                )
                
                print(f"\n📊 Response Status: {import_response.status_code}")
                
                try:
                    data = import_response.json()
                    print(f"\n📋 Response:")
                    print(json.dumps(data, indent=2))
                    
                    if data.get('status') == 'success':
                        print("\n✅ IMPORT SUCCESSFUL!")
                    elif data.get('status') == 'error':
                        print("\n⚠️ Import failed with detailed error:")
                        if 'message' in data:
                            print(f"Message: {data['message']}")
                        if 'details' in data:
                            print("\nDetails:")
                            for detail in data.get('details', []):
                                print(f"  {detail}")
                except json.JSONDecodeError:
                    print(f"Raw response: {import_response.text}")
        else:
            print("❌ No projects found")
    else:
        print(f"❌ Failed to get projects: {projects_response.status_code}")
        print(projects_response.text)
else:
    print(f"❌ Login failed: {login_response.status_code}")
    print(login_response.text)
