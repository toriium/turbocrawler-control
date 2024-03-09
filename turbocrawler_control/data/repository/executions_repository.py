from turbocrawler_control.data.db_orm.query_obj import insert_obj
from turbocrawler_control.data.db_orm.tables import TblExecutions
from turbocrawler_control.data.dtos.crawlers_dto import CrawlerDTO
from turbocrawler_control.data.dtos.executions_dto import CreateExecutionDTO, ExecutionDTO
from turbocrawler_control.data.repository.crawlers_repository import CrawlersRepository


class ExecutionsRepository:
    @staticmethod
    def create_execution(execution: CreateExecutionDTO) -> ExecutionDTO | None:
        execution_obg = TblExecutions()
        execution_obg.crawler = CrawlersRepository.find_crawler_by_id(execution.crawler_id)
        execution_obg.requests_made = execution.requests_made
        execution_obg.creation_date = execution.creation_date
        execution_obg.updated_date = execution.updated_date

        query_result, error = insert_obj(execution_obg)
        if error:
            print(error)
        # crawler = CrawlerDTO()
        return ExecutionDTO(id=query_result.id,crawler=5).model_validate(query_result)
