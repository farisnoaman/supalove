from core.database import SessionLocal
from models.organization import Organization
from models.resource_quota import ResourceQuota
from models.project import Project
from models.subscription import Subscription

db = SessionLocal()
org_id = "09c58234-02a0-4731-b7c4-6246c550930b"

print(f"Checking Org: {org_id}")

quota = db.query(ResourceQuota).filter(ResourceQuota.org_id == org_id).first()
if quota:
    print(f"Quota - Max Projects: {quota.max_projects}")
else:
    print("No ResourceQuota found for this org!")

projects = db.query(Project).filter(Project.org_id == org_id).all()
print(f"Current Projects Count: {len(projects)}")
for p in projects:
    print(f" - {p.name} ({p.id})")
