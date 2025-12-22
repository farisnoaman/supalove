#!/usr/bin/env python3
"""
Test script to create a new Supalove project with the full Supabase stack.
Run this after starting the backend to verify the integration works.

Usage:
    python test_create_project.py
"""

import requests
import json
import sys
import time

API_URL = "http://127.0.0.1:8000"

def get_token():
    """Get auth token - either from login or use existing"""
    # Try to login with test credentials
    print("🔐 Authenticating...")
    
    # You may need to adjust these credentials
    login_data = {
        "email": "test@example.com",
        "password": "password123"
    }
    
    resp = requests.post(f"{API_URL}/api/v1/auth/login", json=login_data)
    
    if resp.status_code == 200:
        token = resp.json().get("access_token")
        print("✅ Logged in successfully")
        return token
    else:
        print(f"⚠️  Login failed: {resp.status_code}")
        print("   Trying to register new user...")
        
        # Try to register
        resp = requests.post(f"{API_URL}/api/v1/auth/register", json=login_data)
        if resp.status_code in [200, 201]:
            # Now login
            resp = requests.post(f"{API_URL}/api/v1/auth/login", json=login_data)
            if resp.status_code == 200:
                token = resp.json().get("access_token")
                print("✅ Registered and logged in")
                return token
        
        print("❌ Could not authenticate. Please provide a valid token.")
        token = input("Enter your JWT token (or press Enter to exit): ").strip()
        if not token:
            sys.exit(1)
        return token

def create_project(token: str, project_name: str = "test-supabase-stack"):
    """Create a new project"""
    print(f"\n🚀 Creating project: {project_name}")
    
    headers = {"Authorization": f"Bearer {token}"}
    
    # First get the org_id
    resp = requests.get(f"{API_URL}/api/v1/orgs", headers=headers)
    if resp.status_code != 200:
        print(f"❌ Failed to get organizations: {resp.status_code}")
        print(resp.text)
        return None
    
    orgs = resp.json()
    if not orgs:
        print("❌ No organizations found. Please create one first.")
        return None
    
    org_id = orgs[0]["id"]
    print(f"   Using organization: {orgs[0]['name']} ({org_id})")
    
    # Create the project
    project_data = {
        "name": project_name,
        "org_id": org_id
    }
    
    print("   Provisioning project (this may take 30-60 seconds)...")
    start = time.time()
    
    resp = requests.post(f"{API_URL}/api/v1/projects", json=project_data, headers=headers, timeout=120)
    
    elapsed = time.time() - start
    
    if resp.status_code in [200, 201]:
        project = resp.json()
        print(f"✅ Project created in {elapsed:.1f}s!")
        print(f"   Project ID: {project.get('project_id')}")
        return project.get('project_id')
    else:
        print(f"❌ Failed to create project: {resp.status_code}")
        print(resp.text)
        return None

def get_project_config(token: str, project_id: str):
    """Get project configuration (connection strings, keys)"""
    print(f"\n🔗 Getting project configuration...")
    
    headers = {"Authorization": f"Bearer {token}"}
    resp = requests.get(f"{API_URL}/api/v1/projects/{project_id}/config", headers=headers)
    
    if resp.status_code == 200:
        config = resp.json()
        print("✅ Project configuration retrieved!")
        print("\n" + "="*60)
        print("📋 CONNECTION DETAILS")
        print("="*60)
        print(f"\n🌐 API URL:      {config.get('api_url')}")
        print(f"🔐 Auth URL:     {config.get('auth_url')}")
        print(f"⚡ Realtime URL: {config.get('realtime_url')}")
        print(f"📦 Storage URL:  {config.get('storage_url')}")
        print(f"⚙️  Functions:    {config.get('functions_url')}")
        print(f"\n🗄️  Database URL: {config.get('db_url')}")
        print(f"   Host: {config.get('db_host')}")
        print(f"   Port: {config.get('db_port')}")
        print(f"   User: {config.get('db_user')}")
        print(f"   Pass: {config.get('db_pass')[:8]}...")
        print(f"\n🔑 Anon Key:         {config.get('anon_key')[:50]}...")
        print(f"🔑 Service Role Key: {config.get('service_role_key')[:50]}...")
        print("="*60)
        return config
    else:
        print(f"❌ Failed to get config: {resp.status_code}")
        print(resp.text)
        return None

def check_services(config: dict):
    """Check if all services are running"""
    print("\n🏥 Checking service health...")
    
    services = [
        ("API (PostgREST)", config.get("api_url")),
        ("Auth (GoTrue)", config.get("auth_url") + "/health" if config.get("auth_url") else None),
        ("Storage", config.get("storage_url") + "/status" if config.get("storage_url") else None),
    ]
    
    for name, url in services:
        if not url:
            print(f"   ⚠️  {name}: URL not available")
            continue
        try:
            resp = requests.get(url, timeout=5)
            if resp.status_code < 400:
                print(f"   ✅ {name}: Running ({url})")
            else:
                print(f"   ⚠️  {name}: Returned {resp.status_code}")
        except requests.exceptions.ConnectionError:
            print(f"   ❌ {name}: Not reachable ({url})")
        except Exception as e:
            print(f"   ❌ {name}: Error - {e}")

def main():
    print("="*60)
    print("🧪 SUPALOVE PROJECT CREATION TEST")
    print("="*60)
    
    # 1. Authenticate
    token = get_token()
    
    # 2. Create project
    project_id = create_project(token, f"test-stack-{int(time.time())}")
    
    if not project_id:
        print("\n❌ Test failed: Could not create project")
        sys.exit(1)
    
    # 3. Get configuration
    config = get_project_config(token, project_id)
    
    if not config:
        print("\n❌ Test failed: Could not get project config")
        sys.exit(1)
    
    # 4. Check services
    print("\n⏳ Waiting 10 seconds for services to start...")
    time.sleep(10)
    check_services(config)
    
    print("\n" + "="*60)
    print("✅ TEST COMPLETE")
    print("="*60)
    print(f"\nYour project '{project_id}' is ready!")
    print("You can now:")
    print(f"  1. Open the dashboard and navigate to /projects/{project_id}")
    print(f"  2. Click 'Connect' to see connection details")
    print(f"  3. Use the API URL in your app: {config.get('api_url')}")

if __name__ == "__main__":
    main()
