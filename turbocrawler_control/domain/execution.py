from datetime import date
from pydantic import BaseModel

from turbocrawler_control.domain.crawler import CrawlerDomain


class ExecutionDomain(BaseModel):
    id: int | None
    crawler_id: int
    requests_made: int
    creation_date: date
    updated_date: date
