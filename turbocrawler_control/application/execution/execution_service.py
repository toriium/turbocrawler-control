from datetime import date

from turbocrawler_control.application.crawler.crawler_error import CrawlerError
from turbocrawler_control.application.crawler.crawler_service import CrawlerService
from turbocrawler_control.application.execution.execution_error import ExecutionError
from turbocrawler_control.data.dtos.executions_dto import CreateExecutionDTO
from turbocrawler_control.data.repository.executions_repository import ExecutionsRepository
from turbocrawler_control.domain.execution import ExecutionDomain
from turbocrawler_control.data.errors.sql_error import SQLError
from turbocrawler_control.data.repository.crawlers_repository import CrawlersRepository
from turbocrawler_control.presentation.schemas.crawler_schema import CreateCrawlerInput, UpdateCrawlerInput


class ExecutionService:
    @staticmethod
    def insert_execution(crawler_name: str, requests_made: int) -> tuple[ExecutionDomain | None, ExecutionError | None]:
        crawler, error = CrawlerService.find_crawler_by_name(crawler_name=crawler_name)
        if error:
            if error == CrawlerError.not_found:
                return None, ExecutionError.not_found

        execution = CreateExecutionDTO(crawler=crawler.id, requests_made=requests_made)

        execution = ExecutionsRepository.create_execution(execution=execution)

        return ExecutionDomain(**execution.model_dump()), None

