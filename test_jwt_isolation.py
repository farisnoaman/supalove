#!/usr/bin/env python3
"""
Test script to verify per-project JWT secret isolation
Tests that shared projects get unique JWT secrets
"""
import sys
import os

# Add the API source to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'control-plane', 'api', 'src'))

def test_per_project_jwt_secrets():
    """Verify that shared projects get unique JWT secrets"""
    from core.database import SessionLocal
    from models.project import Project
    from models.project_secret import ProjectSecret
    from services.secrets_service import generate_project_secrets
    
    db = SessionLocal()
    
    try:
        print("Testing Per-Project JWT Secrets for Shared Projects")
        print("=" * 60)
        
        # Find two shared projects
        shared_projects = db.query(Project).filter(Project.plan == "shared").limit(2).all()
        
        if len(shared_projects) < 2:
            print("❌ Need at least 2 shared projects to test. Found:", len(shared_projects))
            return False
        
        project1 = shared_projects[0]
        project2 = shared_projects[1]
        
        # Get JWT secrets
        secrets1 = db.query(ProjectSecret).filter(
            ProjectSecret.project_id == project1.id,
            ProjectSecret.key == "JWT_SECRET"
        ).first()
        
        secrets2 = db.query(ProjectSecret).filter(
            ProjectSecret.project_id == project2.id,
            ProjectSecret.key == "JWT_SECRET"
        ).first()
        
        if not secrets1 or not secrets2:
            print("❌ One or both projects missing JWT_SECRET")
            return False
        
        print(f"\nProject 1: {project1.name} ({project1.id})")
        print(f"  JWT Secret (first 20 chars): {secrets1.value[:20]}...")
        print(f"  JWT Secret length: {len(secrets1.value)}")
        
        print(f"\nProject 2: {project2.name} ({project2.id})")
        print(f"  JWT Secret (first 20 chars): {secrets2.value[:20]}...")
        print(f"  JWT Secret length: {len(secrets2.value)}")
        
        # Verify they are different
        if secrets1.value == secrets2.value:
            print("\n❌ FAIL: Both projects have the SAME JWT secret!")
            print("   This means they are still using shared JWT secret")
            return False
        
        # Verify they are not the default shared secret
        shared_jwt_secret = os.getenv("SHARED_JWT_SECRET", "super-secret-jwt-token-with-at-least-32-characters-long")
        
        if secrets1.value == shared_jwt_secret or secrets2.value == shared_jwt_secret:
            print("\n❌ FAIL: One or both projects using SHARED_JWT_SECRET from environment")
            return False
        
        print("\n✅ PASS: Projects have unique JWT secrets")
        print("✅ PASS: Neither project uses shared JWT secret")
        print("\n" + "=" * 60)
        print("JWT isolation is working correctly!")
        
        return True
        
    except Exception as e:
        print(f"❌ Error during test: {e}")
        import traceback
        traceback.print_exc()
        return False
    finally:
        db.close()


if __name__ == "__main__":
    success = test_per_project_jwt_secrets()
    sys.exit(0 if success else 1)
