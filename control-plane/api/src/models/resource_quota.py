from sqlalchemy import Column, String, Integer, ForeignKey
from core.database import Base

class ResourceQuota(Base):
    __tablename__ = "resource_quotas"

    org_id = Column(String, ForeignKey("organizations.id"), primary_key=True)
    max_projects = Column(Integer, default=3)
    max_db_size_mb = Column(Integer, default=1000)
    max_storage_mb = Column(Integer, default=5000)
    max_api_requests_daily = Column(Integer, default=100000)

    @staticmethod
    def get_defaults(plan: str):
        if plan == "pro":
            return {
                "max_projects": -1, # Unlimited
                "max_db_size_mb": 8192, # 8GB
                "max_storage_mb": 51200, # 50GB
                "max_api_requests_daily": 1000000
            }
        else: # Free
            return {
                "max_projects": 3,
                "max_db_size_mb": 500, # 500MB
                "max_storage_mb": 1024, # 1GB
                "max_api_requests_daily": 100000
            }
