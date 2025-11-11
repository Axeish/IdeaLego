from fastapi import APIRouter
from typing import List, Optional
from datetime import datetime
from app.models import ScheduledItem

router = APIRouter()

# In-memory DB
schedule_db: List[ScheduledItem] = []


# Create a scheduled item
@router.post("/")
def schedule_item(item: ScheduledItem):
    schedule_db.append(item)
    return item


# Get scheduled items by month (current/next/future)
@router.get("/", response_model=List[ScheduledItem])
def get_scheduled_items(month: Optional[str] = "current"):
    today = datetime.utcnow()

    def get_month_string(dt):
        return dt.strftime("%Y-%m")

    if month == "current":
        month_str = get_month_string(today)
    elif month == "next":
        next_month = (today.month % 12) + 1
        year = today.year + (1 if next_month == 1 else 0)
        month_str = f"{year}-{next_month:02d}"
    elif month == "future":
        # future = not assigned yet
        return [s for s in schedule_db if s.month.lower() == "future"]
    else:
        month_str = month

    return [s for s in schedule_db if s.month == month_str]
