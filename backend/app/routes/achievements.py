# backend/app/routes/achievements.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app import crud, schemas
from app.db import get_db

router = APIRouter()

@router.get("/", response_model=List[schemas.AchievementRead])
def read_achievements(db: Session = Depends(get_db)):
    return crud.get_achievements(db)

@router.get("/{achievement_id}", response_model=schemas.AchievementRead)
def read_achievement(achievement_id: str, db: Session = Depends(get_db)):
    obj = crud.get_achievement(db, achievement_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Achievement not found")
    return obj

@router.post("/", response_model=schemas.AchievementRead)
def create_achievement(achievement: schemas.AchievementCreate, db: Session = Depends(get_db)):
    return crud.create_achievement(db, achievement)

@router.delete("/{achievement_id}")
def delete_achievement(achievement_id: str, db: Session = Depends(get_db)):
    deleted = crud.delete_achievement(db, achievement_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Achievement not found")
    return {"deleted": achievement_id}
