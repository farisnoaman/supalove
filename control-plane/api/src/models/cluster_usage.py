from sqlalchemy import Column, String, Integer, Float, ForeignKey, DateTime
from datetime import datetime
from core.database import Base

class ClusterUsage(Base):
    __tablename__ = "cluster_usage"
    
    cluster_id = Column(String, ForeignKey("clusters.id"), primary_key=True)
    cpu_percent = Column(Float, default=0.0)
    memory_mb = Column(Integer, default=0)
    active_connections = Column(Integer, default=0)
    db_count = Column(Integer, default=0)
    updated_at = Column(DateTime, default=datetime.utcnow)
