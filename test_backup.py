#!/usr/bin/env python3
"""Test backup creation for shared project"""

import requests

API_URL = "http://localhost:8000/api/v1"
PROJECT_ID = "70e7f1c7be6c"  # The shared project from the error

# Get token (you'll need to replace with actual token)
token = input("Enter your auth token: ").strip()

headers = {"Authorization": f"Bearer {token}"}

print(f"Testing backup creation for project {PROJECT_ID}...")
response = requests.post(
    f"{API_URL}/projects/{PROJECT_ID}/backups",
    headers=headers
)

print(f"\nStatus Code: {response.status_code}")
print(f"Response: {response.text}")

if response.status_code == 500:
    print("\n❌ Error occurred!")
    print("Check backend logs for details")
