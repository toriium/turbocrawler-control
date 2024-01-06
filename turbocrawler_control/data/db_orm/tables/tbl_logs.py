from enum import Enum as EnumType

from sqlalchemy import TIMESTAMP, Column, Integer, Text, String, Enum
from sqlalchemy.sql import func

from turbocrawler_control.data.db_orm.tables.base import Base


class LogLevel(EnumType):
    CRITICAL = "CRITICAL"
    FATAL = "FATAL"
    ERROR = "ERROR"
    WARNING = "WARNING"
    INFO = "INFO"
    DEBUG = "DEBUG"
    NOTSET = "NOTSET"


class TblLogs(Base):
    __tablename__ = 'tbl_logs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    running_id = Column(String(21), nullable=False, index=True)
    level = Column(Enum(LogLevel), nullable=False)
    message = Column(Text(), nullable=False)
    creation_date = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
