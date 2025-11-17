# test_db.py
from app.connection import SessionLocal, Base, engine
from app.models import Category, Item

# Create tables if not already created
Base.metadata.create_all(bind=engine)

# Get a database session
db = SessionLocal()

try:
    # --- Test Category ---
    category = Category(id="cat1", name="Test Category", color="blue")
    db.add(category)
    db.commit()
    db.refresh(category)
    print("Category added:", category.id, category.name)

    # --- Test Item ---
    item = Item(id="item1", name="Test Item", categoryId=category.id)
    db.add(item)
    db.commit()
    db.refresh(item)
    print("Item added:", item.id, item.name, "Category:", item.categoryId)

    # --- Query back ---
    items = db.query(Item).all()
    for i in items:
        print("Item in DB:", i.id, i.name, i.categoryId)

finally:
    db.close()
