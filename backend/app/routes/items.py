# backend/app/routes/items.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session


from app import crud, schemas

from app.models import Item
from app.db import get_db

router = APIRouter()

@router.get("/", response_model=list[schemas.ItemRead])
def read_items(db: Session = Depends(get_db)):
    return crud.get_items(db)

@router.get("/{item_id}", response_model=schemas.ItemRead)
def read_item(item_id: str, db: Session = Depends(get_db)):
    obj = crud.get_item(db, item_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Item not found")
    return obj

@router.post("/", response_model=schemas.ItemRead)
def create_item(payload : schemas.ItemCreate, db: Session = Depends(get_db)):

    obj = Item(**payload.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

@router.delete("/{item_id}")
def delete_item(item_id: str, db: Session = Depends(get_db)):
    deleted = crud.delete_item(db, item_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"deleted": item_id}
