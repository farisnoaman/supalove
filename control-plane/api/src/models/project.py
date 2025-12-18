from sqlalchemy import Column, String, DateTime
from datetime import datetime
from core.database import Base

class Project(Base):
    __tablename__ = "projects"

    id = Column(String, primary_key=True, index=True)
    status = Column(String, default="provisioning")
    created_at = Column(DateTime, default=datetime.utcnow)
