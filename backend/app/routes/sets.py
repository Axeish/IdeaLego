# backend/app/routes/sets.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import Set

from app import crud, schemas
from app.db import get_db

router = APIRouter()

@router.get("/", response_model=list[schemas.SetRead])
def read_sets(db: Session = Depends(get_db)):
    return crud.get_sets(db)

@router.get("/{set_id}", response_model=schemas.SetRead)
def read_set(set_id: str, db: Session = Depends(get_db)):
    obj = crud.get_set(db, set_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Set not found")
    return obj

@router.post("/", response_model=schemas.SetRead)
def create_set(payload: schemas.SetCreate, db: Session = Depends(get_db)):
    obj = Set(**payload.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

@router.delete("/{set_id}")
def delete_set(set_id: str, db: Session = Depends(get_db)):
    deleted = crud.delete_set(db, set_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Set not found")
    return {"deleted": set_id}
