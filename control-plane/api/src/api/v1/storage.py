import io
from fastapi import APIRouter, HTTPException, File, UploadFile, Depends
from pydantic import BaseModel
from services.storage_service import StorageService
from api.v1.utils import verify_project_access
from api.v1.deps import get_db, get_current_user
from sqlalchemy.orm import Session
from models.user import User

router = APIRouter()
storage_service = StorageService()

@router.get("/{project_id}/storage/buckets")
def list_storage_buckets(
    project_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    verify_project_access(project_id, db, current_user)
    try:
        return storage_service.list_buckets(project_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

class CreateBucketRequest(BaseModel):
    name: str

@router.post("/{project_id}/storage/buckets")
def create_storage_bucket(
    project_id: str,
    body: CreateBucketRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    verify_project_access(project_id, db, current_user)
    try:
        bucket_name = storage_service.create_new_bucket(project_id, body.name)
        return {"name": bucket_name}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{project_id}/storage/buckets/{bucket_name}/objects")
def list_storage_objects(
    project_id: str, 
    bucket_name: str, 
    prefix: str = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    verify_project_access(project_id, db, current_user)
    try:
        return storage_service.list_objects(project_id, bucket_name, prefix)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/{project_id}/storage/buckets/{bucket_name}/objects")
async def upload_storage_object(
    project_id: str, 
    bucket_name: str, 
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    verify_project_access(project_id, db, current_user)
    try:
        content = await file.read()
        storage_service.upload_object(
            project_id=project_id,
            bucket_name=bucket_name,
            object_name=file.filename,
            data=io.BytesIO(content),
            length=len(content),
            content_type=file.content_type
        )
        return {"name": file.filename, "size": len(content)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/{project_id}/storage/buckets/{bucket_name}/objects/{object_name:path}")
def delete_storage_object(
    project_id: str, 
    bucket_name: str, 
    object_name: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    verify_project_access(project_id, db, current_user)
    try:
        storage_service.delete_object(project_id, bucket_name, object_name)
        return {"status": "success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
