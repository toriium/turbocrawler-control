from datetime import date

from pydantic import BaseModel


class ScheduledExecutionDTO(BaseModel):
    id: int
    crawler_id: int
    creation_date: date

    class Config:
        from_attributes = True

