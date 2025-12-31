#!/usr/bin/env python3
"""
Test script to verify SQL editor database isolation
"""
import requests
import json
import sys

API_URL = "http://localhost:8000"

def get_token():
    """Get auth token - you'll need to update with valid credentials"""
    # You may need to login first and get token
    # For now, we'll try to read from a file or env
    try:
        with open('/tmp/supalove_token.txt', 'r') as f:
            return f.read().strip()
    except:
        print("Please login first and save token to /tmp/supalove_token.txt")
        return None

def test_sql_editor(project_id: str, sql: str):
    """Test SQL editor endpoint"""
    token = get_token()
    if not token:
        print("No token available")
        return
    
    url = f"{API_URL}/api/v1/projects/{project_id}/sql"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    data = {"sql": sql}
    
    print(f"\n{'='*60}")
    print(f"Testing Project: {project_id}")
    print(f"SQL: {sql}")
    print(f"{'='*60}")
    
    response = requests.post(url, headers=headers, json=data)
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    
    return response.json()

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python test_sql_isolation.py <project_id> <sql_query>")
        print("Example: python test_sql_isolation.py abc123 'SELECT current_database(), current_user'")
        sys.exit(1)
    
    project_id = sys.argv[1]
    sql = sys.argv[2]
    
    test_sql_editor(project_id, sql)
