from datetime import date

from pydantic import BaseModel


class ScheduledExecutionDomain(BaseModel):
    id: int
    crawler_name: str
    creation_date: date
