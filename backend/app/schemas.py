# backend/app/schemas.py
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

# -------------------------
# Category
# -------------------------
class CategoryBase(BaseModel):
    id: str
    name: str
    color: Optional[str] = None
    description: Optional[str] = None

class CategoryCreate(CategoryBase):
    pass

class CategoryRead(CategoryBase):
    createdAt: Optional[datetime]
    updatedAt: Optional[datetime]

    class Config:
        orm_mode = True

# -------------------------
# Item
# -------------------------
class ItemBase(BaseModel):
    id: str
    name: str
    description: Optional[str] = None
    categoryId: Optional[str] = None
    status: Optional[str] = "idea"
    priority: Optional[int] = None
    tags: Optional[str] = ""
    deadline: Optional[datetime] = None

class ItemCreate(ItemBase):
    pass

class ItemRead(ItemBase):
    createdAt: Optional[datetime]
    updatedAt: Optional[datetime]

    class Config:
        orm_mode = True

# -------------------------
# Set
# -------------------------
class SetBase(BaseModel):
    id: str
    name: str
    categoryId: Optional[str] = None
    month: Optional[str] = None
    progress: Optional[int] = 0

class SetCreate(SetBase):
    pass

class SetRead(SetBase):
    createdAt: Optional[datetime]
    updatedAt: Optional[datetime]

    class Config:
        orm_mode = True

# -------------------------
# ScheduledItem
# -------------------------
class ScheduledItemBase(BaseModel):
    id: str
    itemId: str
    setId: Optional[str] = None
    month: str
    startDate: Optional[datetime] = None
    endDate: Optional[datetime] = None
    repeat: Optional[bool] = False
    completed: Optional[bool] = False

class ScheduledItemCreate(ScheduledItemBase):
    pass

class ScheduledItemRead(ScheduledItemBase):
    createdAt: Optional[datetime]
    updatedAt: Optional[datetime]

    class Config:
        orm_mode = True

# -------------------------
# Achievement
# -------------------------
class AchievementBase(BaseModel):
    id: str
    itemId: Optional[str] = None
    setId: Optional[str] = None
    categoryId: Optional[str] = None
    month: str
    completedAt: Optional[datetime] = None

class AchievementCreate(AchievementBase):
    pass

class AchievementRead(AchievementBase):
    class Config:
        orm_mode = True
