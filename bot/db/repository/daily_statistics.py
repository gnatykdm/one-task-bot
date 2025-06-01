from models.models import DailyStatistic
from sqlalchemy.orm import Session
from typing import Optional, List

class DailyStatisticRepository:
    @staticmethod
    def create(session: Session, u_id: int, performed: int = 0, focus_counter: int = 0, break_counter: int = 0,
               notes_counter: int = 0, streak: int = 0, best_streak: int = 0,
               energy_level: Optional[int] = None) -> DailyStatistic:
        stat = DailyStatistic(
            u_id=u_id,
            performed=performed,
            focus_counter=focus_counter,
            break_counter=break_counter,
            notes_counter=notes_counter,
            streak=streak,
            best_streak=best_streak,
            energy_level=energy_level
        )
        session.add(stat)
        session.commit()
        session.refresh(stat)
        return stat

    @staticmethod
    def get(session: Session, d_id: int) -> Optional[DailyStatistic]:
        return session.query(DailyStatistic).filter(DailyStatistic.d_id == d_id).first()

    @staticmethod
    def update(session: Session, d_id: int, **kwargs) -> Optional[DailyStatistic]:
        stat = session.query(DailyStatistic).filter(DailyStatistic.d_id == d_id).first()
        if not stat:
            return None
        for key, value in kwargs.items():
            setattr(stat, key, value)
        session.commit()
        return stat

    @staticmethod
    def delete(session: Session, d_id: int) -> bool:
        stat = session.query(DailyStatistic).filter(DailyStatistic.d_id == d_id).first()
        if not stat:
            return False
        session.delete(stat)
        session.commit()
        return True

    @staticmethod
    def list_by_user(session: Session, u_id: int) -> List[DailyStatistic]:
        return session.query(DailyStatistic).filter(DailyStatistic.u_id == u_id).all()