"""
Shared Auth Service - GoTrue Compatible API

Provides multi-tenant authentication endpoints compatible with Supabase JS Client.
This service handles auth for "Shared" projects that don't have dedicated GoTrue containers.

API Prefix: /projects/{project_id}/auth/v1
"""

import uuid
import secrets
from datetime import datetime, timedelta
from typing import Optional, Dict, Any

from fastapi import APIRouter, HTTPException, Depends, Header, Request
from pydantic import BaseModel
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from jose import jwt

from api.v1.deps import get_db
from models.project import Project

router = APIRouter(prefix="/projects/{project_id}/auth/v1", tags=["Shared Auth"])

# Password hashing - compatible with GoTrue's bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# JWT Settings
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_HOURS = 1
REFRESH_TOKEN_EXPIRE_DAYS = 30


# ============================================
# REQUEST/RESPONSE MODELS
# ============================================

class SignUpRequest(BaseModel):
    email: str  # Using str instead of EmailStr to avoid email-validator dependency
    password: str
    data: Optional[Dict[str, Any]] = None  # user_metadata


class SignInRequest(BaseModel):
    email: str  # Using str instead of EmailStr to avoid email-validator dependency
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    expires_in: int
    expires_at: int
    refresh_token: str
    user: Dict[str, Any]


class UserResponse(BaseModel):
    id: str
    aud: str
    role: str
    email: str
    email_confirmed_at: Optional[str]
    created_at: str
    updated_at: str
    user_metadata: Dict[str, Any]
    app_metadata: Dict[str, Any]


class ErrorResponse(BaseModel):
    error: str
    error_description: str


# ============================================
# HELPER FUNCTIONS
# ============================================

def get_project_db_connection(project_id: str, db: Session):
    """
    Get a direct connection to the project's database.
    Returns connection info and JWT secret.
    """
    from models.cluster import Cluster
    from models.project_secret import ProjectSecret
    
    # Verify project exists
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    
    # Get project secrets
    secrets = db.query(ProjectSecret).filter(
        ProjectSecret.project_id == project_id
    ).all()
    secrets_dict = {s.key: s.value for s in secrets}
    
    if not secrets_dict.get("JWT_SECRET"):
        raise HTTPException(status_code=500, detail="Project JWT secret not found")
    
    # Get cluster connection info (for shared projects)
    if project.cluster_id:
        cluster = db.query(Cluster).filter(Cluster.id == project.cluster_id).first()
        if cluster:
            host = cluster.postgres_host or "localhost"
            port = cluster.postgres_port or 5435
        else:
            host = "localhost"
            port = 5435
    else:
        # Fallback for legacy projects or dedicated projects with direct connection
        host = secrets_dict.get("SHARED_POSTGRES_HOST", "localhost")
        port = int(secrets_dict.get("DB_PORT", "5435"))
    
    return {
        "host": host,
        "port": port,
        "database": project.db_name or f"project_{project_id}",
        # Use project-specific user if available, otherwise fall back to cluster superuser
        "user": secrets_dict.get("POSTGRES_USER", f"{project.db_name}_user"),
        "password": secrets_dict.get("DB_PASSWORD", "postgres"),
        "jwt_secret": secrets_dict.get("JWT_SECRET", ""),
        "project": project
    }


def get_auth_db_cursor(config: dict):
    """Get a cursor to the project's auth schema."""
    import psycopg2
    conn = psycopg2.connect(
        host=config["host"],
        port=config["port"],
        dbname=config["database"],
        user=config["user"],
        password=config["password"]
    )
    return conn, conn.cursor()


def hash_password(password: str) -> str:
    """Hash password using bcrypt (GoTrue compatible)."""
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify password against bcrypt hash."""
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(user_id: str, email: str, role: str, jwt_secret: str, 
                        user_metadata: dict = None, app_metadata: dict = None) -> tuple:
    """
    Create a GoTrue-compatible JWT access token.
    Returns (access_token, expires_at timestamp).
    """
    now = datetime.utcnow()
    expires_at = now + timedelta(hours=ACCESS_TOKEN_EXPIRE_HOURS)
    
    payload = {
        "aud": "authenticated",
        "exp": int(expires_at.timestamp()),
        "iat": int(now.timestamp()),
        "iss": "supalove",
        "sub": user_id,
        "email": email,
        "role": role,
        "user_metadata": user_metadata or {},
        "app_metadata": app_metadata or {}
    }
    
    token = jwt.encode(payload, jwt_secret, algorithm=ALGORITHM)
    return token, int(expires_at.timestamp())


def create_refresh_token() -> str:
    """Generate a secure refresh token."""
    return secrets.token_urlsafe(32)


def format_user_response(user_row: tuple, user_metadata: dict = None, app_metadata: dict = None) -> dict:
    """Format database row into GoTrue-compatible user object."""
    # Expected row: (id, email, encrypted_password, created_at, updated_at, email_confirmed_at, role, aud)
    return {
        "id": str(user_row[0]),
        "aud": user_row[7] if len(user_row) > 7 else "authenticated",
        "role": user_row[6] if len(user_row) > 6 else "authenticated",
        "email": user_row[1],
        "email_confirmed_at": user_row[5].isoformat() if user_row[5] else None,
        "created_at": user_row[3].isoformat() if user_row[3] else datetime.utcnow().isoformat(),
        "updated_at": user_row[4].isoformat() if user_row[4] else datetime.utcnow().isoformat(),
        "user_metadata": user_metadata or {},
        "app_metadata": app_metadata or {}
    }


# ============================================
# AUTH ENDPOINTS
# ============================================

@router.post("/signup", response_model=TokenResponse)
async def signup(
    project_id: str,
    request: SignUpRequest,
    db: Session = Depends(get_db)
):
    """
    Create a new user account.
    Compatible with supabase.auth.signUp()
    """
    config = get_project_db_connection(project_id, db)
    
    try:
        conn, cursor = get_auth_db_cursor(config)
        
        # Check if user already exists
        cursor.execute(
            "SELECT id FROM auth.users WHERE email = %s",
            (request.email,)
        )
        if cursor.fetchone():
            raise HTTPException(
                status_code=400,
                detail={"error": "user_already_exists", "error_description": "User already registered"}
            )
        
        # Create user
        user_id = str(uuid.uuid4())
        hashed_pw = hash_password(request.password)
        now = datetime.utcnow()
        
        # For simplicity, auto-confirm email (can be configurable later)
        cursor.execute("""
            INSERT INTO auth.users (
                id, email, encrypted_password, created_at, updated_at, 
                email_confirmed_at, role, aud, user_metadata, app_metadata
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            RETURNING id, email, encrypted_password, created_at, updated_at, email_confirmed_at, role, aud
        """, (
            user_id, request.email, hashed_pw, now, now, 
            now,  # auto-confirm
            "authenticated", "authenticated",
            str(request.data or {}), "{}"
        ))
        
        user_row = cursor.fetchone()
        conn.commit()
        
        # Generate tokens
        access_token, expires_at = create_access_token(
            user_id=user_id,
            email=request.email,
            role="authenticated",
            jwt_secret=config["jwt_secret"],
            user_metadata=request.data
        )
        refresh_token = create_refresh_token()
        
        # Store refresh token (simplified - in production, store in DB)
        
        user = format_user_response(user_row, request.data, {})
        
        return TokenResponse(
            access_token=access_token,
            token_type="bearer",
            expires_in=ACCESS_TOKEN_EXPIRE_HOURS * 3600,
            expires_at=expires_at,
            refresh_token=refresh_token,
            user=user
        )
        
    except HTTPException:
        raise
    except Exception as e:
        print(f"[SharedAuth] Signup error: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()


@router.post("/token", response_model=TokenResponse)
async def login(
    project_id: str,
    request: SignInRequest,
    grant_type: str = "password",
    db: Session = Depends(get_db)
):
    """
    Sign in with email and password.
    Compatible with supabase.auth.signInWithPassword()
    """
    if grant_type != "password":
        raise HTTPException(status_code=400, detail="Only password grant_type supported")
    
    config = get_project_db_connection(project_id, db)
    
    try:
        conn, cursor = get_auth_db_cursor(config)
        
        # Find user
        cursor.execute("""
            SELECT id, email, encrypted_password, created_at, updated_at, 
                   email_confirmed_at, role, aud, user_metadata, app_metadata
            FROM auth.users 
            WHERE email = %s
        """, (request.email,))
        
        user_row = cursor.fetchone()
        
        if not user_row:
            raise HTTPException(
                status_code=400,
                detail={"error": "invalid_grant", "error_description": "Invalid login credentials"}
            )
        
        # Verify password
        if not verify_password(request.password, user_row[2]):
            raise HTTPException(
                status_code=400,
                detail={"error": "invalid_grant", "error_description": "Invalid login credentials"}
            )
        
        # Parse metadata (stored as text in simplified schema)
        try:
            import json
            user_metadata = json.loads(user_row[8]) if user_row[8] else {}
            app_metadata = json.loads(user_row[9]) if user_row[9] else {}
        except:
            user_metadata = {}
            app_metadata = {}
        
        # Generate tokens
        access_token, expires_at = create_access_token(
            user_id=str(user_row[0]),
            email=user_row[1],
            role=user_row[6] or "authenticated",
            jwt_secret=config["jwt_secret"],
            user_metadata=user_metadata,
            app_metadata=app_metadata
        )
        refresh_token = create_refresh_token()
        
        # Update last_sign_in_at
        cursor.execute(
            "UPDATE auth.users SET updated_at = %s WHERE id = %s",
            (datetime.utcnow(), user_row[0])
        )
        conn.commit()
        
        user = format_user_response(user_row, user_metadata, app_metadata)
        
        return TokenResponse(
            access_token=access_token,
            token_type="bearer",
            expires_in=ACCESS_TOKEN_EXPIRE_HOURS * 3600,
            expires_at=expires_at,
            refresh_token=refresh_token,
            user=user
        )
        
    except HTTPException:
        raise
    except Exception as e:
        print(f"[SharedAuth] Login error: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()


@router.get("/user", response_model=UserResponse)
async def get_user(
    project_id: str,
    authorization: str = Header(...),
    db: Session = Depends(get_db)
):
    """
    Get the current user from JWT token.
    Compatible with supabase.auth.getUser()
    """
    # Extract token from header
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid authorization header")
    
    token = authorization.replace("Bearer ", "")
    
    config = get_project_db_connection(project_id, db)
    
    try:
        # Decode and verify JWT
        payload = jwt.decode(token, config["jwt_secret"], algorithms=[ALGORITHM])
        user_id = payload.get("sub")
        
        if not user_id:
            raise HTTPException(status_code=401, detail="Invalid token")
        
        # Fetch user from DB
        conn, cursor = get_auth_db_cursor(config)
        cursor.execute("""
            SELECT id, email, encrypted_password, created_at, updated_at, 
                   email_confirmed_at, role, aud, user_metadata, app_metadata
            FROM auth.users 
            WHERE id = %s
        """, (user_id,))
        
        user_row = cursor.fetchone()
        
        if not user_row:
            raise HTTPException(status_code=404, detail="User not found")
        
        # Parse metadata
        try:
            import json
            user_metadata = json.loads(user_row[8]) if user_row[8] else {}
            app_metadata = json.loads(user_row[9]) if user_row[9] else {}
        except:
            user_metadata = {}
            app_metadata = {}
        
        return UserResponse(**format_user_response(user_row, user_metadata, app_metadata))
        
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.JWTError as e:
        raise HTTPException(status_code=401, detail=f"Invalid token: {e}")
    except HTTPException:
        raise
    except Exception as e:
        print(f"[SharedAuth] Get user error: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()


@router.post("/logout")
async def logout(
    project_id: str,
    authorization: str = Header(None),
    db: Session = Depends(get_db)
):
    """
    Log out the current user.
    For JWT-based auth, this is mostly a client-side operation.
    Compatible with supabase.auth.signOut()
    """
    # In a stateless JWT system, logout is handled client-side
    # We can optionally blacklist the token here if needed
    return {"message": "Logged out successfully"}
