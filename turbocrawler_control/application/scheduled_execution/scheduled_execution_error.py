from enum import Enum, auto


class ScheduledExecutionError(Enum):
    duplicate_entry = auto()
    not_found = auto()
