from datetime import date
from pydantic import BaseModel


class CrawlerDomain(BaseModel):
    id: int | None = None
    name: str
    active: bool
    creation_date: date
