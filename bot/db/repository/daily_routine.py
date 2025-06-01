from models.models import DailyRoutine, RoutineType
from sqlalchemy.orm import Session
from typing import Optional, List

class DailyRoutineRepository:
    @staticmethod
    def create(session: Session, u_id: int, r_name: str, r_type: RoutineType) -> DailyRoutine:
        routine = DailyRoutine(
            u_id=u_id,
            r_name=r_name,
            r_type=r_type
        )
        session.add(routine)
        session.commit()
        session.refresh(routine)
        return routine

    @staticmethod
    def get(session: Session, r_id: int) -> Optional[DailyRoutine]:
        return session.query(DailyRoutine).filter(DailyRoutine.r_id == r_id).first()

    @staticmethod
    def update(session: Session, r_id: int, **kwargs) -> Optional[DailyRoutine]:
        routine = session.query(DailyRoutine).filter(DailyRoutine.r_id == r_id).first()
        if not routine:
            return None
        for key, value in kwargs.items():
            setattr(routine, key, value)
        session.commit()
        return routine

    @staticmethod
    def delete(session: Session, r_id: int) -> bool:
        routine = session.query(DailyRoutine).filter(DailyRoutine.r_id == r_id).first()
        if not routine:
            return False
        session.delete(routine)
        session.commit()
        return True

    @staticmethod
    def list_by_user(session: Session, u_id: int) -> List[DailyRoutine]:
        return session.query(DailyRoutine).filter(DailyRoutine.u_id == u_id).all()