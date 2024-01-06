from turbocrawler_control.data.db_orm.query_obj import insert_obj
from turbocrawler_control.data.db_orm.tables import TblLogs


class LogsRepository:
    @staticmethod
    def create_log(running_id: str, level: str, message: str) -> None:
        log_obg = TblLogs()
        log_obg.running_id = running_id
        log_obg.level = level
        log_obg.message = message

        query_result, error = insert_obj(log_obg)
        if error:
            print(error)
