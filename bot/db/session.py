from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine, Engine
from config.dbconfig import get_db_url
from contextlib import contextmanager
from typing import Generator

DATABASE_URL: str = get_db_url()
engine: Engine = create_engine(DATABASE_URL)
SessionLocal: Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_session() -> Generator[Session, None, None]:
    session: Session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

@contextmanager
def get_db_session():
    session = next(get_session())
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
