
from turbocrawler_control.application.execution.execution_error import ExecutionError
from turbocrawler_control.data.dtos.executions_dto import CreateExecutionDTO
from turbocrawler_control.data.repository.executions_repository import ExecutionsRepository
from turbocrawler_control.domain.execution import ExecutionDomain


class ExecutionService:
    @staticmethod
    def get_executions_by_crawler(crawler_id: int) -> tuple[list[ExecutionDomain] | None, ExecutionError | None]:
        executions, error = ExecutionsRepository.get_executions_by_crawler(crawler_id=crawler_id)

        if not executions:
            return None, None

        return [ExecutionDomain(**execution.model_dump()) for execution in executions], None

    @staticmethod
    def insert_execution(crawler_id: int, requests_made: int) -> tuple[ExecutionDomain | None, ExecutionError | None]:
        execution = CreateExecutionDTO(crawler_id=crawler_id, requests_made=requests_made)

        execution = ExecutionsRepository.create_execution(execution=execution)

        return ExecutionDomain(**execution.model_dump()), None
