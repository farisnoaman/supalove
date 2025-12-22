from core.database import Base, engine
from models.user import User
from models.organization import Organization
from models.org_member import OrgMember
from models.project import Project
from models.project_secret import ProjectSecret
from models.resource_quota import ResourceQuota

print("Dropping all tables...")
Base.metadata.drop_all(bind=engine)
print("Creating all tables...")
Base.metadata.create_all(bind=engine)
print("Database reset complete.")
