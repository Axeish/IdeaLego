from fastapi import APIRouter
from typing import List
from app.models import Item

router = APIRouter()

# In-memory database
items_db: List[Item] = []

@router.post("/")
def create_item(item: Item):
    items_db.append(item)
    return item

@router.get("/", response_model=List[Item])
def get_items():
    return items_db
