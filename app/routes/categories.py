# app/routes/categories.py
from fastapi import APIRouter, HTTPException
from typing import List
from datetime import datetime
from app.models import Category
from app.storage import db

router = APIRouter()

# ---------- CREATE ----------
@router.post("/", response_model=Category)
def create_category(category: Category):
    # Prevent duplicate ID
    if any(c.id == category.id for c in db.categories_db):
        raise HTTPException(status_code=400, detail="Category ID already exists")
    category.createdAt = datetime.utcnow()
    category.updatedAt = category.createdAt
    db.categories_db.append(category)
    return category

# ---------- LIST ----------
@router.get("/", response_model=List[Category])
def list_categories():
    return db.categories_db

# ---------- GET SINGLE ----------
@router.get("/{cat_id}", response_model=Category)
def get_category(cat_id: str):
    c = next((x for x in db.categories_db if x.id == cat_id), None)
    if not c:
        raise HTTPException(status_code=404, detail="Category not found")
    return c

# ---------- UPDATE ----------
@router.patch("/{cat_id}", response_model=Category)
def update_category(cat_id: str, patch: Category):
    c = next((x for x in db.categories_db if x.id == cat_id), None)
    if not c:
        raise HTTPException(status_code=404, detail="Category not found")
    for k, v in patch.dict(exclude_unset=True).items():
        setattr(c, k, v)
    c.updatedAt = datetime.utcnow()
    return c

# ---------- DELETE ----------
@router.delete("/{cat_id}")
def delete_category(cat_id: str):
    cat = next((c for c in db.categories_db if c.id == cat_id), None)
    if not cat:
        raise HTTPException(status_code=404, detail="Category not found")

    # OPTIONAL: Refuse if category is in use
    used_in_items = any(i.categoryId == cat_id for i in db.items_db)
    used_in_sets = any(s.categoryId == cat_id for s in db.sets_db)
    used_in_ach = any(a.categoryId == cat_id for a in db.achievements_db)

    if used_in_items or used_in_sets or used_in_ach:
        raise HTTPException(
            status_code=400,
            detail="Category is used in items/sets/achievements — remove links first."
        )

    db.categories_db.remove(cat)
    return {"message": "Category deleted"}
