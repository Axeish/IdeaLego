from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class Category(BaseModel):
    id: str
    name: str
    color: Optional[str] = None
    description: Optional[str] = None
    createdAt: datetime = Field(default_factory=datetime.utcnow)
    updatedAt: datetime = Field(default_factory=datetime.utcnow)

class Item(BaseModel):
    id: str
    name: str
    description: Optional[str] = None
    categoryId: str
    status: str = "idea"   # idea → scheduled → done
    priority: Optional[int] = None
    tags: List[str] = []
    createdAt: datetime = datetime.utcnow()
    updatedAt: datetime = datetime.utcnow()
    deadline: Optional[datetime] = None

class Set(BaseModel):
    id: str
    name: str
    categoryId: str
    month: Optional[str] = None         # "2025-11" format
    items: List[Item] = []
    progress: int = 0
    createdAt: datetime = Field(default_factory=datetime.utcnow)
    updatedAt: datetime = Field(default_factory=datetime.utcnow)

class ScheduledItem(BaseModel):
    id: str
    itemId: str
    setId: Optional[str] = None
    month: str                          # "2025-11" or "future"
    startDate: Optional[datetime] = None
    endDate: Optional[datetime] = None
    repeat: bool = False
    completed: bool = False
    createdAt: datetime = Field(default_factory=datetime.utcnow)
    updatedAt: datetime = Field(default_factory=datetime.utcnow)


# -------------------------------
# Achievement (completed items/sets)
# -------------------------------
class Achievement(BaseModel):
    id: str
    itemId: Optional[str] = None
    setId: Optional[str] = None
    categoryId: str
    month: str
    completedAt: datetime = Field(default_factory=datetime.utcnow)

