from sqlalchemy import Column, String, DateTime, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from datetime import datetime
from core.database import Base

class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    org_id = Column(String, ForeignKey("organizations.id"), nullable=False)
    stripe_invoice_id = Column(String, nullable=True, unique=True)
    amount_due = Column(Integer, default=0) # In cents
    amount_paid = Column(Integer, default=0) # In cents
    status = Column(String, default="draft") # draft, open, paid, uncollectible, void
    invoice_pdf = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    organization = relationship("Organization")
