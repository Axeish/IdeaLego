# app/routes/sets.py
from fastapi import APIRouter, HTTPException
from typing import List
from datetime import datetime
from app.models import Set
from app.storage import db
from app.routes.achievements import add_achievement

router = APIRouter()

@router.post("/", response_model=Set)
def create_set(new_set: Set):
    new_set.createdAt = datetime.utcnow()
    new_set.updatedAt = new_set.createdAt
    db.sets_db.append(new_set)
    return new_set

@router.get("/", response_model=List[Set])
def list_sets(month: str = None):
    if month:
        return [s for s in db.sets_db if s.month == month]
    return db.sets_db

@router.get("/{set_id}", response_model=Set)
def get_set(set_id: str):
    s = next((x for x in db.sets_db if x.id == set_id), None)
    if not s:
        raise HTTPException(status_code=404, detail="Set not found")
    # Recalculate progress (live)
    if not s.items:
        s.progress = 0
    else:
        completed = 0
        for sched_id in s.items:
            sch = next((x for x in db.schedule_db if x.id == sched_id), None)
            if sch and sch.completed:
                completed += 1
        s.progress = int((completed / len(s.items)) * 100)
    # If finished, add to achievements
    if s.progress == 100 and not any(a.setId == s.id for a in db.achievements_db):
        add_achievement(name=s.name, type="set", categoryId=s.categoryId, month=s.month, setId=s.id)
    return s

@router.post("/{set_id}/add_item/{sched_id}", response_model=Set)
def add_item_to_set(set_id: str, sched_id: str):
    s = next((x for x in db.sets_db if x.id == set_id), None)
    if not s:
        raise HTTPException(status_code=404, detail="Set not found")
    sch = next((x for x in db.schedule_db if x.id == sched_id), None)
    if not sch:
        raise HTTPException(status_code=404, detail="Scheduled item not found")
    if sched_id not in s.items:
        s.items.append(sched_id)
        s.updatedAt = datetime.utcnow()
    return s

@router.patch("/{set_id}", response_model=Set)
def update_set(set_id: str, patch: Set):
    s = next((x for x in db.sets_db if x.id == set_id), None)
    if not s:
        raise HTTPException(status_code=404, detail="Set not found")
    for k, v in patch.dict(exclude_unset=True).items():
        setattr(s, k, v)
    s.updatedAt = datetime.utcnow()
    return s

@router.delete("/{set_id}")
def delete_set(set_id: str):
    s = next((x for x in db.sets_db if x.id == set_id), None)
    if not s:
        raise HTTPException(status_code=404, detail="Set not found")
    db.sets_db.remove(s)
    return {"message": "Set deleted"}
