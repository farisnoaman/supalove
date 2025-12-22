from sqlalchemy import Column, String, DateTime, ForeignKey, Enum
from datetime import datetime
from core.database import Base
import enum
import uuid

class OrgRole(str, enum.Enum):
    OWNER = "owner"
    ADMIN = "admin"
    MEMBER = "member"

class OrgMember(Base):
    __tablename__ = "org_members"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    org_id = Column(String, ForeignKey("organizations.id"), nullable=False)
    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    role = Column(Enum(OrgRole), default=OrgRole.MEMBER, nullable=False)
    joined_at = Column(DateTime, default=datetime.utcnow)
