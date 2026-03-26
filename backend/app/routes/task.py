from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.config.database import SessionLocal
from app.models.task import Task
from app.schemas.task_schema import TaskCreate
from app.utils.dependencies import get_current_user

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_task(
    task: TaskCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    new_task = Task(**task.dict())
    db.add(new_task)
    db.commit()
    return new_task

@router.get("/")
def get_tasks(
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return db.query(Task).all()

@router.delete("/{id}")
def delete_task(
    id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    if user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Admin only")

    task = db.query(Task).filter(Task.id == id).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(task)
    db.commit()

    return {"message": "Deleted"}