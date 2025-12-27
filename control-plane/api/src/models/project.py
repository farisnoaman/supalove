import enum
from sqlalchemy import Column, String, DateTime, Enum, Text, ForeignKey
from datetime import datetime
from core.database import Base

class ProjectStatus(str, enum.Enum):
    CREATING = "creating"         # Initial state, db record created
    PROVISIONING = "provisioning" # Infrastructure being set up
    RUNNING = "running"           # Fully operational
    FAILED = "failed"             # Provisioning or runtime error
    STOPPED = "stopped"           # Intentionally stopped by user
    DELETING = "deleting"         # Cleanup in progress
    DELETED = "deleted"           # Soft deleted / fully removed

class ProjectPlan(str, enum.Enum):
    shared = "shared"       # Runs on shared infrastructure
    dedicated = "dedicated" # Isolated Docker stack per project

class BackendType(str, enum.Enum):
    local_docker = "local_docker"     # Local Docker Compose
    shared_cluster = "shared_cluster" # Shared Postgres cluster
    coolify = "coolify"               # Coolify deployment

class ProjectPlacement(str, enum.Enum):
    private = "private"
    shared = "shared"

class Project(Base):
    __tablename__ = "projects"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=True)
    # Multi-tenancy
    org_id = Column(String, ForeignKey("organizations.id"), nullable=True) # Nullable for migration
    
    # Cluster & Placement
    cluster_id = Column(String, ForeignKey("clusters.id"), nullable=True)  # Nullable for migration
    placement = Column(Enum(ProjectPlacement), default=ProjectPlacement.shared)
    
    # owner_id = Column(String, nullable=True) # Deprecated in favor of org_id
    status = Column(Enum(ProjectStatus), default=ProjectStatus.CREATING)
    last_error = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Shared plan support
    plan = Column(Enum(ProjectPlan), default=ProjectPlan.shared)  # Default to shared
    backend_type = Column(Enum(BackendType), default=BackendType.shared_cluster)
    db_name = Column(String, nullable=True)  # Database name in shared cluster

