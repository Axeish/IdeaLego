from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from pathlib import Path

# Path to SQLite file
BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "db" / "sqlite" / "ideaLego.sqlite3"

DATABASE_URL = f"sqlite:///{DB_PATH}"

# SQLAlchemy engine
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}  # SQLite specific
)

# Session class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Metadata
metadata = MetaData()

