from core.database import Base, engine
from models.user import User
from models.organization import Organization
from models.org_member import OrgMember
from models.project import Project
from models.project_secret import ProjectSecret
from models.plan import Plan
from models.organization_entitlement import OrganizationEntitlement
from models.cluster import Cluster
from models.cluster_usage import ClusterUsage

print("Dropping all tables...")
Base.metadata.drop_all(bind=engine)
print("Creating all tables...")
Base.metadata.create_all(bind=engine)
print("Database reset complete.")
