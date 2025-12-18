from sqlalchemy import Column, String, DateTime
from datetime import datetime
from core.database import Base

class ProjectSecret(Base):
    __tablename__ = "project_secrets"

    project_id = Column(String, primary_key=True)
    key = Column(String, primary_key=True)
    value = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
   