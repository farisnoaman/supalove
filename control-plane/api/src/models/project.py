import enum
from sqlalchemy import Column, String, DateTime, Enum, Text
from datetime import datetime
from core.database import Base

class ProjectStatus(str, enum.Enum):
    pending = "pending"
    provisioning = "provisioning"
    running = "running"
    failed = "failed"
    deleting = "deleting"
    deleted = "deleted"
    stopped = "stopped"

class Project(Base):
    __tablename__ = "projects"

    id = Column(String, primary_key=True, index=True)
    owner_id = Column(String, nullable=True) # For future multi-tenant support
    status = Column(Enum(ProjectStatus), default=ProjectStatus.pending)
    last_error = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
