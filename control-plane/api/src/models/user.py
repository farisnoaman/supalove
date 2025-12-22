from sqlalchemy import Column, String, DateTime, Boolean
from datetime import datetime
from core.database import Base
import uuid

class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    avatar_url = Column(String, nullable=True)
    timezone = Column(String, default="UTC")
    preferences = Column(String, nullable=True) # JSON string
    created_at = Column(DateTime, default=datetime.utcnow)
