import requests
import json

BASE_URL = "http://localhost:8000/api/v1"
PROJECT_ID = "29315029c9e7"

def test_endpoint(path, name):
    print(f"Testing {name} ({path})...")
    try:
        resp = requests.get(f"{BASE_URL}{path}", timeout=5)
        print(f"Status: {resp.status_code}")
        print(f"Response: {json.dumps(resp.json(), indent=2)[:200]}...")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_endpoint("/health", "Health")
    test_endpoint(f"/projects/{PROJECT_ID}/secrets", "Secrets")
    test_endpoint(f"/projects/{PROJECT_ID}/logs?service=database&lines=5", "Logs")
