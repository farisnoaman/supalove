#!/usr/bin/env python3
"""
Test database import with the provided credentials.
"""

import requests
import json

API_URL = "http://localhost:8000"
EMAIL = "faris1@faris.com"
PASSWORD = "123123123"
SQL_FILE = "/home/faris/Documents/MyApps/supalove/vps_logs.md"

print("=" * 70)
print("DATABASE IMPORT TEST - With Authentication")
print("=" * 70)

# Step 1: Login
print(f"\n🔐 Logging in as {EMAIL}...")
login_response = requests.post(
    f"{API_URL}/api/v1/auth/login",
    json={"email": EMAIL, "password": PASSWORD}
)

if login_response.status_code != 200:
    print(f"❌ Login failed: {login_response.status_code}")
    print(login_response.text)
    exit(1)

token = login_response.json().get("access_token")
print(f"✅ Login successful!")
print(f"   Token: {token[:30]}...")

# Step 2: Get projects
print("\n📋 Fetching projects...")
projects_response = requests.get(
    f"{API_URL}/api/v1/projects",
    headers={"Authorization": f"Bearer {token}"}
)

if projects_response.status_code != 200:
    print(f"❌ Failed to fetch projects: {projects_response.status_code}")
    print(projects_response.text)
    exit(1)

projects = projects_response.json()
if not projects:
    print("❌ No projects found!")
    exit(1)

project = projects[0]
project_id = project["id"]
project_name = project.get("name", "Unknown")

print(f"✅ Found {len(projects)} project(s)")
print(f"   Using: {project_name} (ID: {project_id})")

# Step 3: Test import
print("\n" + "=" * 70)
print("TESTING STANDARD SQL IMPORT")
print("=" * 70)

print(f"\n📤 Uploading: {SQL_FILE}")
print(f"   Target: Project {project_id}")
print(f"   Endpoint: /api/v1/projects/{project_id}/import")

try:
    with open(SQL_FILE, 'rb') as f:
        files = {'file': ('vps_dump.sql', f, 'application/sql')}
        headers = {"Authorization": f"Bearer {token}"}
        
        print("\n⏳ Uploading and processing (this may take up to 5 minutes)...")
        print("   Watch for detailed progress in API logs...")
        
        response = requests.post(
            f"{API_URL}/api/v1/projects/{project_id}/import",
            files=files,
            headers=headers,
            timeout=300
        )
        
        print(f"\n📊 Response Status: {response.status_code}")
        
        try:
            data = response.json()
            print(f"\n📋 Response Body:")
            print(json.dumps(data, indent=2))
            
            if response.status_code == 200:
                status = data.get('status')
                message = data.get('message')
                details = data.get('details', [])
                
                if status == 'success':
                    print("\n" + "=" * 70)
                    print("✅ IMPORT SUCCESSFUL!")
                    print("=" * 70)
                    print(f"Message: {message}")
                    if details:
                        print("\nDetails:")
                        for detail in details:
                            for line in detail.split('\n'):
                                if line.strip():
                                    print(f"  {line}")
                                    
                elif status == 'error':
                    print("\n" + "=" * 70)
                    print("❌ IMPORT FAILED (with detailed diagnostics)")
                    print("=" * 70)
                    print(f"Message: {message}")
                    if details:
                        print("\n📝 Error Details:")
                        for i, detail in enumerate(details, 1):
                            print(f"\n  [{i}] {detail[:500]}")
                    print("\n💡 The detailed error messages show exactly what went wrong!")
                    
            else:
                print(f"\n❌ HTTP Error {response.status_code}")
                if 'detail' in data:
                    print(f"Error: {data['detail']}")
                    
        except json.JSONDecodeError:
            print(f"\n❌ Could not parse JSON response")
            print(f"Raw response: {response.text[:500]}")
            
except FileNotFoundError:
    print(f"\n❌ File not found: {SQL_FILE}")
except requests.exceptions.Timeout:
    print(f"\n⏱️ Request timed out after 5 minutes")
    print("The import may still be running. Check API logs for progress.")
except requests.exceptions.RequestException as e:
    print(f"\n❌ Request failed: {e}")
except Exception as e:
    print(f"\n❌ Unexpected error: {e}")

print("\n" + "=" * 70)
print("Test complete!")
print("=" * 70)
