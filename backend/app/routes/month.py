from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, schemas
from app.models import Item, Set, Achievement
from app.db import get_db

router = APIRouter()

@router.get("/", response_model=list[schemas.MonthlySummary])
def get_monthly_summary(db: Session = Depends(get_db)):
    # For simplicity, assume 'month' column is "YYYY-MM"
    results = []

    months = db.query(Item.month).distinct().all()  # or generate last 12 months

    for (month,) in months:
        total_items = db.query(Item).filter(Item.deadline.startswith(month)).count()
        completed_items = db.query(Item).filter(Item.deadline.startswith(month), Item.status=="done").count()
        total_sets = db.query(Set).filter(Set.month==month).count()
        completed_sets = db.query(Set).filter(Set.month==month, Set.progress==100).count()
        achievements = db.query(Achievement).filter(Achievement.month==month).count()

        results.append(schemas.MonthlySummary(
            month=month,
            total_items=total_items,
            completed_items=completed_items,
            total_sets=total_sets,
            completed_sets=completed_sets,
            achievements=achievements
        ))
    return results
