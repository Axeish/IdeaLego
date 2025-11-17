# backend/app/schemas.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# -------------------------
# Category
# -------------------------

class CategoryCreate(BaseModel):
    name: str
    color: Optional[str] = None
    description: Optional[str] = None

class CategoryRead(BaseModel):
    id: str
    name: str
    color: Optional[str]
    description: Optional[str]
    createdAt: Optional[datetime]
    updatedAt: Optional[datetime]

    class Config:
        from_attributes = True


# -------------------------
# Item
# -------------------------

class ItemCreate(BaseModel):
    name: str
    description: Optional[str] = None
    categoryId: Optional[str] = None
    status: Optional[str] = "idea"
    priority: Optional[int] = None
    tags: Optional[str] = ""
    deadline: Optional[datetime] = None

class ItemRead(BaseModel):
    id: str
    name: str
    description: Optional[str]
    categoryId: Optional[str]
    status: Optional[str]
    priority: Optional[int]
    tags: Optional[str]
    deadline: Optional[datetime]
    createdAt: Optional[datetime]
    updatedAt: Optional[datetime]

    class Config:
        from_attributes = True


# -------------------------
# Set
# -------------------------

class SetCreate(BaseModel):
    name: str
    categoryId: Optional[str]
    month: Optional[str]
    progress: Optional[int] = 0

class SetRead(BaseModel):
    id: str
    name: str
    categoryId: Optional[str]
    month: Optional[str]
    progress: Optional[int]
    createdAt: Optional[datetime]
    updatedAt: Optional[datetime]

    class Config:
        from_attributes = True


# -------------------------
# Scheduled Item
# -------------------------

class ScheduledItemCreate(BaseModel):
    itemId: str
    setId: Optional[str] = None
    month: str
    startDate: Optional[datetime] = None
    endDate: Optional[datetime] = None
    repeat: Optional[bool] = False
    completed: Optional[bool] = False

class ScheduledItemRead(BaseModel):
    id: str
    itemId: str
    setId: Optional[str]
    month: str
    startDate: Optional[datetime]
    endDate: Optional[datetime]
    repeat: Optional[bool]
    completed: Optional[bool]
    createdAt: Optional[datetime]
    updatedAt: Optional[datetime]

    class Config:
        from_attributes = True


# -------------------------
# Achievement
# -------------------------

class AchievementCreate(BaseModel):
    itemId: Optional[str] = None
    setId: Optional[str] = None
    categoryId: Optional[str] = None
    month: str

class AchievementRead(BaseModel):
    id: str
    itemId: Optional[str]
    setId: Optional[str]
    categoryId: Optional[str]
    month: str
    completedAt: Optional[datetime]

    class Config:
        from_attributes = True
