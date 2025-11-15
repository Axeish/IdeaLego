from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime

from typing import Optional, List

Base = declarative_base()

class Category(Base):
    __tablename__ = "categories"
    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    color = Column(String, nullable=True)
    description = Column(String, nullable=True)
    createdAt = Column(DateTime, default=datetime.utcnow)
    updatedAt = Column(DateTime, default=datetime.utcnow)

    items = relationship("Item", back_populates="category")
    sets = relationship("Set", back_populates="category")

class Item(Base):
    __tablename__ = "items"
    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    categoryId = Column(String, ForeignKey("categories.id"))
    status = Column(String, default="idea")  # idea → scheduled → done
    priority = Column(Integer, nullable=True)
    tags = Column(String, default="")        # Store as comma-separated string
    createdAt = Column(DateTime, default=datetime.utcnow)
    updatedAt = Column(DateTime, default=datetime.utcnow)
    deadline = Column(DateTime, nullable=True)

    category = relationship("Category", back_populates="items")

class Set(Base):
    __tablename__ = "sets"
    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    categoryId = Column(String, ForeignKey("categories.id"))
    month = Column(String, nullable=True)  # "2025-11" format
    progress = Column(Integer, default=0)
    createdAt = Column(DateTime, default=datetime.utcnow)
    updatedAt = Column(DateTime, default=datetime.utcnow)

    category = relationship("Category", back_populates="sets")

class ScheduledItem(Base):
    __tablename__ = "scheduled_items"
    id = Column(String, primary_key=True, index=True)
    itemId = Column(String, ForeignKey("items.id"))
    setId = Column(String, ForeignKey("sets.id"), nullable=True)
    month = Column(String, nullable=False)
    startDate = Column(DateTime, nullable=True)
    endDate = Column(DateTime, nullable=True)
    repeat = Column(Boolean, default=False)
    completed = Column(Boolean, default=False)
    createdAt = Column(DateTime, default=datetime.utcnow)
    updatedAt = Column(DateTime, default=datetime.utcnow)

class Achievement(Base):
    __tablename__ = "achievements"
    id = Column(String, primary_key=True, index=True)
    itemId = Column(String, ForeignKey("items.id"), nullable=True)
    setId = Column(String, ForeignKey("sets.id"), nullable=True)
    categoryId = Column(String, ForeignKey("categories.id"))
    month = Column(String, nullable=False)
    completedAt = Column(DateTime, default=datetime.utcnow)


