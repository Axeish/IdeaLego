# app/storage/db.py
"""
Central in-memory storage to avoid circular imports between routers.
When you migrate to a real DB, replace this module's contents with DB session helpers.
"""

from typing import List
from app.models import Item, ScheduledItem, Set, Achievement, Category

items_db: List[Item] = []
schedule_db: List[ScheduledItem] = []
sets_db: List[Set] = []
achievements_db: List[Achievement] = []
categories_db: List[Category] = []