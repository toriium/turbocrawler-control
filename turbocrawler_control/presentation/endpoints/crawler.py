from fastapi import APIRouter, status
from starlette.responses import JSONResponse

from turbocrawler_control.application.crawler.crawler_error import CrawlerError
from turbocrawler_control.application.crawler.crawler_service import CrawlerService
from turbocrawler_control.presentation.schemas.crawler_schema import *
from turbocrawler_control.presentation.schemas.message_schema import Message

crawler_router = APIRouter()


@crawler_router.get(
    path='/crawler',
    response_model=FindCrawlerOutput,
    status_code=200,
    responses={404: {"model": Message},
               500: {"model": Message}},
    tags=["crawler"],
    description='Get one Crawler'
)
async def get_crawler(crawler_id: int):
    result, error = CrawlerService.find_crawler_by_id(crawler_id=crawler_id)
    if result:
        return JSONResponse(content=FindCrawlerOutput(**result.dict()).dict(), status_code=status.HTTP_200_OK)

    return JSONResponse(content={"message": "Not found crawler with this id"}, status_code=status.HTTP_404_NOT_FOUND)


@crawler_router.post(
    path='/crawler',
    response_model=CreateCrawlerOutput,
    status_code=201,
    responses={404: {"model": Message},
               500: {"model": Message}},
    tags=["crawler"],
    description='Create a Crawler'
)
async def create_crawler(payload: CreateCrawlerInput):
    crawler, error = CrawlerService.insert_crawler(data=payload)
    if error:
        if error == CrawlerError.duplicate_entry:
            return JSONResponse(content={"message": "This crawler already exists in our base"},
                                status_code=status.HTTP_400_BAD_REQUEST)

    return JSONResponse(content=CreateCrawlerOutput(**crawler.dict()).dict(), status_code=status.HTTP_201_CREATED)


@crawler_router.put(
    path='/crawler',
    response_model=UpdateCrawlerOutput,
    status_code=200,
    responses={404: {"model": Message},
               500: {"model": Message}},
    tags=["crawler"],
    description='Update a Crawler'
)
async def update_crawler(payload: UpdateCrawlerInput):
    crawler, error = CrawlerService.update_crawler(data=payload)
    if error:
        if error == CrawlerError.not_found:
            return JSONResponse(content={"message": "Crawler not found"}, status_code=status.HTTP_404_NOT_FOUND)

    return JSONResponse(UpdateCrawlerOutput(**crawler.dict()).dict(), status_code=status.HTTP_200_OK)


@crawler_router.delete(
    path='/crawler',
    response_model=Message,
    status_code=200,
    responses={404: {"model": Message},
               500: {"model": Message}},
    tags=["crawler"],
    description='Delete a Crawler'
)
async def delete_crawler(crawler_id: int):
    error = CrawlerService.delete_crawler(crawler_id=crawler_id)
    if error:
        if error == CrawlerError.not_found:
            return JSONResponse(content={"message": "Crawler not found"}, status_code=status.HTTP_404_NOT_FOUND)

    return JSONResponse(content={"message": "Crawler deleted"}, status_code=status.HTTP_200_OK)
