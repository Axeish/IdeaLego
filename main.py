from fastapi import FastAPI
from app.routes import items, sets, schedule, month

app = FastAPI(
    title="IdeaLego API",
    version="1.0.0",
    description="Build ideas block by block: from concept ➡ schedule ➡ set ➡ done."
)

# Register routers
app.include_router(items.router, prefix="/items", tags=["Items"])
app.include_router(sets.router, prefix="/sets", tags=["Sets"])
app.include_router(schedule.router, prefix="/schedule", tags=["Schedule"])
app.include_router(month.router, prefix="/analytics", tags=["Analytics"])


@app.get("/")
def root():
    return {"message": "Welcome to IdeaLego 🚀"}
