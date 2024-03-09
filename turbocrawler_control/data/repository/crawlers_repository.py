from turbocrawler_control.data.db_orm.query_obj import delete_obj, insert_obj, select_first_obj, update_obj, \
    select_all_obj
from turbocrawler_control.data.db_orm.tables.tbl_crawlers import TblCrawlers
from turbocrawler_control.data.dtos.crawlers_dto import CrawlerDTO
from turbocrawler_control.data.errors.sql_error import SQLError
from turbocrawler_control.domain.crawler import CrawlerDomain


class CrawlersRepository:
    @staticmethod
    def find_crawler_by_id(crawler_id: int) -> tuple[CrawlerDTO | None, SQLError | None]:
        query_result = select_first_obj(obj_table=TblCrawlers, filter_by={"id": crawler_id})
        if query_result:
            return CrawlerDTO.model_validate(query_result), None
        else:
            return None, None

    @staticmethod
    def find_crawler_by_name(crawler_name: str) -> tuple[CrawlerDTO | None, SQLError | None]:
        query_result = select_first_obj(obj_table=TblCrawlers, filter_by={"name": crawler_name})
        if query_result:
            return CrawlerDTO.model_validate(query_result), None
        else:
            return None, None

    @staticmethod
    def get_all_crawlers() -> tuple[list[CrawlerDTO] | None, SQLError | None]:
        query_result = select_all_obj(obj_table=TblCrawlers)
        if query_result:
            crawlers = []
            for crawler in query_result:
                crawlers.append(CrawlerDTO.model_validate(crawler))
            return crawlers, None
        else:
            return None, None

    @staticmethod
    def insert_crawler(crawler: CrawlerDomain) -> tuple[CrawlerDTO | None, SQLError | None]:
        new_crawler = TblCrawlers()
        new_crawler.name = crawler.name
        new_crawler.active = crawler.active
        new_crawler.creation_date = crawler.creation_date

        query_result, error = insert_obj(obj=new_crawler)
        if error:
            if error == SQLError.duplicate_entry:
                return None, SQLError.duplicate_entry

        if query_result:
            return CrawlerDTO.model_validate(query_result), None
        else:
            return None, None

    @staticmethod
    def update_crawler(crawler: CrawlerDomain) -> tuple[CrawlerDTO | None, SQLError | None]:
        obj_update = crawler.model_dump()
        query_result, error = update_obj(TblCrawlers, filter_by={"id": crawler.id}, obj_update=obj_update)
        if error:
            if error == SQLError.not_found:
                return None, SQLError.not_found

        if query_result:
            return CrawlerDTO(**crawler.model_dump()), None
        else:
            return None, None

    @staticmethod
    def delete_crawler(crawler_id: int) -> SQLError | None:
        error = delete_obj(obj_table=TblCrawlers, filter_by={"id": crawler_id})
        return error if error else None
