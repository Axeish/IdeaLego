from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.storage import db
from app.models import Item

router = APIRouter()

@router.get("/")
def get_all_items(database: Session = Depends(db.get_db)):
    return db.get_items(database)

@router.get("/{item_id}")
def get_item(item_id: str, database: Session = Depends(db.get_db)):
    item = db.get_item(database, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.post("/")
def create_item(item: Item, database: Session = Depends(db.get_db)):
    return db.create_item(database, item)

@router.delete("/{item_id}")
def delete_item(item_id: str, database: Session = Depends(db.get_db)):
    deleted = db.delete_item(database, item_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"deleted": item_id}
