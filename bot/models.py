from sqlalchemy import (
    Column, String, BigInteger, Integer, Text,
    Enum, ForeignKey, TIMESTAMP, Boolean, Interval, BIGINT, BigInteger
)
from sqlalchemy.orm import declarative_base, relationship
import enum

Base = declarative_base()

# ------------------- ENUM TYPES -------------------

class LanguageEnum(str, enum.Enum):
    ENGLISH = "ENGLISH"
    RUSSIAN = "RUSSIAN"

class TaskStatus(str, enum.Enum):
    DONE = "DONE"
    PROCESSING = "PROCESSING"

class RoutineType(str, enum.Enum):
    MORNING = "MORNING"
    EVENING = "EVENING"

# ------------------- TABLES -------------------

class User(Base):
    __tablename__ = "users"

    t_id = Column(BigInteger, primary_key=True, index=True)
    t_name = Column(String(255), unique=True, nullable=False)
    language = Column(Enum(LanguageEnum), nullable=False, default=LanguageEnum.ENGLISH)
    created_at = Column(TIMESTAMP, nullable=False)
    wake_up_time = Column(TIMESTAMP)
    sleep_time = Column(TIMESTAMP)

    tasks = relationship("Task", back_populates="user", cascade="all, delete-orphan")
    notes = relationship("Note", back_populates="user", cascade="all, delete-orphan")
    routines = relationship("DailyRoutine", back_populates="user", cascade="all, delete-orphan")
    statistics = relationship("DailyStatistic", back_populates="user", cascade="all, delete-orphan")
    habits = relationship("Habit", back_populates="user", cascade="all, delete-orphan")
    focuses = relationship("Focus", back_populates="user", cascade="all, delete-orphan")
    reminders = relationship("Reminder", back_populates="user", cascade="all, delete-orphan")


class Task(Base):
    __tablename__ = "tasks"

    t_id = Column(BigInteger, primary_key=True, index=True)
    u_id = Column(BigInteger, ForeignKey("users.t_id", ondelete="CASCADE"), nullable=False)
    t_name = Column(String(255), nullable=False)
    t_deadline = Column(TIMESTAMP)
    t_status = Column(Enum(TaskStatus), nullable=False, default=TaskStatus.PROCESSING)
    t_created_at = Column(TIMESTAMP, nullable=False)

    user = relationship("User", back_populates="tasks")
    focuses = relationship("Focus", back_populates="task", cascade="all, delete-orphan")
    reminders = relationship("Reminder", back_populates="task", cascade="all, delete-orphan")


class Note(Base):
    __tablename__ = "notes"

    n_id = Column(BigInteger, primary_key=True)
    u_id = Column(BigInteger, ForeignKey("users.t_id", ondelete="CASCADE"), nullable=False)
    n_context = Column(Text, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)

    user = relationship("User", back_populates="notes")


class DailyRoutine(Base):
    __tablename__ = "daily_routines"

    r_id = Column(BigInteger, primary_key=True)
    u_id = Column(BigInteger, ForeignKey("users.t_id", ondelete="CASCADE"), nullable=False)
    r_name = Column(String(255), nullable=False)
    r_type = Column(Enum(RoutineType), nullable=False)

    user = relationship("User", back_populates="routines")


class DailyStatistic(Base):
    __tablename__ = "daily_statistics"

    d_id = Column(BigInteger, primary_key=True)
    u_id = Column(BigInteger, ForeignKey("users.t_id", ondelete="CASCADE"), nullable=False)
    performed = Column(Integer, default=0, nullable=False)
    focus_counter = Column(Integer, default=0, nullable=False)
    break_counter = Column(Integer, default=0, nullable=False)
    notes_counter = Column(Integer, default=0, nullable=False)
    streak = Column(Integer, default=0, nullable=False)
    best_streak = Column(Integer, default=0, nullable=False)
    energy_level = Column(Integer)

    user = relationship("User", back_populates="statistics")


class Habit(Base):
    __tablename__ = "habits"

    h_id = Column(BigInteger, primary_key=True)
    u_id = Column(BigInteger, ForeignKey("users.t_id", ondelete="CASCADE"), nullable=False)
    h_name = Column(String(255), nullable=False)
    h_status = Column(Enum(TaskStatus), nullable=False, default=TaskStatus.PROCESSING)
    start_h_time = Column(TIMESTAMP, nullable=False)
    finish_h_time = Column(TIMESTAMP, nullable=False)
    h_created_at = Column(TIMESTAMP, nullable=False)

    user = relationship("User", back_populates="habits")


class Focus(Base):
    __tablename__ = "focuses"

    f_id = Column(BigInteger, primary_key=True)
    u_id = Column(BigInteger, ForeignKey("users.t_id", ondelete="CASCADE"), nullable=False)
    t_id = Column(BigInteger, ForeignKey("tasks.t_id", ondelete="SET NULL"))
    start_time = Column(TIMESTAMP, nullable=False)
    stop_time = Column(TIMESTAMP, nullable=False)
    breaks_counter = Column(Integer, nullable=False, default=0)

    user = relationship("User", back_populates="focuses")
    task = relationship("Task", back_populates="focuses")


class Reminder(Base):
    __tablename__ = "reminders"

    id = Column(BigInteger, primary_key=True)
    u_id = Column(BigInteger, ForeignKey("users.t_id", ondelete="CASCADE"), nullable=False)
    task_id = Column(BigInteger, ForeignKey("tasks.t_id", ondelete="CASCADE"))
    reminder_time = Column(TIMESTAMP, nullable=False)
    repeat_interval = Column(Interval)
    is_active = Column(Boolean, default=True)
    created_at = Column(TIMESTAMP)

    user = relationship("User", back_populates="reminders")
    task = relationship("Task", back_populates="reminders")
