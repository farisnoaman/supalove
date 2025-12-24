
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import os

# Connect to Control Plane DB
DATABASE_URL = "postgresql://platform:platform@localhost:5433/control_plane"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

project_id = "2104626b7d3f"

# New secrets to update/insert
new_secrets = {
    "DB_PORT": "5504",
    "REST_PORT": "5505",
    "REALTIME_PORT": "5602",
    "STORAGE_PORT": "5603",
    "AUTH_PORT": "5604",
    "FUNCTIONS_PORT": "5605",
    "GATEWAY_PORT": "5606",
    "POSTGRES_DB": "app",
    "POSTGRES_USER": "app",
    "ANON_KEY": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiYW5vbiIsImlzcyI6InN1cGFsb3ZlIiwiaWF0IjoxNzY2NTYwMjcxLCJleHAiOjIwODE5MjAyNzF9.UR-jVafUIs6kUpgmhcR8Bcc_ASBToN9yJ_u5yRfGJpE",
    "SERVICE_ROLE_KEY": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoic2VydmljZV9yb2xlIiwiaXNzIjoic3VwYWxvdmUiLCJpYXQiOjE3NjY1NjAyNzEsImV4cCI6MjA4MTkyMDI3MX0._oDqx1h956a15ujdQoCeIq4THpefttCIL9WzBBx1vto"
}

print(f"Updating secrets for project {project_id}...")

try:
    for key, value in new_secrets.items():
        # Check if exists
        result = session.execute(
            text("SELECT 1 FROM project_secrets WHERE project_id = :pid AND key = :key"),
            {"pid": project_id, "key": key}
        ).fetchone()
        
        if result:
            # Update
            session.execute(
                text("UPDATE project_secrets SET value = :value WHERE project_id = :pid AND key = :key"),
                {"value": value, "pid": project_id, "key": key}
            )
            print(f"Updated {key}")
        else:
            # Insert
            session.execute(
                text("INSERT INTO project_secrets (project_id, key, value) VALUES (:pid, :key, :value)"),
                {"pid": project_id, "key": key, "value": value}
            )
            print(f"Inserted {key}")

    session.commit()
    print("✅ Secrets updated successfully!")
except Exception as e:
    session.rollback()
    print(f"❌ Error updating secrets: {e}")
finally:
    session.close()
