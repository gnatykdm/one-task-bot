from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from typing import Dict

import enum

from sqlalchemy import (
    Column, BigInteger, String, Text, TIME,
    TIMESTAMP, Integer, Boolean, Interval, Enum, ForeignKey, CheckConstraint, func
)

Base = declarative_base()

# --- Enum definitions in Python ---
class LanguageEnum(enum.Enum):
    ENGLISH = "ENGLISH"
    RUSSIAN = "RUSSIAN"

class TaskStatus(enum.Enum):
    DONE = "DONE"
    PROCESSING = "PROCESSING"

class RoutineType(enum.Enum):
    MORNING = "MORNING"
    EVENING = "EVENING"

# --- Models ---
class User(Base):
    __tablename__ = "users"

    t_id = Column(BigInteger, primary_key=True)
    t_name = Column(String(255), unique=True, nullable=False)
    language = Column(Enum(LanguageEnum), nullable=False, default=LanguageEnum.ENGLISH)
    created_at = Column(TIMESTAMP, nullable=False)
    wake_up_time = Column(TIME, nullable=True)
    sleep_time = Column(TIME, nullable=True)

    tasks = relationship("Task", back_populates="user", cascade="all, delete")
    notes = relationship("Note", back_populates="user", cascade="all, delete")
    daily_routines = relationship("DailyRoutine", back_populates="user", cascade="all, delete")
    daily_statistics = relationship("DailyStatistic", back_populates="user", cascade="all, delete")
    habits = relationship("Habit", back_populates="user", cascade="all, delete")
    focuses = relationship("Focus", back_populates="user", cascade="all, delete")
    reminders = relationship("Reminder", back_populates="user", cascade="all, delete")


class Task(Base):
    __tablename__ = "tasks"

    t_id = Column(BigInteger, primary_key=True, autoincrement=True)
    u_id = Column(BigInteger, ForeignKey("users.t_id", ondelete="CASCADE"), nullable=False)
    t_name = Column(String(255), nullable=False)
    t_deadline = Column(TIMESTAMP, nullable=True)
    t_status = Column(Enum(TaskStatus), nullable=False, default=TaskStatus.PROCESSING)
    t_created_at = Column(TIMESTAMP, nullable=False, server_default=func.now())

    user = relationship("User", back_populates="tasks")
    focuses = relationship("Focus", back_populates="task", cascade="all, delete")
    reminders = relationship("Reminder", back_populates="task", cascade="all, delete")


class Note(Base):
    __tablename__ = "notes"

    n_id = Column(BigInteger, primary_key=True, autoincrement=True)
    u_id = Column(BigInteger, ForeignKey("users.t_id", ondelete="CASCADE"), nullable=False)
    n_context = Column(Text, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=func.now())

    user = relationship("User", back_populates="notes")


class DailyRoutine(Base):
    __tablename__ = "daily_routines"

    r_id = Column(BigInteger, primary_key=True, autoincrement=True)
    u_id = Column(BigInteger, ForeignKey("users.t_id", ondelete="CASCADE"), nullable=False)
    r_name = Column(String(255), nullable=False)
    r_type = Column(Enum(RoutineType), nullable=False)

    user = relationship("User", back_populates="daily_routines")


class DailyStatistic(Base):
    __tablename__ = "daily_statistics"

    d_id = Column(BigInteger, primary_key=True, autoincrement=True)
    u_id = Column(BigInteger, ForeignKey("users.t_id", ondelete="CASCADE"), nullable=False)
    performed = Column(Integer, nullable=False, default=0)
    focus_counter = Column(Integer, nullable=False, default=0)
    break_counter = Column(Integer, nullable=False, default=0)
    notes_counter = Column(Integer, nullable=False, default=0)
    streak = Column(Integer, nullable=False, default=0)
    best_streak = Column(Integer, nullable=False, default=0)
    energy_level = Column(Integer, CheckConstraint("energy_level BETWEEN 1 AND 10"), nullable=True)

    user = relationship("User", back_populates="daily_statistics")


class Habit(Base):
    __tablename__ = "habits"

    h_id = Column(BigInteger, primary_key=True, autoincrement=True)
    u_id = Column(BigInteger, ForeignKey("users.t_id", ondelete="CASCADE"), nullable=False)
    h_name = Column(String(255), nullable=False)
    h_status = Column(Enum(TaskStatus), nullable=False, default=TaskStatus.PROCESSING)
    start_h_time = Column(TIMESTAMP, nullable=False)
    finish_h_time = Column(TIMESTAMP, nullable=False)
    h_created_at = Column(TIMESTAMP, nullable=False, server_default=func.now())

    user = relationship("User", back_populates="habits")


class Focus(Base):
    __tablename__ = "focuses"

    f_id = Column(BigInteger, primary_key=True, autoincrement=True)
    u_id = Column(BigInteger, ForeignKey("users.t_id", ondelete="CASCADE"), nullable=False)
    t_id = Column(BigInteger, ForeignKey("tasks.t_id", ondelete="SET NULL"), nullable=True)
    start_time = Column(TIMESTAMP, nullable=False)
    stop_time = Column(TIMESTAMP, nullable=False)
    breaks_counter = Column(Integer, nullable=False, default=0)

    user = relationship("User", back_populates="focuses")
    task = relationship("Task", back_populates="focuses")


class Reminder(Base):
    __tablename__ = "reminders"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    u_id = Column(BigInteger, ForeignKey("users.t_id", ondelete="CASCADE"), nullable=False)
    task_id = Column(BigInteger, ForeignKey("tasks.t_id", ondelete="CASCADE"), nullable=True)
    reminder_time = Column(TIMESTAMP, nullable=False)
    repeat_interval = Column(Interval, nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(TIMESTAMP, server_default=func.now())

    user = relationship("User", back_populates="reminders")
    task = relationship("Task", back_populates="reminders")
