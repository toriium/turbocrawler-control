from fastapi import APIRouter

from turbocrawler_control.application.execution.execution_service import ExecutionService

from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

execution_router = APIRouter()
templates = Jinja2Templates(directory="presentation/templates")


@execution_router.get("/execution/{crawler_id}", response_class=HTMLResponse)
async def execution(request: Request, crawler_id: int):
    executions, error = ExecutionService.get_executions_by_crawler(crawler_id=crawler_id)

    if executions:
        executions = [execution.model_dump() for execution in executions]
    else:
        executions = []

    return templates.TemplateResponse(request=request, name="execution.html", context={"executions": executions})
