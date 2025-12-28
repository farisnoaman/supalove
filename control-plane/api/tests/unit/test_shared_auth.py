import pytest
from unittest.mock import patch, MagicMock, ANY
import uuid
from datetime import datetime, timezone, timedelta
from jose import jwt

# We use the 'client' fixture from conftest.py

@pytest.mark.asyncio
async def test_signup_success(client):
    """Test successful signup flow with stable UUIDs."""
    project_id = "test-project-id"
    test_email = "test@example.com"
    test_jwt_secret = "test-jwt-secret-123"
    stable_uuid = "24f421e7-be4d-44a6-9ea6-b7a62f0acbd7"
    
    with patch("api.v1.shared_auth.get_project_db_connection") as mock_get_conn:
        mock_get_conn.return_value = {
            "host": "localhost",
            "port": 5435,
            "database": "test_db",
            "user": "test_user",
            "password": "test_password",
            "jwt_secret": test_jwt_secret,
            "project": MagicMock(id=project_id)
        }
        
        with patch("api.v1.shared_auth.get_auth_db_cursor") as mock_get_cursor:
            with patch("uuid.uuid4", return_value=uuid.UUID(stable_uuid)):
                mock_conn = MagicMock()
                mock_cursor = MagicMock()
                mock_get_cursor.return_value = (mock_conn, mock_cursor)
                
                now = datetime.now(timezone.utc)
                mock_cursor.fetchone.side_effect = [
                    None, 
                    (stable_uuid, test_email, "hashed_pw", now, now, now, "authenticated", "authenticated")
                ]
                
                payload = {
                    "email": test_email,
                    "password": "securepassword123"
                }
                
                response = await client.post(
                    f"/api/v1/projects/{project_id}/auth/v1/signup",
                    json=payload
                )
                
                assert response.status_code == 200
                data = response.json()
                assert data["user"]["id"] == stable_uuid
                
                # Verify JWT signing
                decoded = jwt.decode(data["access_token"], test_jwt_secret, algorithms=["HS256"], audience="authenticated")
                assert decoded["sub"] == stable_uuid

@pytest.mark.asyncio
async def test_login_success(client):
    """Test successful login with password verification."""
    project_id = "test-project-id"
    test_email = "login@test.com"
    test_password = "password123"
    test_jwt_secret = "jwt-secret"
    
    from api.v1.shared_auth import pwd_context
    hashed_password = pwd_context.hash(test_password)
    
    with patch("api.v1.shared_auth.get_project_db_connection") as mock_get_conn:
        mock_get_conn.return_value = {
            "jwt_secret": test_jwt_secret,
            "project": MagicMock(),
            "host": "h", "port": 1, "database": "d", "user": "u", "password": "p"
        }
        
        with patch("api.v1.shared_auth.get_auth_db_cursor") as mock_get_cursor:
            mock_conn = MagicMock()
            mock_cursor = MagicMock()
            mock_get_cursor.return_value = (mock_conn, mock_cursor)
            
            user_id = str(uuid.uuid4())
            now = datetime.now(timezone.utc)
            user_row = (user_id, test_email, hashed_password, now, now, now, "authenticated", "authenticated", "{}", "{}")
            mock_cursor.fetchone.return_value = user_row
            
            response = await client.post(
                f"/api/v1/projects/{project_id}/auth/v1/token",
                json={"email": test_email, "password": test_password},
                params={"grant_type": "password"}
            )
            
            assert response.status_code == 200
            data = response.json()
            assert data["user"]["id"] == user_id
            
            # Verify update_at was called (last_sign_in simulation)
            mock_cursor.execute.assert_any_call(
                "UPDATE auth.users SET updated_at = %s WHERE id = %s",
                (ANY, user_id)
            )

@pytest.mark.asyncio
async def test_login_invalid_password(client):
    """Test login fails with wrong password."""
    project_id = "test-project-id"
    from api.v1.shared_auth import pwd_context
    valid_hash = pwd_context.hash("realpassword")
    
    with patch("api.v1.shared_auth.get_project_db_connection") as mock_get_conn:
        mock_get_conn.return_value = {"jwt_secret": "s"}
        with patch("api.v1.shared_auth.get_auth_db_cursor") as mock_get_cursor:
            _, mock_cursor = MagicMock(), MagicMock()
            mock_get_cursor.return_value = (MagicMock(), mock_cursor)
            
            # Return user with correct-looking hash but wrong password
            mock_cursor.fetchone.return_value = (uuid.uuid4(), "t@t.com", valid_hash, datetime.now(timezone.utc), datetime.now(timezone.utc), None, "role", "aud", "{}", "{}")
            
            response = await client.post(
                f"/api/v1/projects/{project_id}/auth/v1/token",
                json={"email": "t@t.com", "password": "WRONG_PASSWORD"}
            )
            
            assert response.status_code == 400
            assert "invalid_grant" in response.text

@pytest.mark.asyncio
async def test_get_user_success(client):
    """Test fetching current user details using valid JWT."""
    project_id = "test-project-id"
    user_id = str(uuid.uuid4())
    test_jwt_secret = "verify-secret"
    
    now = datetime.now(timezone.utc)
    # Generate token
    token = jwt.encode({
        "sub": user_id, 
        "aud": "authenticated", 
        "role": "authenticated",
        "exp": int((now + timedelta(hours=1)).timestamp())
    }, test_jwt_secret)
    
    with patch("api.v1.shared_auth.get_project_db_connection") as mock_get_conn:
        mock_get_conn.return_value = {"jwt_secret": test_jwt_secret}
        with patch("api.v1.shared_auth.get_auth_db_cursor") as mock_get_cursor:
            _, mock_cursor = MagicMock(), MagicMock()
            mock_get_cursor.return_value = (MagicMock(), mock_cursor)
            
            mock_cursor.fetchone.return_value = (user_id, "me@test.com", "pw", now, now, now, "authenticated", "authenticated", "{}", "{}")
            
            headers = {"Authorization": f"Bearer {token}"}
            response = await client.get(
                f"/api/v1/projects/{project_id}/auth/v1/user",
                headers=headers
            )
            
            assert response.status_code == 200
            assert response.json()["id"] == user_id
