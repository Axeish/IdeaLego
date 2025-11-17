# backend/app/routes/schedule.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import ScheduledItem

from app import crud, schemas
from app.db import get_db

router = APIRouter()

@router.get("/", response_model=list[schemas.ScheduledItemRead])
def read_scheduled_items(db: Session = Depends(get_db)):
    return crud.get_scheduled_items(db)

@router.get("/{scheduled_id}", response_model=schemas.ScheduledItemRead)
def read_scheduled_item(scheduled_id: str, db: Session = Depends(get_db)):
    obj = crud.get_scheduled_item(db, scheduled_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Scheduled item not found")
    return obj

@router.post("/", response_model=schemas.ScheduledItemRead)
def create_scheduled_item(payload: schemas.ScheduledItemCreate, db: Session = Depends(get_db)):
    obj = ScheduledItem(**payload.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj
@router.delete("/{scheduled_id}")
def delete_scheduled_item(scheduled_id: str, db: Session = Depends(get_db)):
    deleted = crud.delete_scheduled_item(db, scheduled_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Scheduled item not found")
    return {"deleted": scheduled_id}
