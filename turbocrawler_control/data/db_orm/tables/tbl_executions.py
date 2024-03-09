from sqlalchemy import Column, Date, Integer, String, Text, Boolean, func, ForeignKey
from datetime import date

from sqlalchemy.orm import relationship

from turbocrawler_control.data.db_orm.tables.base import Base


class TblExecutions(Base):
    __tablename__ = 'tbl_executions'

    id = Column(Integer, primary_key=True, autoincrement=True)
    crawler_id = Column(ForeignKey("tbl_crawlers.id"))
    crawler = relationship("TblCrawlers", back_populates="execution")
    requests_made = Column(Integer, nullable=True)
    creation_date = Column(Date, nullable=False, default=date.today())
    updated_date = Column(Date, nullable=False, default=date.today())