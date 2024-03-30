from turbocrawler_control.data.db_orm.query_obj import insert_obj, select_all_obj, select_first_obj, delete_obj
from turbocrawler_control.data.db_orm.tables import TblScheduledExecutions
from turbocrawler_control.data.dtos.scheduled_execution_dto import ScheduledExecutionDTO
from turbocrawler_control.data.errors.repository_error import RepositoryError
from turbocrawler_control.data.errors.sql_error import SQLError


class ScheduledExecutionsRepository:

    @staticmethod
    def get_all_scheduled_executions() -> list[ScheduledExecutionDTO] | None:
        query_result = select_all_obj(obj_table=TblScheduledExecutions)
        if not query_result:
            return None

        scheduled_executions = []
        for scheduled_execution in query_result:
            scheduled_executions.append(ScheduledExecutionDTO.model_validate(scheduled_execution))
        return scheduled_executions

    @staticmethod
    def get_scheduled_execution(crawler_name: str) -> tuple[ScheduledExecutionDTO | None, RepositoryError | None]:
        query_result = select_first_obj(obj_table=TblScheduledExecutions, filter_by={"crawler_name": crawler_name})
        if not query_result:
            return None, RepositoryError.not_found
        return ScheduledExecutionDTO.model_validate(query_result), None

    @staticmethod
    def create_scheduled_execution(crawler_name: str) -> RepositoryError | None:
        obj = TblScheduledExecutions()
        obj.crawler_name = crawler_name

        query_result, error = insert_obj(obj)
        if error and error == SQLError.duplicate_entry:
            return RepositoryError.duplicate_entry

    @staticmethod
    def delete_scheduled_execution(crawler_name: str) -> RepositoryError | None:
        error = delete_obj(obj_table=TblScheduledExecutions, filter_by={"crawler_name": crawler_name})
        if error and error == SQLError.not_found:
            return RepositoryError.not_found
