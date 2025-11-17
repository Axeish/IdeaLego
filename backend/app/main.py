# backend/app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.connection import engine, Base

# import routers
from app.routes import items, sets, schedule, categories, achievements

app = FastAPI(
    title="IdeaLego API",
    version="1.0.0",
    description="Build ideas block by block: from concept ➡ schedule ➡ set ➡ done."
)

origins = [
    "http://localhost:5173",
    # you can add more origins if needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # or ["*"] to allow all (not recommended for production)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# create all tables
Base.metadata.create_all(bind=engine)

# Register routers
app.include_router(items.router, prefix="/items", tags=["Items"])
app.include_router(sets.router, prefix="/sets", tags=["Sets"])
app.include_router(schedule.router, prefix="/schedule", tags=["Schedule"])
app.include_router(achievements.router, prefix="/achievements", tags=["Achievements"])
app.include_router(categories.router, prefix="/categories", tags=["Categories"])

@app.get("/")
def root():
    return {"message": "Welcome to IdeaLego 🚀"}
