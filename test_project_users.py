#!/usr/bin/env python3
"""
Comprehensive Test Suite for Project User Management (API-only version)
Tests auto-admin creation, CRUD operations, role management, and isolation
"""

import requests
import time
import sys
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

API_URL = "http://localhost:8000/api/v1"

# Use unique email to avoid quota limits
timestamp = int(time.time())
TEST_USER_EMAIL = f"test_user_{timestamp}@example.com"
TEST_PASSWORD = "SecurePass123!"

class TestRunner:
    def __init__(self):
        self.token = None
        self.test_email = TEST_USER_EMAIL
        self.test_password = TEST_PASSWORD
        self.projects = []
        
    def authenticate(self):
        """Register and get authentication token"""
        logger.info("Authenticating...")
        try:
            response = requests.post(f"{API_URL}/auth/register", json={
                "email": self.test_email,
                "password": self.test_password,
                "full_name": "Test User"
            })
            
            if response.status_code == 200:
                self.token = response.json()["access_token"]
                logger.info("✅ Authentication successful")
                return True
            else:
                logger.error(f"Authentication failed: {response.text}")
                return False
        except Exception as e:
            logger.error(f"Authentication error: {e}")
            return False
    
    def create_project(self, name="Test Project"):
        """Create a new shared project"""
        logger.info(f"Creating project: {name}")
        headers = {"Authorization": f"Bearer {self.token}"}
        
        response = requests.post(f"{API_URL}/projects", headers=headers, json={
            "name": name,
            "plan": "shared"
        })
        
        if response.status_code != 200:
            logger.error(f"Project creation failed: {response.text}")
            return None
            
        project = response.json()
        project_id = project["id"]
        logger.info(f"✅ Project created: {project_id}")
        self.projects.append(project_id)
        
        # Wait for provisioning
        time.sleep(5)
        return project_id
    
    def test_auto_admin_creation(self):
        """Test 1: Auto-admin user is created on project setup"""
        logger.info("\n" + "="*60)
        logger.info("TEST 1: Auto-Admin Creation")
        logger.info("="*60)
        
        project_id = self.create_project("Auto-Admin Test")
        if not project_id:
            return False
        
        headers = {"Authorization": f"Bearer {self.token}"}
        
        # List users - should include auto-created admin
        response = requests.get(f"{API_URL}/projects/{project_id}/users", headers=headers)
        if response.status_code != 200:
            logger.error(f"❌ TEST 1 FAILED: Could not list users: {response.text}")
            return False
        
        users = response.json()
        
        # Should have at least one user (the admin)
        if len(users) == 0:
            logger.error("❌ TEST 1 FAILED: No users found in project")
            return False
        
        # Check if admin user exists with correct email
        admin_user = next((u for u in users if u["email"] == self.test_email), None)
        if not admin_user:
            logger.error(f"❌ TEST 1 FAILED: Admin user with email {self.test_email} not found")
            return False
        
        logger.info(f"✅ Found admin user: {admin_user['email']}")
        logger.info("✅ TEST 1 PASSED: Auto-admin created successfully")
        return True
    
    def test_admin_password_retrieval(self):
        """Test 2: Admin password can be retrieved once"""
        logger.info("\n" + "="*60)
        logger.info("TEST 2: Admin Password Retrieval")
        logger.info("="*60)
        
        project_id = self.create_project("Password Test")
        if not project_id:
            return False
        
        headers = {"Authorization": f"Bearer {self.token}"}
        
        # First retrieval should succeed
        response = requests.get(f"{API_URL}/projects/{project_id}/admin-password", headers=headers)
        if response.status_code != 200:
            logger.error(f"❌ TEST 2 FAILED: Could not retrieve password: {response.text}")
            return False
        
        password_data = response.json()
        if not password_data.get("password"):
            logger.error("❌ TEST 2 FAILED: No password in response")
            return False
        
        logger.info(f"✅ Password retrieved: {password_data['password'][:4]}... (16 chars)")
        
        # Verify password length and complexity
        password = password_data['password']
        if len(password) != 16:
            logger.error(f"❌ TEST 2 FAILED: Password should be 16 chars, got {len(password)}")
            return False
        
        # Second retrieval should fail (one-time access)
        response = requests.get(f"{API_URL}/projects/{project_id}/admin-password", headers=headers)
        if response.status_code != 404:
            logger.error(f"❌ TEST 2 FAILED: Password should be deleted after first retrieval, got {response.status_code}")
            return False
        
        logger.info("✅ TEST 2 PASSED: One-time password access works")
        return True
    
    def test_user_crud_operations(self):
        """Test 3: Create, List, and Delete users"""
        logger.info("\n" + "="*60)
        logger.info("TEST 3: User CRUD Operations")
        logger.info("="*60)
        
        project_id = self.create_project("CRUD Test")
        if not project_id:
            return False
        
        headers = {"Authorization": f"Bearer {self.token}"}
        
        # Get initial user count
        response = requests.get(f"{API_URL}/projects/{project_id}/users", headers=headers)
        initial_users = response.json()
        initial_count = len(initial_users)
        logger.info(f"Initial user count: {initial_count}")
        
        # CREATE: Add a new user
        new_user_email = f"member_{timestamp}@example.com"
        response = requests.post(f"{API_URL}/projects/{project_id}/users", headers=headers, json={
            "email": new_user_email,
            "password": "MemberPass123!",
            "role": "member"
        })
        
        if response.status_code != 200:
            logger.error(f"❌ TEST 3 FAILED: Could not create user: {response.text}")
            return False
        
        user_data = response.json()
        user_id = user_data["id"]
        logger.info(f"✅ Created user: {user_id}, email: {new_user_email}")
        
        # READ: List users
        response = requests.get(f"{API_URL}/projects/{project_id}/users", headers=headers)
        if response.status_code != 200:
            logger.error(f"❌ TEST 3 FAILED: Could not list users: {response.text}")
            return False
        
        users = response.json()
        if len(users) != initial_count + 1:
            logger.error(f"❌ TEST 3 FAILED: Expected {initial_count + 1} users, got {len(users)}")
            return False
        
        # Verify new user is in list
        if not any(u["id"] == user_id for u in users):
            logger.error("❌ TEST 3 FAILED: Created user not found in list")
            return False
        
        logger.info(f"✅ Listed {len(users)} users")
        
        # DELETE: Remove user
        response = requests.delete(f"{API_URL}/projects/{project_id}/users/{user_id}", headers=headers)
        if response.status_code != 200:
            logger.error(f"❌ TEST 3 FAILED: Could not delete user: {response.text}")
            return False
        
        logger.info(f"✅ Deleted user: {user_id}")
        
        # Verify deletion
        response = requests.get(f"{API_URL}/projects/{project_id}/users", headers=headers)
        users_after = response.json()
        if any(u["id"] == user_id for u in users_after):
            logger.error("❌ TEST 3 FAILED: User still exists after deletion")
            return False
        
        if len(users_after) != initial_count:
            logger.error(f"❌ TEST 3 FAILED: User count should be {initial_count}, got {len(users_after)}")
            return False
        
        logger.info("✅ TEST 3 PASSED: CRUD operations work correctly")
        return True
    
    def test_role_assignments(self):
        """Test 4: Different role assignments"""
        logger.info("\n" + "="*60)
        logger.info("TEST 4: Role Assignments")
        logger.info("="*60)
        
        project_id = self.create_project("Role Test")
        if not project_id:
            return False
        
        headers = {"Authorization": f"Bearer {self.token}"}
        
        # Create admin user
        admin_email = f"admin_{timestamp}@example.com"
        response = requests.post(f"{API_URL}/projects/{project_id}/users", headers=headers, json={
            "email": admin_email,
            "password": "AdminPass123!",
            "role": "admin"
        })
        
        if response.status_code != 200:
            logger.error(f"❌ TEST 4 FAILED: Could not create admin: {response.text}")
            return False
        
        admin_user = response.json()
        logger.info(f"✅ Created admin: {admin_email}")
        
        # Create member user
        member_email = f"member2_{timestamp}@example.com"
        response = requests.post(f"{API_URL}/projects/{project_id}/users", headers=headers, json={
            "email": member_email,
            "password": "MemberPass123!",
            "role": "member"
        })
        
        if response.status_code != 200:
            logger.error(f"❌ TEST 4 FAILED: Could not create member: {response.text}")
            return False
        
        member_user = response.json()
        logger.info(f"✅ Created member: {member_email}")
        
        # Verify users exist in list
        response = requests.get(f"{API_URL}/projects/{project_id}/users", headers=headers)
        users = response.json()
        
        found_admin = next((u for u in users if u["email"] == admin_email), None)
        found_member = next((u for u in users if u["email"] == member_email), None)
        
        if not found_admin or not found_member:
            logger.error("❌ TEST 4 FAILED: Users not found in list")
            return False
        
        # Check metadata for roles
        if found_admin.get("user_metadata", {}).get("role") != "admin":
            logger.error(f"❌ TEST 4 FAILED: Admin has wrong role in metadata")
            return False
        
        if found_member.get("user_metadata", {}).get("role") != "member":
            logger.error(f"❌ TEST 4 FAILED: Member has wrong role in metadata")
            return False
        
        logger.info("✅ TEST 4 PASSED: Role assignments work correctly")
        return True
    
    def test_database_isolation(self):
        """Test 5: Users are isolated between projects"""
        logger.info("\n" + "="*60)
        logger.info("TEST 5: Database Isolation")
        logger.info("="*60)
        
        # Create two projects
        project1 = self.create_project("Isolation Project 1")
        project2 = self.create_project("Isolation Project 2")
        
        if not project1 or not project2:
            return False
        
        headers = {"Authorization": f"Bearer {self.token}"}
        
        # Create unique user in Project 1
        unique_email = f"isolated_{timestamp}@example.com"
        response = requests.post(f"{API_URL}/projects/{project1}/users", headers=headers, json={
            "email": unique_email,
            "password": "IsolatedPass123!",
            "role": "member"
        })
        
        if response.status_code != 200:
            logger.error(f"❌ TEST 5 FAILED: Could not create user in P1: {response.text}")
            return False
        
        logger.info(f"✅ Created user in Project 1: {unique_email}")
        
        # Verify user exists in Project 1
        response = requests.get(f"{API_URL}/projects/{project1}/users", headers=headers)
        users_p1 = response.json()
        if not any(u["email"] == unique_email for u in users_p1):
            logger.error("❌ TEST 5 FAILED: User not found in Project 1")
            return False
        
        # Verify user does NOT exist in Project 2
        response = requests.get(f"{API_URL}/projects/{project2}/users", headers=headers)
        users_p2 = response.json()
        if any(u["email"] == unique_email for u in users_p2):
            logger.error("❌ TEST 5 FAILED: User leaked to Project 2!")
            return False
        
        logger.info(f"✅ User isolated to Project 1 only")
        logger.info("✅ TEST 5 PASSED: Database isolation works correctly")
        return True
    
    def run_all_tests(self):
        """Run complete test suite"""
        logger.info("\n" + "#"*60)
        logger.info("# PROJECT USER MANAGEMENT - COMPREHENSIVE TEST SUITE")
        logger.info("#"*60 + "\n")
        
        if not self.authenticate():
            logger.error("❌ FATAL: Authentication failed")
            return False
        
        results = {
            "Auto-Admin Creation": self.test_auto_admin_creation(),
            "Admin Password Retrieval": self.test_admin_password_retrieval(),
            "User CRUD Operations": self.test_user_crud_operations(),
            "Role Assignments": self.test_role_assignments(),
            "Database Isolation": self.test_database_isolation()
        }
        
        # Summary
        logger.info("\n" + "="*60)
        logger.info("TEST SUMMARY")
        logger.info("="*60)
        
        passed = sum(1 for v in results.values() if v)
        total = len(results)
        
        for test_name, result in results.items():
            status = "✅ PASS" if result else "❌ FAIL"
            logger.info(f"{status} - {test_name}")
        
        logger.info("="*60)
        logger.info(f"RESULTS: {passed}/{total} tests passed")
        logger.info("="*60 + "\n")
        
        if passed == total:
            logger.info("🎉 ALL TESTS PASSED! 🎉")
            return True
        else:
            logger.error(f"❌ {total - passed} test(s) failed")
            return False

if __name__ == "__main__":
    runner = TestRunner()
    success = runner.run_all_tests()
    sys.exit(0 if success else 1)
