from datetime import date

from pydantic import BaseModel

from turbocrawler_control.data.dtos.crawlers_dto import CrawlerDTO


class ExecutionDTO(BaseModel):
    id: int
    crawler: CrawlerDTO
    requests_made: int
    creation_date: date
    updated_date: date

    class Config:
        from_attributes = True


class CreateExecutionDTO(BaseModel):
    crawler: any
    requests_made: int
    creation_date: date | None = None
    updated_date: date | None = None
