from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from database.config import get_db_url
from typing import Generator

DATABASE_URL = get_db_url()
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_session() -> Generator[Session, None, None]:
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
