from datetime import date

from turbocrawler_control.application.crawler.crawler_error import CrawlerError
from turbocrawler_control.domain.crawler import Crawler
from turbocrawler_control.data.errors.sql_error import SQLError
from turbocrawler_control.data.repository.crawlers_repository import CrawlersRepository
from turbocrawler_control.presentation.schemas.crawler_schema import CreateCrawlerInput, UpdateCrawlerInput


class CrawlerService:
    @staticmethod
    def find_crawler_by_id(crawler_id: int) -> tuple[Crawler | None, CrawlerError | None]:
        found_crawler, error = CrawlersRepository.find_crawler_by_id(crawler_id=crawler_id)

        if not found_crawler:
            return None, None
        return Crawler(**found_crawler.dict()), None

    @staticmethod
    def find_crawler_by_name(crawler_name: str) -> tuple[Crawler | None, CrawlerError | None]:
        found_crawler, error = CrawlersRepository.find_crawler_by_name(crawler_name=crawler_name)

        if not found_crawler:
            return None, None
        return Crawler(**found_crawler.dict()), None

    @staticmethod
    def insert_crawler(data: CreateCrawlerInput) -> tuple[Crawler | None, CrawlerError | None]:
        creation_date = date.today()
        new_crawler = Crawler(name=data.name, active=True, creation_date=creation_date)

        new_crawler, error = CrawlersRepository.insert_crawler(crawler=new_crawler)
        if error:
            if error == SQLError.duplicate_entry:
                return None, CrawlerError.duplicate_entry

        return Crawler(**new_crawler.dict()), None

    @staticmethod
    def update_crawler(data: UpdateCrawlerInput) -> tuple[Crawler | None, CrawlerError | None]:
        target_crawler = Crawler(**data.dict())

        updated_crawler, error = CrawlersRepository.update_crawler(crawler=target_crawler)
        if error:
            return None, CrawlerError.not_found

        return Crawler(**updated_crawler.dict()), None

    @staticmethod
    def delete_crawler(crawler_id) -> CrawlerError | None:
        error = CrawlersRepository.delete_crawler(crawler_id=crawler_id)
        if error == SQLError.not_found:
            return CrawlerError.not_found
        return None
