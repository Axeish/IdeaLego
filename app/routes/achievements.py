from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.storage import db
from app.models import Achievement

router = APIRouter()

@router.get("/")
def get_all_achievements(database: Session = Depends(db.get_db)):
    return db.get_achievements(database)

@router.get("/{achievement_id}")
def get_achievement(achievement_id: str, database: Session = Depends(db.get_db)):
    obj = db.get_achievement(database, achievement_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Achievement not found")
    return obj

@router.post("/")
def create_achievement(achievement: Achievement, database: Session = Depends(db.get_db)):
    return db.create_achievement(database, achievement)

@router.delete("/{achievement_id}")
def delete_achievement(achievement_id: str, database: Session = Depends(db.get_db)):
    deleted = db.delete_achievement(database, achievement_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Achievement not found")
    return {"deleted": achievement_id}
