import enum
from sqlalchemy import Column, String, DateTime, Enum, Text
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

class Project(Base):
    __tablename__ = "projects"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=True)
    owner_id = Column(String, nullable=True) # For future multi-tenant support
    status = Column(Enum(ProjectStatus), default=ProjectStatus.pending)
    last_error = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
