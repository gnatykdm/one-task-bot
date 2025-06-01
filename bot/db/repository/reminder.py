from models.models import Reminder
from sqlalchemy.orm import Session
from typing import Optional, List
import datetime

class ReminderRepository:
    @staticmethod
    def create(session: Session, u_id: int, r_name: str,
               r_time: datetime.datetime, r_created_at: Optional[datetime.datetime] = None) -> Reminder:
        if r_created_at is None:
            r_created_at = datetime.datetime.utcnow()
        reminder = Reminder(
            u_id=u_id,
            r_name=r_name,
            r_time=r_time,
            r_created_at=r_created_at
        )
        session.add(reminder)
        session.commit()
        session.refresh(reminder)
        return reminder

    @staticmethod
    def get(session: Session, r_id: int) -> Optional[Reminder]:
        return session.query(Reminder).filter(Reminder.r_id == r_id).first()

    @staticmethod
    def update(session: Session, r_id: int, **kwargs) -> Optional[Reminder]:
        reminder = session.query(Reminder).filter(Reminder.r_id == r_id).first()
        if not reminder:
            return None
        for key, value in kwargs.items():
            setattr(reminder, key, value)
        session.commit()
        return reminder

    @staticmethod
    def delete(session: Session, r_id: int) -> bool:
        reminder = session.query(Reminder).filter(Reminder.r_id == r_id).first()
        if not reminder:
            return False
        session.delete(reminder)
        session.commit()
        return True

    @staticmethod
    def list_by_user(session: Session, u_id: int) -> List[Reminder]:
        return session.query(Reminder).filter(Reminder.u_id == u_id).all()
