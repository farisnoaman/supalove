from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime
from core.database import Base

class UsageRecord(Base):
    __tablename__ = "usage_records"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    org_id = Column(String, ForeignKey("organizations.id"), nullable=False)
    
    # Snapshot Data
    projects_count = Column(Integer, default=0)
    database_size_mb = Column(Integer, default=0)
    storage_size_mb = Column(Integer, default=0)
    api_requests_count = Column(Integer, default=0)
    
    recorded_at = Column(DateTime, default=datetime.utcnow)
