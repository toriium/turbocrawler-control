from turbocrawler_control.application.scheduled_execution.scheduled_execution_error import ScheduledExecutionError
from turbocrawler_control.data.repository.scheduled_executions_repository import ScheduledExecutionsRepository
from turbocrawler_control.domain.scheduled_execution import ScheduledExecutionDomain
from turbocrawler_control.data.errors.repository_error import RepositoryError


class ScheduledExecutionService:

    @staticmethod
    def get_scheduled_execution(crawler_name: str) \
            -> tuple[ScheduledExecutionDomain | None, ScheduledExecutionError | None]:
        scheduled_request, error = ScheduledExecutionsRepository.get_scheduled_execution(crawler_name=crawler_name)

        if error:
            if error == RepositoryError.not_found:
                return None, ScheduledExecutionError.not_found

        return ScheduledExecutionDomain(**scheduled_request.model_dump()), None

    @staticmethod
    def get_all_scheduled_execution() -> tuple[list[ScheduledExecutionDomain] | None, ScheduledExecutionError | None]:
        scheduled_executions, error = ScheduledExecutionsRepository.get_all_scheduled_executions()
        if not scheduled_executions:
            return None, None

        return [ScheduledExecutionDomain(**scheduled_execution.model_dump())
                for scheduled_execution in scheduled_executions], None

    @staticmethod
    def create_scheduled_execution(crawler_name: str) -> ScheduledExecutionError | None:
        error = ScheduledExecutionsRepository.create_scheduled_execution(crawler_name=crawler_name)

        if error:
            return {
                RepositoryError.duplicate_entry: ScheduledExecutionError.duplicate_entry
            }.get(error)

    @classmethod
    def pop_scheduled_execution(cls, crawler_name: str) \
            -> tuple[ScheduledExecutionDomain | None, ScheduledExecutionError | None]:
        scheduled_request, error = cls.get_scheduled_execution(crawler_name=crawler_name)
        if error:
            return None, error

        ScheduledExecutionsRepository.delete_scheduled_execution(crawler_name=crawler_name)

        return ScheduledExecutionDomain(**scheduled_request.model_dump()), None
