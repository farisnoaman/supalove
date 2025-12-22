import requests

BASE_URL = "http://localhost:8000/api/v1"

def test_profile():
    # 1. Login
    print("Logging in...")
    resp = requests.post(f"{BASE_URL}/auth/login", json={
        "email": "alice_fix_auth@example.com",
        "password": "password"
    })
    
    if resp.status_code != 200:
        print(f"Login failed: {resp.text}")
        return
            
    token = resp.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    
    # 2. Get Profile
    print("Fetching profile...")
    resp = requests.get(f"{BASE_URL}/users/me", headers=headers)
    print(f"Status: {resp.status_code}")
    print(f"Profile: {resp.json()}")
    assert resp.status_code == 200
    
    # 3. Update Profile
    print("Updating profile...")
    resp = requests.patch(f"{BASE_URL}/users/me", headers=headers, json={
        "full_name": "Alice Updated",
        "timezone": "America/New_York",
        "theme": "dark"
    })
    print(f"Status: {resp.status_code}")
    print(f"Updated Profile: {resp.json()}")
    assert resp.status_code == 200
    
    # 4. Verify Update
    resp = requests.get(f"{BASE_URL}/users/me", headers=headers)
    profile = resp.json()
    assert profile["full_name"] == "Alice Updated"
    assert profile["timezone"] == "America/New_York"
    assert profile["preferences"]["theme"] == "dark"
    
    print("✅ Profile API Verification Successful!")

if __name__ == "__main__":
    test_profile()
