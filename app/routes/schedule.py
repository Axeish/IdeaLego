from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.storage import db
from app.models import ScheduledItem

router = APIRouter()

@router.get("/")
def get_all_scheduled_items(database: Session = Depends(db.get_db)):
    return db.get_scheduled_items(database)

@router.get("/{schedule_id}")
def get_scheduled_item(schedule_id: str, database: Session = Depends(db.get_db)):
    obj = db.get_scheduled_item(database, schedule_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Scheduled item not found")
    return obj

@router.post("/")
def create_scheduled_item(scheduled_item: ScheduledItem, database: Session = Depends(db.get_db)):
    return db.create_scheduled_item(database, scheduled_item)

@router.delete("/{schedule_id}")
def delete_scheduled_item(schedule_id: str, database: Session = Depends(db.get_db)):
    deleted = db.delete_scheduled_item(database, schedule_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Scheduled item not found")
    return {"deleted": schedule_id}
