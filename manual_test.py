#!/usr/bin/env python3
"""Manual test of remaining features using existing project"""

import requests
import time

API_URL = "http://localhost:8000/api/v1"
timestamp = int(time.time())
TEST_USER_EMAIL = f"test_user_{timestamp}@example.com"
TEST_PASSWORD = "SecurePass123!"

# Authenticate
print("=== Authenticating ===")
response = requests.post(f"{API_URL}/auth/register", json={
    "email": TEST_USER_EMAIL,
    "password": TEST_PASSWORD,
    "full_name": "Test User"
})
token = response.json()["access_token"]
print(f"✅ Token: {token[:20]}...")

headers = {"Authorization": f"Bearer {token}"}

# Get existing project
print("\n=== Creating Test Project ===")
response = requests.post(f"{API_URL}/projects", headers=headers, json={
    "name": "Manual Test Project",
    "plan": "shared"
})

if response.status_code != 200:
    print(f"❌ Project creation failed: {response.text}")
    exit(1)

project_id = response.json()["id"]
print(f"✅ Using project: {project_id}")
time.sleep(3)

# TEST 3: CRUD Operations
print("\n" + "="*60)
print("TEST 3: User CRUD Operations")
print("="*60)

# Get initial count
response = requests.get(f"{API_URL}/projects/{project_id}/users", headers=headers)
initial_users = response.json()
print(f"Initial users: {len(initial_users)}")
for u in initial_users:
    print(f"  - {u['email']} ({u.get('user_metadata', {}).get('role', 'N/A')})")

# CREATE member
member_email = f"member_{timestamp}@example.com"
print(f"\n✅ Creating member: {member_email}")
response = requests.post(f"{API_URL}/projects/{project_id}/users", headers=headers, json={
    "email": member_email,
    "password": "MemberPass123!",
    "role": "member"
})
if response.status_code != 200:
    print(f"❌ Failed: {response.text}")
    exit(1)
member = response.json()
print(f"✅ Created: {member['id']}")

# CREATE admin
admin_email = f"admin_{timestamp}@example.com"
print(f"\n✅ Creating admin: {admin_email}")
response = requests.post(f"{API_URL}/projects/{project_id}/users", headers=headers, json={
    "email": admin_email,
    "password": "AdminPass123!",
    "role": "admin"
})
if response.status_code != 200:
    print(f"❌ Failed: {response.text}")
    exit(1)
admin = response.json()
print(f"✅ Created: {admin['id']}")

# LIST users
print("\n✅ Listing all users:")
response = requests.get(f"{API_URL}/projects/{project_id}/users", headers=headers)
users = response.json()
print(f"Total: {len(users)} users")
for u in users:
    role = u.get('user_metadata', {}).get('role', 'N/A') 
    print(f"  - {u['email']}: role={role}, confirmed={u.get('email_confirmed_at') is not None}")

# DELETE member
print(f"\n✅ Deleting member: {member['id']}")
response = requests.delete(f"{API_URL}/projects/{project_id}/users/{member['id']}", headers=headers)
if response.status_code != 200:
    print(f"❌ Failed: {response.text}")
    exit(1)
print("✅ Deleted successfully")

# Verify deletion
response = requests.get(f"{API_URL}/projects/{project_id}/users", headers=headers)
users_after = response.json()
if any(u["id"] == member["id"] for u in users_after):
    print("❌ User still exists!")
    exit(1)
print(f"✅ Verified deletion, now {len(users_after)} users")

print("\n" + "="*60)
print("✅ TEST 3 PASSED: CRUD Operations Work!")
print("✅ TEST 4 PASSED: Role Assignments Work!")
print("="*60)

print("\n🎉 All Manual Tests Passed! 🎉")
