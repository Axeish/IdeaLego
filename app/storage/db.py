# app/storage/db.py

from typing import List, Optional
from sqlalchemy.orm import Session

from app.connection import SessionLocal
from app.models import Item, ScheduledItem, Set, Achievement, Category


# ---------------------------
# DB Session Dependency
# ---------------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# =====================================================
# CATEGORY CRUD
# =====================================================
def get_categories(db: Session) -> List[Category]:
    return db.query(Category).all()


def get_category(db: Session, category_id: str) -> Optional[Category]:
    return db.query(Category).filter(Category.id == category_id).first()


def create_category(db: Session, category: Category) -> Category:
    db.add(category)
    db.commit()
    db.refresh(category)
    return category


def delete_category(db: Session, category_id: str) -> Optional[Category]:
    obj = get_category(db, category_id)
    if not obj:
        return None
    db.delete(obj)
    db.commit()
    return obj


# =====================================================
# ITEM CRUD
# =====================================================
def get_items(db: Session) -> List[Item]:
    return db.query(Item).all()


def get_item(db: Session, item_id: str) -> Optional[Item]:
    return db.query(Item).filter(Item.id == item_id).first()


def create_item(db: Session, item: Item) -> Item:
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def delete_item(db: Session, item_id: str) -> Optional[Item]:
    obj = get_item(db, item_id)
    if not obj:
        return None
    db.delete(obj)
    db.commit()
    return obj


# =====================================================
# SET CRUD
# =====================================================
def get_sets(db: Session) -> List[Set]:
    return db.query(Set).all()


def get_set(db: Session, set_id: str) -> Optional[Set]:
    return db.query(Set).filter(Set.id == set_id).first()


def create_set(db: Session, set_obj: Set) -> Set:
    db.add(set_obj)
    db.commit()
    db.refresh(set_obj)
    return set_obj


def delete_set(db: Session, set_id: str) -> Optional[Set]:
    obj = get_set(db, set_id)
    if not obj:
        return None
    db.delete(obj)
    db.commit()
    return obj


# =====================================================
# SCHEDULED ITEMS CRUD
# =====================================================
def get_scheduled_items(db: Session) -> List[ScheduledItem]:
    return db.query(ScheduledItem).all()


def get_scheduled_item(db: Session, scheduled_id: str) -> Optional[ScheduledItem]:
    return db.query(ScheduledItem).filter(ScheduledItem.id == scheduled_id).first()


def create_scheduled_item(db: Session, scheduled_item: ScheduledItem) -> ScheduledItem:
    db.add(scheduled_item)
    db.commit()
    db.refresh(scheduled_item)
    return scheduled_item


def delete_scheduled_item(db: Session, scheduled_id: str) -> Optional[ScheduledItem]:
    obj = get_scheduled_item(db, scheduled_id)
    if not obj:
        return None
    db.delete(obj)
    db.commit()
    return obj


# =====================================================
# ACHIEVEMENTS CRUD
# =====================================================
def get_achievements(db: Session) -> List[Achievement]:
    return db.query(Achievement).all()


def get_achievement(db: Session, achievement_id: str) -> Optional[Achievement]:
    return db.query(Achievement).filter(Achievement.id == achievement_id).first()


def create_achievement(db: Session, achievement: Achievement) -> Achievement:
    db.add(achievement)
    db.commit()
    db.refresh(achievement)
    return achievement


def delete_achievement(db: Session, achievement_id: str) -> Optional[Achievement]:
    obj = get_achievement(db, achievement_id)
    if not obj:
        return None
    db.delete(obj)
    db.commit()
    return obj
