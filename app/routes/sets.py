from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.storage import db
from app.models import Set

router = APIRouter()

@router.get("/")
def get_all_sets(database: Session = Depends(db.get_db)):
    return db.get_sets(database)

@router.get("/{set_id}")
def get_set(set_id: str, database: Session = Depends(db.get_db)):
    obj = db.get_set(database, set_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Set not found")
    return obj

@router.post("/")
def create_set(set_obj: Set, database: Session = Depends(db.get_db)):
    return db.create_set(database, set_obj)

@router.delete("/{set_id}")
def delete_set(set_id: str, database: Session = Depends(db.get_db)):
    deleted = db.delete_set(database, set_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Set not found")
    return {"deleted": set_id}
