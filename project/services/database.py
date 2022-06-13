"""SQLAlchemy Database."""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from project import config

# Declarative base.
Base = declarative_base()

# Retrieve database uri
settings = config.get_settings()
database_uri = f"{settings.DATABASE_DIALECT}://{settings.DATABASE_USER}:{settings.DATABASE_PASSWORD}" \
               f"@{settings.DATABASE_HOST}:{settings.DATABASE_PORT}/{settings.DATABASE_NAME}"

# Session local
engine = create_engine(database_uri)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


def get_db():
    """Get database local session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_db() -> None:
    Base.metadata.create_all(engine)