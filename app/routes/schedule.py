from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
from datetime import datetime
from copy import deepcopy
from app.models import ScheduledItem
from app.storage import db
from app.utils.progressmanager import ProgressManager

router = APIRouter()
pm = ProgressManager()


# Create a scheduled item
@router.post("/", response_model=ScheduledItem)
def create_scheduled(item: ScheduledItem):
    item.createdAt = datetime.utcnow()
    item.updatedAt = item.createdAt
    db.schedule_db.append(item)
    pm.on_task_added(item)
    return item


@router.get("/", response_model=List[ScheduledItem])
def list_scheduled(month: Optional[str] = Query("current")):
    now = datetime.utcnow()
    def this_month():
        return now.strftime("%Y-%m")
    if month == "current":
        m = this_month()
    elif month == "next":
        next_month = (now.month % 12) + 1
        year = now.year + (1 if next_month == 1 else 0)
        m = f"{year}-{next_month:02d}"
    elif month == "future":
        return [s for s in db.schedule_db if not s.month]
    else:
        m = month
    return [s for s in db.schedule_db if s.month == m]

@router.get("/{sched_id}", response_model=ScheduledItem)
def get_scheduled(sched_id: str):
    s = next((x for x in db.schedule_db if x.id == sched_id), None)
    if not s:
        raise HTTPException(status_code=404, detail="Scheduled item not found")
    return s

@router.patch("/{sched_id}/complete", response_model=ScheduledItem)
def complete_scheduled(sched_id: str):
    sched = next((x for x in db.schedule_db if x.id == sched_id), None)
    if not sched:
        raise HTTPException(status_code=404, detail="Scheduled item not found")
    pm.on_task_completed(sched)
    return sched

@router.patch("/{sched_id}", response_model=ScheduledItem)
def update_scheduled(sched_id: str, patch: ScheduledItem):
    sched = next((x for x in db.schedule_db if x.id == sched_id), None)
    if not sched:
        raise HTTPException(status_code=404, detail="Scheduled item not found")
    for k, v in patch.dict(exclude_unset=True).items():
        setattr(sched, k, v)
    sched.updatedAt = datetime.utcnow()
    # Recalc progress if set association changed or completion changed
    pm.on_task_added(sched)
    return sched

@router.delete("/{sched_id}")
def delete_scheduled(sched_id: str):
    sched = next((x for x in db.schedule_db if x.id == sched_id), None)
    if not sched:
        raise HTTPException(status_code=404, detail="Scheduled item not found")
    db.schedule_db.remove(sched)
    pm.on_task_removed(sched)
    return {"message": "Scheduled item deleted"}