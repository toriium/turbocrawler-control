from fastapi import APIRouter, status
from starlette.responses import JSONResponse

from turbocrawler_control.application.crawler.crawler_service import CrawlerService
from turbocrawler_control.presentation.schemas.crawler_schema import *
from turbocrawler_control.presentation.schemas.message_schema import Message

from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

home_router = APIRouter()
templates = Jinja2Templates(directory="presentation/templates")


# @home_router.get(
#     path='/',
#     response_model=FindCrawlerOutput,
#     status_code=200,
#     responses={404: {"model": Message},
#                500: {"model": Message}},
#     tags=["crawler"],
#     description='Get one Crawler'
# )
# async def get_crawler(crawler_id: int):
#     result, error = CrawlerService.find_crawler_by_id(crawler_id=crawler_id)
#     if result:
#         return JSONResponse(content=FindCrawlerOutput(**result.dict()).dict(), status_code=status.HTTP_200_OK)
#
#     return JSONResponse(content={"message": "Not found crawler with this id"}, status_code=status.HTTP_404_NOT_FOUND)


@home_router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    crawlers, error = CrawlerService.get_all_crawlers()

    if crawlers:
        crawlers = [crawler.model_dump() for crawler in crawlers]
    else:
        crawlers = []

    return templates.TemplateResponse(request=request, name="home.html", context={"crawlers": crawlers})
