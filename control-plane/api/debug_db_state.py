from core.database import SessionLocal
from models.organization import Organization
from models.organization_entitlement import OrganizationEntitlement
from models.plan import Plan
from models.project import Project
from models.subscription import Subscription

db = SessionLocal()
org_id = "09c58234-02a0-4731-b7c4-6246c550930b"

print(f"Checking Org: {org_id}")

ent = db.query(OrganizationEntitlement).filter(OrganizationEntitlement.org_id == org_id).first()
if ent:
    plan = db.query(Plan).filter(Plan.id == ent.plan_id).first()
    print(f"Plan: {plan.name} ({plan.id})")
    print(f"Projects Used: {ent.projects_used} / {plan.max_projects}")
else:
    print("No Entitlement found for this org!")

projects = db.query(Project).filter(Project.org_id == org_id).all()
print(f"Current Projects Count: {len(projects)}")
for p in projects:
    print(f" - {p.name} ({p.id})")
