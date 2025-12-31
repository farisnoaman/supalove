#!/usr/bin/env python3
"""
Verify JWT secret configuration for existing shared projects
Shows which projects have old shared secret vs new unique secrets
"""
import sys
import os

# Add the API source to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'control-plane', 'api', 'src'))

def check_all_shared_projects():
    """Check JWT secrets for all shared projects"""
    from core.database import SessionLocal
    from models.project import Project
    from models.project_secret import ProjectSecret
    
    db = SessionLocal()
    
    try:
        print("JWT Secret Analysis for Shared Projects")
        print("=" * 80)
        
        # Get shared JWT secret from environment
        shared_jwt_secret = os.getenv("SHARED_JWT_SECRET", "super-secret-jwt-token-with-at-least-32-characters-long")
        
        # Find all shared projects
        shared_projects = db.query(Project).filter(Project.plan == "shared").all()
        
        print(f"\nFound {len(shared_projects)} shared projects\n")
        
        old_secret_count = 0
        new_secret_count = 0
        
        for project in shared_projects:
            # Get JWT secret
            jwt_secret = db.query(ProjectSecret).filter(
                ProjectSecret.project_id == project.id,
                ProjectSecret.key == "JWT_SECRET"
            ).first()
            
            if not jwt_secret:
                print(f"⚠️  {project.name} ({project.id}): NO JWT SECRET FOUND")
                continue
            
            # Check if it's the old shared secret
            if jwt_secret.value == shared_jwt_secret:
                print(f"🔴 {project.name} ({project.id}): Using OLD shared secret")
                old_secret_count += 1
            else:
                print(f"✅ {project.name} ({project.id}): Using UNIQUE secret (length: {len(jwt_secret.value)})")
                new_secret_count += 1
        
        print("\n" + "=" * 80)
        print(f"Summary:")
        print(f"  - Projects with old shared secret: {old_secret_count}")
        print(f"  - Projects with unique secrets: {new_secret_count}")
        
        if old_secret_count > 0:
            print(f"\n✅ This is EXPECTED behavior!")
            print(f"   - Old projects keep their existing shared secret")
            print(f"   - NEW projects will get unique secrets")
            print(f"   - Zero breaking changes - existing tokens remain valid")
        
        if new_secret_count > 0:
            print(f"\n🎉 {new_secret_count} project(s) already have unique JWT secrets!")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False
    finally:
        db.close()


if __name__ == "__main__":
    check_all_shared_projects()
