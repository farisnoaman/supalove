
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.append(str(ROOT))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.v1.projects import router as projects_router
from core.database import Base, engine

# 👇 ADD these imports
from models.project import Project
from models.project_secret import ProjectSecret

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Supabase Cloud Clone")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In prod, specify the dashboard URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(projects_router, prefix="/v1")
