# app/test_db_full.py
from app.connection import SessionLocal, Base, engine
from app.models import Category, Item, Set

# Create tables if not exist
Base.metadata.create_all(bind=engine)

db = SessionLocal()

try:
    # -----------------------------
    # Clear existing data
    # -----------------------------
    db.query(Item).delete()
    db.query(Set).delete()
    db.query(Category).delete()
    db.commit()

    # -----------------------------
    # Create categories
    # -----------------------------
    cat1 = Category(id="cat01", name="Axeishguy", color="red")
    cat2 = Category(id="cat02", name="Cornoddity", color="green")
    db.add_all([cat1, cat2])
    db.commit()

    # -----------------------------
    # Create set "Zodiac" in Axeishguy category
    # -----------------------------
    zodiac_set = Set(id="set01", name="Zodiac", categoryId=cat1.id)
    db.add(zodiac_set)
    db.commit()

    # -----------------------------
    # Add 4 Zodiac items
    # -----------------------------
    zodiac_items = [
        Item(id="item01", name="Sagittarius", categoryId=cat1.id),
        Item(id="item02", name="Capricorn", categoryId=cat1.id),
        Item(id="item03", name="Aquarius", categoryId=cat1.id),
        Item(id="item04", name="Pisces", categoryId=cat1.id),
    ]
    db.add_all(zodiac_items)
    db.commit()

    # Assign them to the Zodiac set (optional: if using ScheduledItem, can do later)
    # In this model, Set is separate; relationship in DB is via categoryId

    # -----------------------------
    # Add 3 more items to Cornoddity
    # -----------------------------
    cornoddity_items = [
        Item(id="item05", name="cub one", categoryId=cat2.id),
        Item(id="item06", name="Santa", categoryId=cat2.id),
        Item(id="item07", name="pattern", categoryId=cat2.id),
    ]
    db.add_all(cornoddity_items)
    db.commit()

    # -----------------------------
    # Print summary
    # -----------------------------
    print("Categories:")
    for c in db.query(Category).all():
        print(c.id, c.name)

    print("\nSets:")
    for s in db.query(Set).all():
        print(s.id, s.name, s.categoryId)

    print("\nItems:")
    for i in db.query(Item).all():
        print(i.id, i.name, i.categoryId)

finally:
    db.close()
