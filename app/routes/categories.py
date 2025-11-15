from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.storage import db
from app.models import Category

router = APIRouter()

@router.get("/")
def get_all_categories(database: Session = Depends(db.get_db)):
    return db.get_categories(database)

@router.get("/{category_id}")
def get_category(category_id: str, database: Session = Depends(db.get_db)):
    category = db.get_category(database, category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

@router.post("/")
def create_category(category: Category, database: Session = Depends(db.get_db)):
    return db.create_category(database, category)

@router.delete("/{category_id}")
def delete_category(category_id: str, database: Session = Depends(db.get_db)):
    deleted = db.delete_category(database, category_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Category not found")
    return {"deleted": category_id}
