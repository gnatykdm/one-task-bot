from sqlalchemy.orm import Session
from typing import Optional, List
from models.models import Focus
import datetime

class FocusRepository:
    @staticmethod
    def create(session: Session, u_id: int, start_time: datetime.datetime, stop_time: datetime.datetime,
               breaks_counter: int = 0, t_id: Optional[int] = None) -> Focus:
        focus = Focus(
            u_id=u_id,
            t_id=t_id,
            start_time=start_time,
            stop_time=stop_time,
            breaks_counter=breaks_counter
        )
        session.add(focus)
        session.commit()
        session.refresh(focus)
        return focus

    @staticmethod
    def get(session: Session, f_id: int) -> Optional[Focus]:
        return session.query(Focus).filter(Focus.f_id == f_id).first()

    @staticmethod
    def update(session: Session, f_id: int, **kwargs) -> Optional[Focus]:
        focus = session.query(Focus).filter(Focus.f_id == f_id).first()
        if not focus:
            return None
        for key, value in kwargs.items():
            setattr(focus, key, value)
        session.commit()
        return focus

    @staticmethod
    def delete(session: Session, f_id: int) -> bool:
        focus = session.query(Focus).filter(Focus.f_id == f_id).first()
        if not focus:
            return False
        session.delete(focus)
        session.commit()
        return True

    @staticmethod
    def list_by_user(session: Session, u_id: int) -> List[Focus]:
        return session.query(Focus).filter(Focus.u_id == u_id).all()