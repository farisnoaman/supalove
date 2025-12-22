import sys
from pathlib import Path
from sqlalchemy import text
from core.database import engine

def add_columns():
    print("Adding 'timezone' and 'preferences' columns to 'users' table...")
    with engine.connect() as conn:
        try:
            conn.execute(text("ALTER TABLE users ADD COLUMN timezone VARCHAR DEFAULT 'UTC'"))
            print("Added 'timezone' column.")
        except Exception as e:
            print(f"Skipping 'timezone': {e}")
            
        try:
            conn.execute(text("ALTER TABLE users ADD COLUMN preferences VARCHAR"))
            print("Added 'preferences' column.")
        except Exception as e:
            print(f"Skipping 'preferences': {e}")
            
        conn.commit()
    print("Migration complete.")

if __name__ == "__main__":
    add_columns()
