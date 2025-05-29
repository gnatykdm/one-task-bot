from sqlalchemy.orm import Session
from typing import List, Optional
import datetime

from models import (
    User, Task, Note, DailyRoutine, DailyStatistic, Habit, Focus, Reminder,
    LanguageEnum, TaskStatus, RoutineType
)

# --- User CRUD ---
class UserCRUD:
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
    def list_all(session: Session) -> List[User]:
        return session.query(User).all()


# --- Task CRUD ---
class TaskCRUD:
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


# --- Note CRUD ---
class NoteCRUD:
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


# --- DailyRoutine CRUD ---
class DailyRoutineCRUD:
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


# --- DailyStatistic CRUD ---
class DailyStatisticCRUD:
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


# --- Habit CRUD ---
class HabitCRUD:
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


# --- Focus CRUD ---
class FocusCRUD:
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


# --- Reminder CRUD ---
class ReminderCRUD:
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
