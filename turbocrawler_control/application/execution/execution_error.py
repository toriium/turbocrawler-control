from enum import Enum, auto


class ExecutionError(Enum):
    duplicate_entry = auto()
    not_found = auto()
