from fastapi import APIRouter, HTTPException
from typing import List
from app.models import Set, ScheduledItem
from app.routes.schedule import schedule_db  # reference in-memory schedule
from datetime import datetime

router = APIRouter()

# In-memory DB
sets_db: List[Set] = []

# Helper function to calculate set progress
def calculate_set_progress(s: Set):
    if not s.items:
        return 0
    completed_count = sum(
        1 for sched_id in s.items
        if next((sch for sch in schedule_db if sch.id == sched_id and sch.completed), None)
    )
    return int((completed_count / len(s.items)) * 100)

# Get set with auto progress
@router.get("/{set_id}")
def get_set(set_id: str):
    s = next((s for s in sets_db if s.id == set_id), None)
    if not s:
        raise HTTPException(status_code=404, detail="Set not found")
    s.progress = calculate_set_progress(s)
    return s

# Create a set
@router.post("/")
def create_set(new_set: Set):
    sets_db.append(new_set)
    return new_set

# Add ScheduledItem to a set
@router.post("/{set_id}/add_item/{sched_id}")
def add_item_to_set(set_id: str, sched_id: str):
    s = next((s for s in sets_db if s.id == set_id), None)
    if not s:
        raise HTTPException(status_code=404, detail="Set not found")

    sched = next((sch for sch in schedule_db if sch.id == sched_id), None)
    if not sched:
        raise HTTPException(status_code=404, detail="Scheduled item not found")

    if sched.id not in s.items:
        s.items.append(sched.id)
        s.updatedAt = datetime.utcnow()
    return s

# Update set progress manually
@router.patch("/{set_id}/progress")
def update_set_progress(set_id: str, progress: int):
    s = next((s for s in sets_db if s.id == set_id), None)
    if not s:
        raise HTTPException(status_code=404, detail="Set not found")
    s.progress = progress
    s.updatedAt = datetime.utcnow()
    return s
