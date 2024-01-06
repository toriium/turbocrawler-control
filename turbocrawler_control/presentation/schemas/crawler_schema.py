from pydantic import BaseModel


class FindCrawlerOutput(BaseModel):
    id: int
    name: str


class CreateCrawlerInput(BaseModel):
    name: str


class CreateCrawlerOutput(BaseModel):
    name: str


class UpdateCrawlerInput(BaseModel):
    id: int
    name: str


class UpdateCrawlerOutput(BaseModel):
    id: int
    name: str
