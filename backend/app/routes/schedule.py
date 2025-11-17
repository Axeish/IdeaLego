# backend/app/routes/schedule.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app import crud, schemas
from app.db import get_db

router = APIRouter()

@router.get("/", response_model=List[schemas.ScheduledItemRead])
def read_scheduled_items(db: Session = Depends(get_db)):
    return crud.get_scheduled_items(db)

@router.get("/{scheduled_id}", response_model=schemas.ScheduledItemRead)
def read_scheduled_item(scheduled_id: str, db: Session = Depends(get_db)):
    obj = crud.get_scheduled_item(db, scheduled_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Scheduled item not found")
    return obj

@router.post("/", response_model=schemas.ScheduledItemRead)
def create_scheduled_item(scheduled_item: schemas.ScheduledItemCreate, db: Session = Depends(get_db)):
    return crud.create_scheduled_item(db, scheduled_item)

@router.delete("/{scheduled_id}")
def delete_scheduled_item(scheduled_id: str, db: Session = Depends(get_db)):
    deleted = crud.delete_scheduled_item(db, scheduled_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Scheduled item not found")
    return {"deleted": scheduled_id}
