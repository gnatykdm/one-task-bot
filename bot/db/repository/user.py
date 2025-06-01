from models.models import User, LanguageEnum
from sqlalchemy.orm import Session
from typing import Optional
import datetime

class UserRepository:
    @staticmethod
    def create(session: Session, t_id: int, t_name: str, language: LanguageEnum = LanguageEnum.ENGLISH,
               created_at: datetime.datetime = None, wake_up_time: Optional[datetime.datetime] = None,
               sleep_time: Optional[datetime.datetime] = None) -> User:
        if created_at is None:
            created_at = datetime.datetime.utcnow()
        user = User(
            t_id=t_id,
            t_name=t_name,
            language=language,
            created_at=created_at,
            wake_up_time=wake_up_time,
            sleep_time=sleep_time
        )
        session.add(user)
        session.commit()
        session.refresh(user)
        return user

    @staticmethod
    def get(session: Session, t_id: int) -> Optional[User]:
        return session.query(User).filter(User.t_id == t_id).first()

    @staticmethod
    def update(session: Session, t_id: int, **kwargs) -> Optional[User]:
        user = session.query(User).filter(User.t_id == t_id).first()
        if not user:
            return None
        for key, value in kwargs.items():
            setattr(user, key, value)
        session.commit()
        return user

    @staticmethod
    def delete(session: Session, t_id: int) -> bool:
        user = session.query(User).filter(User.t_id == t_id).first()
        if not user:
            return False
        session.delete(user)
        session.commit()
        return True

    @staticmethod
    def list_all(session: Session) -> list[type[User]]:
        return session.query(User).all()