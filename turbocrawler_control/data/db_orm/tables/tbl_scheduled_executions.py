from sqlalchemy import Column, Date, Integer, String
from datetime import date
from turbocrawler_control.data.db_orm.tables.base import Base


class TblScheduledExecutions(Base):
    __tablename__ = 'tbl_scheduled_executions'

    id = Column(Integer, primary_key=True, autoincrement=True)
    crawler_name = Column(String(100), nullable=False, unique=True)
    creation_date = Column(Date, nullable=False, default=date.today())
