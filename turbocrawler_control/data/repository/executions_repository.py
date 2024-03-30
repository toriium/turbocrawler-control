from turbocrawler_control.data.db_orm.query_obj import insert_obj, select_all_obj
from turbocrawler_control.data.db_orm.tables import TblExecutions
from turbocrawler_control.data.dtos.executions_dto import CreateExecutionDTO, ExecutionDTO
from turbocrawler_control.data.errors.sql_error import SQLError


class ExecutionsRepository:

    @staticmethod
    def get_executions_by_crawler(crawler_id: int) -> tuple[list[ExecutionDTO] | None, SQLError | None]:
        query_result = select_all_obj(obj_table=TblExecutions, filter_by={'crawler_id': crawler_id})
        if query_result:
            executions = []
            for execution in query_result:
                executions.append(ExecutionDTO.model_validate(execution))
            return executions, None
        else:
            return None, None

    @staticmethod
    def create_execution(execution: CreateExecutionDTO) -> ExecutionDTO | None:
        execution_obg = TblExecutions()
        execution_obg.crawler_id = execution.crawler_id
        execution_obg.requests_made = execution.requests_made
        execution_obg.creation_date = execution.creation_date
        execution_obg.updated_date = execution.updated_date

        query_result, error = insert_obj(execution_obg)
        if error:
            print(error)
        return ExecutionDTO.model_validate(query_result)
