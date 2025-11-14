from fastapi import APIRouter, HTTPException
from typing import List
from app.models import Achievement
from datetime import datetime
from app.storage import db

router = APIRouter()

# Get all achievements


@router.get("/", response_model=List[Achievement])
def get_achievements():
    return db.achievements_db


# Add a new achievement (usually called internally)
def add_achievement(name: str, categoryId: str, month: str, itemId: str = None, setId: str = None):
    ach = Achievement(
        id=f"ach{len(db.achievements_db)+1:03d}",
        itemId=itemId,
        setId=setId,
        name=name,
        categoryId=categoryId,
        month=month,
        completedAt=datetime.utcnow()
    )
    db.achievements_db.append(ach)
    return ach

@router.delete("/{ach_id}")
def delete_achievement(ach_id: str):
    for ach in db.achievements_db:
        if ach.id == ach_id:
            db.achievements_db.remove(ach)
            return {"message": f"Achievement {ach_id} deleted"}
    raise HTTPException(status_code=404, detail="Achievement not found")