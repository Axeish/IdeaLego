# backend/app/routes/sets.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app import crud, schemas
from app.db import get_db

router = APIRouter()

@router.get("/", response_model=List[schemas.SetRead])
def read_sets(db: Session = Depends(get_db)):
    return crud.get_sets(db)

@router.get("/{set_id}", response_model=schemas.SetRead)
def read_set(set_id: str, db: Session = Depends(get_db)):
    obj = crud.get_set(db, set_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Set not found")
    return obj

@router.post("/", response_model=schemas.SetRead)
def create_set(set_in: schemas.SetCreate, db: Session = Depends(get_db)):
    return crud.create_set(db, set_in)

@router.delete("/{set_id}")
def delete_set(set_id: str, db: Session = Depends(get_db)):
    deleted = crud.delete_set(db, set_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Set not found")
    return {"deleted": set_id}
