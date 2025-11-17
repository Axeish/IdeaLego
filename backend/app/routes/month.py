# app/routes/month.py
from fastapi import APIRouter
from typing import Dict
from app.storage import db

router = APIRouter()

@router.get("/month/{month}/category_progress")
def category_progress(month: str) -> Dict[str, int]:
    """
    Return average progress for each category for the given month.
    Uses set.progress (recalculated on read).
    """
    category_map = {}
    counts = {}
    for s in db.sets_db:
        if s.month != month:
            continue
        # ensure s.progress is up-to-date by recomputing quickly
        if not s.items:
            prog = 0
        else:
            done = 0
            for sched_id in s.items:
                sch = next((x for x in db.schedule_db if x.id == sched_id), None)
                if sch and sch.completed:
                    done += 1
            prog = int((done / len(s.items)) * 100)
        key = s.categoryId or "uncategorized"
        category_map[key] = category_map.get(key, 0) + prog
        counts[key] = counts.get(key, 0) + 1

    # average
    result = {k: int(category_map[k] / counts[k]) for k in category_map} if counts else {}
    return result
