from fastapi import FastAPI
from api.v1.projects import router as projects_router

app = FastAPI(title="Supabase Cloud Clone")

app.include_router(projects_router, prefix="/v1")
