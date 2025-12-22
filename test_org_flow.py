import requests
import time
import random

BASE_URL = "http://localhost:8000/api/v1"

def register_user(email, name):
    print(f"Registering {email}...")
    resp = requests.post(f"{BASE_URL}/auth/register", json={
        "email": email,
        "password": "password123",
        "full_name": name
    })
    if resp.status_code == 200:
        return resp.json()["access_token"]
    elif resp.status_code == 400 and "already registered" in resp.text:
         # Login if already exists
         login_resp = requests.post(f"{BASE_URL}/auth/login", json={
             "email": email,
             "password": "password123"
         })
         return login_resp.json()["access_token"]
    else:
        print(f"Failed to register {email}: {resp.text}")
        return None

def main():
    # 1. Register User A
    rand_suffix = str(random.randint(1000, 9999))
    email_a = f"alice_{rand_suffix}@example.com"
    token_a = register_user(email_a, "Alice Owner")
    
    # 2. Register User B
    email_b = f"bob_{rand_suffix}@example.com"
    token_b = register_user(email_b, "Bob Member")

    if not token_a or not token_b:
        print("Failed to get tokens.")
        return

    # 3. User A lists orgs
    headers_a = {"Authorization": f"Bearer {token_a}"}
    resp = requests.get(f"{BASE_URL}/orgs", headers=headers_a)
    orgs_a = resp.json()
    print(f"Alice's Orgs: {len(orgs_a)}")
    print(orgs_a)
    
    org_id_a = orgs_a[0]["id"]

    # 4. User A adds User B
    print(f"Alice adding Bob ({email_b}) to Org {org_id_a}...")
    resp = requests.post(f"{BASE_URL}/orgs/{org_id_a}/members", headers=headers_a, json={
        "email": email_b,
        "role": "member"
    })
    print(f"Add Member Status: {resp.status_code}")
    print(resp.text)

    # 5. User B lists orgs
    headers_b = {"Authorization": f"Bearer {token_b}"}
    resp = requests.get(f"{BASE_URL}/orgs", headers=headers_b)
    orgs_b = resp.json()
    print(f"Bob's Orgs: {len(orgs_b)}")
    print(orgs_b)

    # 6. Test GET /projects
    print("Testing GET /projects for Alice...")
    resp = requests.get(f"{BASE_URL}/projects", headers=headers_a)
    print(f"Projects Status: {resp.status_code}")
    if resp.status_code != 200:
        print(f"Error: {resp.text}")
    else:
        print(f"Projects: {resp.json()}")

    assert len(orgs_b) >= 2, "Bob should be in at least 2 orgs (his own + Alice's)"
    print("✅ Verification Successful!")

if __name__ == "__main__":
    main()
