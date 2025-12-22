import uuid
from sqlalchemy import Column, String, Boolean, ForeignKey, BigInteger
from sqlalchemy.orm import relationship
from core.database import Base
import time

class ProjectUser(Base):
    __tablename__ = "project_users"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    project_id = Column(String, ForeignKey("projects.id"), index=True)
    email = Column(String, index=True)
    # in a real supalove, we'd hash this, but this is a mock/metadata layer
    # or we don't store password here, we just proxy to data plane.
    # For now, store nothing sensitive or just dummy hash.
    username = Column(String, nullable=True)
    enabled = Column(Boolean, default=True)
    createdTimestamp = Column(BigInteger, default=lambda: int(time.time() * 1000))
    
    # We could store a reference to the real ID in the data plane
    # real_user_id = Column(String, nullable=True) 

    # project = relationship("Project", back_populates="users")
