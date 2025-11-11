from fastapi import APIRouter
from app.routes.sets import sets_db
from typing import Dict

router = APIRouter()

@router.get("/month/{month}/category_progress")
def category_progress(month: str):
    # Group sets by category
    category_totals: Dict[str, list] = {}
    for s in sets_db:
        if s.month != month:
            continue
        category_totals.setdefault(s.categoryId, []).append(s.progress)

    # Calculate average progress per category
    category_progress = {
        cat_id: int(sum(progress_list)/len(progress_list)) if progress_list else 0
        for cat_id, progress_list in category_totals.items()
    }
    return category_progress
