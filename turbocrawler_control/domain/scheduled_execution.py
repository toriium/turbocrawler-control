from datetime import date

from pydantic import BaseModel


class ScheduledExecutionDomain(BaseModel):
    id: int
    crawler_id: int
    creation_date: date
