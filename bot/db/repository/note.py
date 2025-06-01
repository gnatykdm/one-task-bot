from sqlalchemy.orm import Session
from typing import Optional, List
from models.models import Note
import datetime

class NoteRepository:
    @staticmethod
    def create(session: Session, u_id: int, n_context: str,
               created_at: datetime.datetime = None) -> Note:
        if created_at is None:
            created_at = datetime.datetime.utcnow()
        note = Note(
            u_id=u_id,
            n_context=n_context,
            created_at=created_at
        )
        session.add(note)
        session.commit()
        session.refresh(note)
        return note

    @staticmethod
    def get(session: Session, n_id: int) -> Optional[Note]:
        return session.query(Note).filter(Note.n_id == n_id).first()

    @staticmethod
    def update(session: Session, n_id: int, **kwargs) -> Optional[Note]:
        note = session.query(Note).filter(Note.n_id == n_id).first()
        if not note:
            return None
        for key, value in kwargs.items():
            setattr(note, key, value)
        session.commit()
        return note

    @staticmethod
    def delete(session: Session, n_id: int) -> bool:
        note = session.query(Note).filter(Note.n_id == n_id).first()
        if not note:
            return False
        session.delete(note)
        session.commit()
        return True

    @staticmethod
    def list_by_user(session: Session, u_id: int) -> List[Note]:
        return session.query(Note).filter(Note.u_id == u_id).all()