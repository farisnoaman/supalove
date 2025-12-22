import pytest
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import Generator, AsyncGenerator
from fastapi.testclient import TestClient
from httpx import AsyncClient, ASGITransport

# Set env vars for testing before imports
os.environ["TESTING"] = "true"
os.environ["DATABASE_URL"] = "postgresql://platform:platform@localhost:5433/control_plane"
os.environ["PLATFORM_JWT_SECRET"] = "super-secret-test-key" 
# NOTE: In a real CI, we'd use a separate test DB. For MVP, we use the local dev DB but with transaction rollbacks.

from main import app
from api.v1.deps import get_db
from core.database import Base

# Setup DB connection
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="session")
def db_engine():
    # Create tables if they don't exist
    Base.metadata.create_all(bind=engine)
    yield engine
    # Optional: Base.metadata.drop_all(bind=engine) # Don't drop for dev speed

@pytest.fixture(scope="function")
def db(db_engine):
    """
    Creates a fresh database session for a test.
    Rolls back transaction after test completes to ensure isolation.
    """
    connection = db_engine.connect()
    transaction = connection.begin()
    session = TestingSessionLocal(bind=connection)
    
    yield session
    
    session.close()
    transaction.rollback()
    connection.close()

@pytest.fixture(scope="function")
async def client(db) -> AsyncGenerator[AsyncClient, None]:
    """
    Async HTTP client that overrides get_db dependency to use the test session.
    """
    def override_get_db():
        try:
            yield db
        finally:
            pass
            
    app.dependency_overrides[get_db] = override_get_db
    
    async with AsyncClient(
        transport=ASGITransport(app=app), 
        base_url="http://test"
    ) as ac:
        yield ac
        
    app.dependency_overrides.clear()

@pytest.fixture
def auth_headers(db):
    """Create a test user and return auth headers with JWT"""
    from services.auth_service import AuthService
    from models.user import User
    import uuid
    
    email = "faris1@faris.com"
    password = "123123123"
    
    # Check if user exists first
    user = db.query(User).filter(User.email == email).first()
    
    if not user:
        # Create user if not exists (fallback)
        hashed = AuthService.get_password_hash(password)
        user = User(id=str(uuid.uuid4()), email=email, hashed_password=hashed, is_active=True)
        db.add(user)
        db.flush()
    
    # Generate JWT for this user
    from jose import jwt
    import datetime
    
    secret = os.getenv("PLATFORM_JWT_SECRET", "super-secret-test-key")
    payload = {
        "sub": user.id,
        "email": email,
        "role": "authenticated",
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }
    token = jwt.encode(payload, secret, algorithm="HS256")
    return {"Authorization": f"Bearer {token}"}
