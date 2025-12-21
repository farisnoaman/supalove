from sqlalchemy import Column, String, Text, DateTime
from datetime import datetime
from core.database import Base

class EdgeFunction(Base):
    __tablename__ = "edge_functions"
    
    id = Column(String, primary_key=True)
    project_id = Column(String, nullable=False, index=True)
    name = Column(String, nullable=False)
    code = Column(Text, nullable=False)
    runtime = Column(String, default="deno")
    version = Column(String, default="1.0.0")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f"<EdgeFunction(id={self.id}, name={self.name}, project_id={self.project_id})>"
