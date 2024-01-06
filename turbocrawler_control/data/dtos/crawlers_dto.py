from datetime import date

from pydantic import BaseModel


class CrawlerDTO(BaseModel):
    id: int
    name: str
    active: bool
    creation_date: date

    class Config:
        from_attributes = True


class CreateCrawlerDTO(BaseModel):
    name: str
    active: bool
    creation_date: date
