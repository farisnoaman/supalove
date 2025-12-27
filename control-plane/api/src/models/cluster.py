from sqlalchemy import Column, String, Integer, Enum, DateTime, ForeignKey
from core.database import Base
import enum
from datetime import datetime

class ClusterType(str, enum.Enum):
    global_shared = "global_shared"
    private_shared = "private_shared"

class ClusterStatus(str, enum.Enum):
    creating = "creating"  # Pending async provisioning
    running = "running"
    stopped = "stopped"
    failed = "failed"

class Cluster(Base):
    __tablename__ = "clusters"
    
    id = Column(String, primary_key=True)
    type = Column(Enum(ClusterType))
    owner_org_id = Column(String, ForeignKey("organizations.id"), nullable=True)
    status = Column(Enum(ClusterStatus), default=ClusterStatus.creating)
    
    # Connection details
    postgres_host = Column(String, nullable=True)
    postgres_port = Column(Integer, nullable=True)
    api_url = Column(String, nullable=True)
    
    created_at = Column(DateTime, default=datetime.utcnow)
