import enum

class UserState(enum.Enum):
    LOGGING = "LOGGING",
    WORKING = "WORKING",
    START_TIME_SET = "START_TIME_SET"
    MAKING_NOTE = "MAKING_NOTE"