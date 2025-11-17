# backend/app/crud.py
from sqlalchemy.orm import Session
from typing import List, Optional

from app import models, schemas

# -------------------------
# Category
# -------------------------
def get_categories(db: Session) -> List[models.Category]:
    return db.query(models.Category).all()

def get_category(db: Session, category_id: str) -> Optional[models.Category]:
    return db.query(models.Category).filter(models.Category.id == category_id).first()

def create_category(db: Session, category_in: schemas.CategoryCreate) -> models.Category:
    obj = models.Category(**category_in.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def delete_category(db: Session, category_id: str) -> Optional[models.Category]:
    obj = get_category(db, category_id)
    if not obj:
        return None
    db.delete(obj)
    db.commit()
    return obj

# -------------------------
# Item
# -------------------------
def get_items(db: Session) -> List[models.Item]:
    return db.query(models.Item).all()

def get_item(db: Session, item_id: str) -> Optional[models.Item]:
    return db.query(models.Item).filter(models.Item.id == item_id).first()

def create_item(db: Session, item_in: schemas.ItemCreate) -> models.Item:
    obj = models.Item(**item_in.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def delete_item(db: Session, item_id: str) -> Optional[models.Item]:
    obj = get_item(db, item_id)
    if not obj:
        return None
    db.delete(obj)
    db.commit()
    return obj

# -------------------------
# Set
# -------------------------
def get_sets(db: Session) -> List[models.Set]:
    return db.query(models.Set).all()

def get_set(db: Session, set_id: str) -> Optional[models.Set]:
    return db.query(models.Set).filter(models.Set.id == set_id).first()

def create_set(db: Session, set_in: schemas.SetCreate) -> models.Set:
    obj = models.Set(**set_in.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def delete_set(db: Session, set_id: str) -> Optional[models.Set]:
    obj = get_set(db, set_id)
    if not obj:
        return None
    db.delete(obj)
    db.commit()
    return obj

# -------------------------
# ScheduledItem
# -------------------------
def get_scheduled_items(db: Session) -> List[models.ScheduledItem]:
    return db.query(models.ScheduledItem).all()

def get_scheduled_item(db: Session, scheduled_id: str) -> Optional[models.ScheduledItem]:
    return db.query(models.ScheduledItem).filter(models.ScheduledItem.id == scheduled_id).first()

def create_scheduled_item(db: Session, scheduled_in: schemas.ScheduledItemCreate) -> models.ScheduledItem:
    obj = models.ScheduledItem(**scheduled_in.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def delete_scheduled_item(db: Session, scheduled_id: str) -> Optional[models.ScheduledItem]:
    obj = get_scheduled_item(db, scheduled_id)
    if not obj:
        return None
    db.delete(obj)
    db.commit()
    return obj

# -------------------------
# Achievement
# -------------------------
def get_achievements(db: Session) -> List[models.Achievement]:
    return db.query(models.Achievement).all()

def get_achievement(db: Session, achievement_id: str) -> Optional[models.Achievement]:
    return db.query(models.Achievement).filter(models.Achievement.id == achievement_id).first()

def create_achievement(db: Session, achievement_in: schemas.AchievementCreate) -> models.Achievement:
    obj = models.Achievement(**achievement_in.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def delete_achievement(db: Session, achievement_id: str) -> Optional[models.Achievement]:
    obj = get_achievement(db, achievement_id)
    if not obj:
        return None
    db.delete(obj)
    db.commit()
    return obj
