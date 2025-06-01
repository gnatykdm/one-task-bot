from models.models import Task, TaskStatus
from sqlalchemy.orm import Session
from typing import Optional, List
import datetime

class TaskRepository:
    @staticmethod
    def create(session: Session, u_id: int, t_name: str, t_deadline: Optional[datetime.datetime] = None,
               t_status: TaskStatus = TaskStatus.PROCESSING,
               t_created_at: datetime.datetime = None) -> Task:
        if t_created_at is None:
            t_created_at = datetime.datetime.utcnow()
        task = Task(
            u_id=u_id,
            t_name=t_name,
            t_deadline=t_deadline,
            t_status=t_status,
            t_created_at=t_created_at
        )
        session.add(task)
        session.commit()
        session.refresh(task)
        return task

    @staticmethod
    def get(session: Session, t_id: int) -> Optional[Task]:
        return session.query(Task).filter(Task.t_id == t_id).first()

    @staticmethod
    def update(session: Session, t_id: int, **kwargs) -> Optional[Task]:
        task = session.query(Task).filter(Task.t_id == t_id).first()
        if not task:
            return None
        for key, value in kwargs.items():
            setattr(task, key, value)
        session.commit()
        return task

    @staticmethod
    def delete(session: Session, t_id: int) -> bool:
        task = session.query(Task).filter(Task.t_id == t_id).first()
        if not task:
            return False
        session.delete(task)
        session.commit()
        return True

    @staticmethod
    def list_by_user(session: Session, u_id: int) -> List[Task]:
        return session.query(Task).filter(Task.u_id == u_id).all()
