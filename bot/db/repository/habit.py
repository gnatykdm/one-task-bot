from models.models import Habit, TaskStatus
from sqlalchemy.orm import Session
from typing import Optional, List
import datetime

class HabitRepository:
    @staticmethod
    def create(session: Session, u_id: int, h_name: str, h_status: TaskStatus,
               start_h_time: datetime.datetime, finish_h_time: datetime.datetime,
               h_created_at: Optional[datetime.datetime] = None) -> Habit:
        if h_created_at is None:
            h_created_at = datetime.datetime.utcnow()
        habit = Habit(
            u_id=u_id,
            h_name=h_name,
            h_status=h_status,
            start_h_time=start_h_time,
            finish_h_time=finish_h_time,
            h_created_at=h_created_at
        )
        session.add(habit)
        session.commit()
        session.refresh(habit)
        return habit

    @staticmethod
    def get(session: Session, h_id: int) -> Optional[Habit]:
        return session.query(Habit).filter(Habit.h_id == h_id).first()

    @staticmethod
    def update(session: Session, h_id: int, **kwargs) -> Optional[Habit]:
        habit = session.query(Habit).filter(Habit.h_id == h_id).first()
        if not habit:
            return None
        for key, value in kwargs.items():
            setattr(habit, key, value)
        session.commit()
        return habit

    @staticmethod
    def delete(session: Session, h_id: int) -> bool:
        habit = session.query(Habit).filter(Habit.h_id == h_id).first()
        if not habit:
            return False
        session.delete(habit)
        session.commit()
        return True

    @staticmethod
    def list_by_user(session: Session, u_id: int) -> List[Habit]:
        return session.query(Habit).filter(Habit.u_id == u_id).all()