from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from datetime import datetime
from core.database import Base

class OrganizationEntitlement(Base):
    __tablename__ = "organization_entitlements"
    
    org_id = Column(String, ForeignKey("organizations.id"), primary_key=True)
    plan_id = Column(String, ForeignKey("plans.id"), nullable=False)
    
    # Runtime counters
    projects_used = Column(Integer, default=0)
    private_clusters_used = Column(Integer, default=0)
    
    # Subscription tracking
    expires_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
