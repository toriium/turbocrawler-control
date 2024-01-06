from enum import Enum, auto


class CrawlerError(Enum):
    duplicate_entry = auto()
    not_found = auto()
