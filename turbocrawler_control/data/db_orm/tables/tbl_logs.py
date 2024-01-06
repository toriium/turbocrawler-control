from sqlalchemy import TIMESTAMP, Column, Integer, Text
from sqlalchemy.sql import func

from turbocrawler_control.data.db_orm.tables.base import Base


class TblLogs(Base):
    __tablename__ = 'tbl_logs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    message = Column(Text(), nullable=False)
    creation_date = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
