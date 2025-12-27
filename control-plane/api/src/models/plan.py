from sqlalchemy import Column, String, Integer, JSON, Enum, Boolean
from core.database import Base
import enum

class ClusterStrategy(str, enum.Enum):
    global_only = "global_only"
    private_per_org = "private_per_org"

class Plan(Base):
    __tablename__ = "plans"
    
    id = Column(String, primary_key=True)  # free, pro, premium
    name = Column(String, nullable=False)
    monthly_price = Column(Integer, default=0)  # In cents
    
    # Entitlements
    max_projects = Column(Integer, default=2)
    max_private_clusters = Column(Integer, default=0)
    
    # Strategy
    cluster_strategy = Column(Enum(ClusterStrategy), default=ClusterStrategy.global_only)
    allow_shared_fallback = Column(Boolean, default=True) # Important for hybrid setups
    
    # Quotas
    max_db_size_mb = Column(Integer, default=500)
    max_storage_mb = Column(Integer, default=1024)
    rate_limit_rps = Column(Integer, default=20)
    
    # Additional features as JSON
    features = Column(JSON, default={})
