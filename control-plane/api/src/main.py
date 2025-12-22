
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
from api.v1.orgs import router as orgs_router

from core.database import Base, engine

# 👇 ADD these imports
from models.project import Project
from models.project_secret import ProjectSecret
from models.edge_function import EdgeFunction
from models.user import User
from models.organization import Organization
from models.org_member import OrgMember
from models.resource_quota import ResourceQuota
from models.project_user import ProjectUser # Import new model

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
# Mount project_auth router under projects/{id}/auth/users? 
# No, usually mounted separately or nested. 
# The frontend calls /api/v1/projects/{id}/auth/users
# So we mount it at /projects/{project_id}/auth/users is cleaner via the router definition
# But the router defines @router.get("") which means root.
# So prefix should be: /api/v1/projects/{project_id}/auth/users is awkward for include_router if project_id is dynamic.

# Better: Mount at /api/v1/projects and let the router handle /{project_id}/auth/users
# But projects_router handles /api/v1/projects.
# We can use a separate prefix or modify projects_router.
# Let's import project_auth_router and mount it with specific prefix structure.

from api.v1.project_auth import router as project_auth_router
# This router expects project_id param.
# If I mount it at /api/v1/projects, it needs to decorate /{project_id}/auth/users
# In project_auth.py I used @router.get("").
# So I should mount it like this:

app.include_router(projects_router, prefix=f"{api_v1_prefix}/projects", tags=["Projects"])
# To support /api/v1/projects/{project_id}/auth/users
# We can mount project_auth_router at /api/v1/projects
# AND change project_auth.py to use `/{project_id}/auth/users` in decorators?
# OR keep main.py clean:

app.include_router(project_auth_router, prefix=f"{api_v1_prefix}/projects/{{project_id}}/auth/users", tags=["Project Auth"])

app.include_router(database_router, prefix=f"{api_v1_prefix}/projects", tags=["Database"])
app.include_router(auth_router, prefix=f"{api_v1_prefix}/auth", tags=["Platform Auth"])
app.include_router(storage_router, prefix=f"{api_v1_prefix}/projects", tags=["Storage"])
app.include_router(backups_router, prefix=f"{api_v1_prefix}/projects", tags=["Backups"])
app.include_router(health_router, prefix=f"{api_v1_prefix}", tags=["Health"])
app.include_router(functions_router, prefix=f"{api_v1_prefix}/projects", tags=["Functions"])
app.include_router(secrets_router, prefix=f"{api_v1_prefix}/projects", tags=["Secrets"])
app.include_router(logs_router, prefix=f"{api_v1_prefix}/projects", tags=["Logs"])
from api.v1.users import router as users_router

app.include_router(users_router, prefix=f"{api_v1_prefix}/users", tags=["Users"])
app.include_router(orgs_router, prefix=f"{api_v1_prefix}/orgs", tags=["Organizations"])
