import logging

from turbocrawler import CrawlerRequest, CrawlerResponse, CrawlerRunner, ExecutionInfo
from turbocrawler.engine.plugin import Plugin
from turbocrawler_control.application.crawler.crawler_service import CrawlerService
from turbocrawler.engine.control import StopCrawler
from turbocrawler_control.application.execution.execution_service import ExecutionService
from turbocrawler_control.data.repository.logs_repository import LogsRepository
from turbocrawler_control.presentation.schemas.crawler_schema import CreateCrawlerInput
from turbocrawler_control.domain.crawler import CrawlerDomain


class TurboCrawlerControlHandler(logging.StreamHandler):
    def __init__(self, crawler, crawler_domain: CrawlerDomain, running_id: str):
        super().__init__()
        self.crawler = crawler
        self.crawler_domain = crawler_domain
        self.running_id = running_id
        self.crawler_id = CrawlerService.find_crawler_by_name(crawler_name=crawler.crawler_name)

    def emit(self, record: logging.LogRecord):
        if hasattr(record, 'json'):
            data = record.json
            ExecutionService.insert_execution(crawler_id=self.crawler_domain.id,
                                              requests_made=data['requests_made'])
        else:
            LogsRepository.create_log(running_id=self.running_id, level=record.levelname, message=record.msg)


class TurboCrawlerPlugin(Plugin):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        crawler_name = self.crawler.crawler_name
        crawler_domain, error = CrawlerService.find_crawler_by_name(crawler_name)
        if error:
            raise StopCrawler("error to find crawler")

        if not crawler_domain:
            new_crawler = CreateCrawlerInput(name=crawler_name)
            crawler_domain, error = CrawlerService.insert_crawler(new_crawler)

        self.crawler_domain = crawler_domain

    def start_crawler(self) -> None:
        print("[TurboCrawlerPlugin] start_crawler")

    def crawler_first_request(self) -> None:
        print("[TurboCrawlerPlugin] crawler_first_request")

    def process_request(self, crawler_request: CrawlerRequest) -> CrawlerResponse | CrawlerRequest | None:
        print("[TurboCrawlerPlugin] process_request")
        return None

    def process_response(self, crawler_request: CrawlerRequest, crawler_response: CrawlerResponse):
        print("[TurboCrawlerPlugin] process_response")

    def stop_crawler(self, execution_info: ExecutionInfo) -> None:
        print("[TurboCrawlerPlugin] process_request")

    def log_handler(self, crawler, running_id: str) -> logging.Handler | None:
        return TurboCrawlerControlHandler(crawler=crawler, crawler_domain=self.crawler_domain, running_id=running_id)
