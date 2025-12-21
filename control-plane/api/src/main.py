
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.append(str(ROOT))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.v1.projects import router as projects_router
from api.v1.database import router as database_router
from api.v1.auth import router as auth_router
from api.v1.storage import router as storage_router
from api.v1.backups import router as backups_router
from api.v1.health import router as health_router
from api.v1.functions import router as functions_router
from api.v1.secrets import router as secrets_router
from api.v1.logs import router as logs_router

from core.database import Base, engine

# 👇 ADD these imports
from models.project import Project
from models.project_secret import ProjectSecret
from models.edge_function import EdgeFunction

Base.metadata.create_all(bind=engine)

from contextlib import asynccontextmanager
from services.scheduler_service import SchedulerService

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    scheduler = SchedulerService()
    scheduler.start()
    yield
    # Shutdown
    scheduler.stop()

app = FastAPI(title="Supabase Cloud Clone", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In prod, specify the dashboard URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# V2 API Normalization
api_v1_prefix = "/api/v1"
app.include_router(projects_router, prefix=f"{api_v1_prefix}/projects", tags=["Projects"])
app.include_router(database_router, prefix=f"{api_v1_prefix}/projects", tags=["Database"])
app.include_router(auth_router, prefix=f"{api_v1_prefix}/projects", tags=["Auth"])
app.include_router(storage_router, prefix=f"{api_v1_prefix}/projects", tags=["Storage"])
app.include_router(backups_router, prefix=f"{api_v1_prefix}/projects", tags=["Backups"])
app.include_router(health_router, prefix=f"{api_v1_prefix}", tags=["Health"])
app.include_router(functions_router, prefix=f"{api_v1_prefix}/projects", tags=["Functions"])
app.include_router(secrets_router, prefix=f"{api_v1_prefix}/projects", tags=["Secrets"])
app.include_router(logs_router, prefix=f"{api_v1_prefix}/projects", tags=["Logs"])
