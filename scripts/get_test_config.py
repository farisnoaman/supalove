#!/usr/bin/env python3
import requests
import json
import os
import sys

API_URL = "http://127.0.0.1:8000"

def get_token():
    # Try to login with defaults
    login_data = {
        "email": "test@example.com",
        "password": "password123"
    }
    
    resp = requests.post(f"{API_URL}/api/v1/auth/login", json=login_data)
    if resp.status_code == 200:
        return resp.json().get("access_token")
    
    # Try to register
    requests.post(f"{API_URL}/api/v1/auth/register", json=login_data)
    resp = requests.post(f"{API_URL}/api/v1/auth/login", json=login_data)
    if resp.status_code == 200:
        return resp.json().get("access_token")
        
    return None

def main():
    token = get_token()
    if not token:
        print(json.dumps({"error": "Could not authenticate"}))
        sys.exit(1)
        
    headers = {"Authorization": f"Bearer {token}"}
    
    # List projects
    resp = requests.get(f"{API_URL}/api/v1/projects", headers=headers)
    projects = resp.json()
    
    project_id = None
    import time
    project_name = f"gateway-test-{int(time.time())}"
    
    # Always create a new one to ensure fresh secrets (Gateway Port)
    resp = requests.get(f"{API_URL}/api/v1/orgs", headers=headers)
    orgs = resp.json()
    if orgs:
        org_id = orgs[0]['id']
        p_resp = requests.post(f"{API_URL}/api/v1/projects", 
            json={"name": project_name, "org_id": org_id}, 
            headers=headers
        )
        if p_resp.status_code in [200, 201]:
            project_id = p_resp.json().get('project_id')
            # Wait for provisioning
            print(f"Project {project_id} creating...", file=sys.stderr)
            time.sleep(5)
        else:
            print(f"Failed to create project: {p_resp.status_code} {p_resp.text}", file=sys.stderr)
    
    if not project_id:
        # Fallback
        if projects:
            project_id = projects[0]['id']
    
    if not project_id:
        print(json.dumps({"error": "No project found and could not create one"}))
        sys.exit(1)
        
    # Get config
    c_resp = requests.get(f"{API_URL}/api/v1/projects/{project_id}/config", headers=headers)
    if c_resp.status_code == 200:
        print(json.dumps(c_resp.json()))
    else:
        print(f"Error getting config: {c_resp.status_code} {c_resp.text}", file=sys.stderr)
        print(json.dumps({"error": "Could not get config", "details": c_resp.text}))
        sys.exit(1)

if __name__ == "__main__":
    main()
