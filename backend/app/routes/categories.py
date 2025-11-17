# backend/app/routes/categories.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app import crud, schemas
from app.db import get_db

router = APIRouter()

@router.get("/", response_model=List[schemas.CategoryRead])
def read_categories(db: Session = Depends(get_db)):
    return crud.get_categories(db)

@router.get("/{category_id}", response_model=schemas.CategoryRead)
def read_category(category_id: str, db: Session = Depends(get_db)):
    obj = crud.get_category(db, category_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Category not found")
    return obj

@router.post("/", response_model=schemas.CategoryRead)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return crud.create_category(db, category)

@router.delete("/{category_id}")
def delete_category(category_id: str, db: Session = Depends(get_db)):
    deleted = crud.delete_category(db, category_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Category not found")
    return {"deleted": category_id}
