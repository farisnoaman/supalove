from sqlalchemy import Column, String, Integer, ForeignKey
from core.database import Base

class ResourceQuota(Base):
    __tablename__ = "resource_quotas"

    org_id = Column(String, ForeignKey("organizations.id"), primary_key=True)
    max_projects = Column(Integer, default=3)
    max_db_size_mb = Column(Integer, default=1000)
    max_storage_mb = Column(Integer, default=5000)
    max_api_requests_daily = Column(Integer, default=100000)
