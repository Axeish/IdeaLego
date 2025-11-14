from fastapi import APIRouter, HTTPException
from typing import List, Optional
from datetime import datetime
from app.models import Item
from app.storage import db

router = APIRouter()

@router.post("/")
def create_item(item: Item):
    item.createdAt = datetime.utcnow()
    item.updatedAt = item.createdAt
    db.items_db.append(item)
    return item


@router.get("/", response_model=List[Item])
def list_items(category: Optional[str] = None, status: Optional[str] = None):
    result = db.items_db
    if category:
        result = [i for i in result if i.categoryId == category]
    if status:
        result = [i for i in result if i.status == status]
    return result

@router.get("/{item_id}", response_model=Item)
def get_item(item_id: str):
    item = next((i for i in db.items_db if i.id == item_id), None)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.patch("/{item_id}", response_model=Item)
def update_item(item_id: str, patch: Item):
    item = next((i for i in db.items_db if i.id == item_id), None)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    # patch fields (simple merge)
    for k, v in patch.dict(exclude_unset=True).items():
        setattr(item, k, v)
    item.updatedAt = datetime.utcnow()
    return item

@router.delete("/{item_id}")
def delete_item(item_id: str):
    item = next((i for i in db.items_db if i.id == item_id), None)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    db.items_db.remove(item)
    # Note: schedule entries referencing this item remain; you may want to cascade delete
    return {"message": f"Item {item_id} deleted"}

