from sqlalchemy import Column, Date, Integer, String, Boolean
from datetime import date
from turbocrawler_control.data.db_orm.tables.base import Base


class TblCrawlers(Base):
    __tablename__ = 'tbl_crawlers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False, unique=True)
    active = Column(Boolean, nullable=False, index=True)
    creation_date = Column(Date, nullable=False, default=date.today())
